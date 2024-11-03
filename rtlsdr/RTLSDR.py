#-*-coding:utf-8;-*-
from ctypes import byref,cast,c_char,c_char_p,c_int,c_ubyte,c_uint32,c_uint8,c_void_p,POINTER
from typing import Callable,Tuple,Union
from numpy import ubyte
from numpy.ctypeslib import as_array
from numpy.typing import NDArray
from .core import LIBRARY,rtlsdr_read_async_cb_t
from .const import rtlsdr_tuner
def rtlsdr_open(index:int)->Tuple[int,Union[int,None]]:
    dev=c_void_p()
    return LIBRARY.rtlsdr_open(byref(dev),index),dev.value
rtlsdr_close=LIBRARY.rtlsdr_close
rtlsdr_set_xtal_freq=LIBRARY.rtlsdr_set_xtal_freq
def rtlsdr_get_xtal_freq(dev:Union[int,None])->Tuple[int,int,int]:
    rtl_freq=c_uint32()
    tuner_freq=c_uint32()
    returnCode=LIBRARY.rtlsdr_get_xtal_freq(dev,byref(rtl_freq),byref(tuner_freq))
    if returnCode:
        return returnCode,-1,-1
    else:
        return returnCode,rtl_freq.value,tuner_freq.value
def rtlsdr_get_usb_strings(dev:Union[int,None])->Tuple[int,bytes,bytes,bytes]:
    manufact=(c_char*256)()
    product=(c_char*256)()
    serial=(c_char*256)()
    returnCode=LIBRARY.rtlsdr_get_usb_strings(dev,cast(manufact,c_char_p),cast(product,c_char_p),cast(serial,c_char_p))
    if returnCode:
        return returnCode,b"",b"",b""
    else:
        return returnCode,manufact.value,product.value,serial.value
def rtlsdr_write_eeprom(dev:Union[int,None],data:bytes,offset:int)->int:
    return LIBRARY.rtlsdr_write_eeprom(dev,cast((c_uint8*len(data))(*data),POINTER(c_uint8)),offset,len(data))
def rtlsdr_read_eeprom(dev:Union[int,None],offset:int,len:int)->Tuple[int,bytes]:
    data=(c_uint8*len)()
    returnCode=LIBRARY.rtlsdr_read_eeprom(dev,cast(data,POINTER(c_uint8)),offset,len)
    if returnCode:
        return returnCode,b""
    else:
        return returnCode,bytes(data[:])
rtlsdr_set_center_freq=LIBRARY.rtlsdr_set_center_freq
rtlsdr_get_center_freq=LIBRARY.rtlsdr_get_center_freq
rtlsdr_set_freq_correction=LIBRARY.rtlsdr_set_freq_correction
rtlsdr_get_freq_correction=LIBRARY.rtlsdr_get_freq_correction
def rtlsdr_get_tuner_type(dev:Union[int,None])->rtlsdr_tuner:
    return rtlsdr_tuner(LIBRARY.rtlsdr_get_tuner_type(dev))
def rtlsdr_get_tuner_gains(dev:Union[int,None])->Tuple[int,Tuple[int,...]]:
    returnCode=LIBRARY.rtlsdr_get_tuner_gains(dev,POINTER(c_int)())
    if returnCode>0:
        gains=(c_int*returnCode)()
        returnCode=LIBRARY.rtlsdr_get_tuner_gains(dev,cast(gains,POINTER(c_int)))
        if returnCode>0:
            return returnCode,(*gains[:returnCode],)
        else:
            return returnCode,()
    else:
        return returnCode,()
rtlsdr_set_tuner_gain=LIBRARY.rtlsdr_set_tuner_gain
rtlsdr_set_tuner_bandwidth=LIBRARY.rtlsdr_set_tuner_bandwidth
rtlsdr_get_tuner_gain=LIBRARY.rtlsdr_get_tuner_gain
rtlsdr_set_tuner_if_gain=LIBRARY.rtlsdr_set_tuner_if_gain
rtlsdr_set_tuner_gain_mode=LIBRARY.rtlsdr_set_tuner_gain_mode
rtlsdr_set_sample_rate=LIBRARY.rtlsdr_set_sample_rate
rtlsdr_get_sample_rate=LIBRARY.rtlsdr_get_sample_rate
rtlsdr_set_testmode=LIBRARY.rtlsdr_set_testmode
rtlsdr_set_agc_mode=LIBRARY.rtlsdr_set_agc_mode
rtlsdr_set_direct_sampling=LIBRARY.rtlsdr_set_direct_sampling
rtlsdr_get_direct_sampling=LIBRARY.rtlsdr_get_direct_sampling
rtlsdr_set_offset_tuning=LIBRARY.rtlsdr_set_offset_tuning
rtlsdr_get_offset_tuning=LIBRARY.rtlsdr_get_offset_tuning
rtlsdr_reset_buffer=LIBRARY.rtlsdr_reset_buffer
def rtlsdr_read_sync(dev:Union[int,None],len:int)->Tuple[int,NDArray[ubyte]]:
    buf=(c_ubyte*len)()
    n_read=c_int()
    return LIBRARY.rtlsdr_read_sync(dev,byref(buf),len,byref(n_read)),as_array(cast(buf,POINTER(c_ubyte)),(n_read.value,))
def rtlsdr_wait_async(dev:Union[int,None],ctx:Union[int,None])->Callable[[Callable[[NDArray[ubyte],Union[int,None]],None]],Union[rtlsdr_read_async_cb_t,None]]:
    def real_rtlsdr_wait_async(cb:Callable[[NDArray[ubyte],Union[int,None]],None])->Union[rtlsdr_read_async_cb_t,None]:
        real_cb=rtlsdr_read_async_cb_t(lambda buf,len,ctx:cb(as_array(buf,(len,)),ctx))
        if not LIBRARY.rtlsdr_wait_async(dev,real_cb,ctx):
            return real_cb
    return real_rtlsdr_wait_async
def rtlsdr_read_async(dev:Union[int,None],ctx:Union[int,None],buf_num:int,buf_len:int)->Callable[[Callable[[NDArray[ubyte],Union[int,None]],None]],Union[rtlsdr_read_async_cb_t,None]]:
    def real_rtlsdr_read_async(cb:Callable[[NDArray[ubyte],Union[int,None]],None])->Union[rtlsdr_read_async_cb_t,None]:
        real_cb=rtlsdr_read_async_cb_t(lambda buf,len,ctx:cb(as_array(buf,(len,)),ctx))
        if not LIBRARY.rtlsdr_read_async(dev,real_cb,ctx,buf_num,buf_len):
            return real_cb
    return real_rtlsdr_read_async
rtlsdr_cancel_async=LIBRARY.rtlsdr_cancel_async
rtlsdr_set_bias_tee=LIBRARY.rtlsdr_set_bias_tee
rtlsdr_set_bias_tee_gpio=LIBRARY.rtlsdr_set_bias_tee_gpio