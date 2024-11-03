#-*-coding:utf-8;-*-
from ctypes import cast,c_char,c_char_p
from typing import Tuple
from .core import LIBRARY
rtlsdr_get_device_count=LIBRARY.rtlsdr_get_device_count
rtlsdr_get_device_name=LIBRARY.rtlsdr_get_device_name
def rtlsdr_get_device_usb_strings(index:int)->Tuple[int,bytes,bytes,bytes]:
    manufact=(c_char*256)()
    product=(c_char*256)()
    serial=(c_char*256)()
    returnCode=LIBRARY.rtlsdr_get_device_usb_strings(index,cast(manufact,c_char_p),cast(product,c_char_p),cast(serial,c_char_p))
    if returnCode:
        return returnCode,b"",b"",b""
    else:
        return returnCode,manufact.value,product.value,serial.value
rtlsdr_get_index_by_serial=LIBRARY.rtlsdr_get_index_by_serial