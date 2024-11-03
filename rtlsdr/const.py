#-*-coding:utf-8;-*-
from enum import IntEnum
class rtlsdr_ds_mode(IntEnum):
    RTLSDR_DS_IQ=0
    RTLSDR_DS_I=1
    RTLSDR_DS_Q=2
class rtlsdr_tuner(IntEnum):
    RTLSDR_TUNER_UNKNOWN=0
    RTLSDR_TUNER_E4000=1
    RTLSDR_TUNER_FC0012=2
    RTLSDR_TUNER_FC0013=3
    RTLSDR_TUNER_FC2580=4
    RTLSDR_TUNER_R820T=5
    RTLSDR_TUNER_R828D=6