
from misc.srv.TG124A import TG124A_freq
from misc.srv.MA24118A import MA24118A_freq

def TGMA_freq(port='ttyACM0', freq='1000'):
    TG124A_freq(freq)
    freq1 = '%.g' % (float(freq)/1000)
    MA24118A_freq(port, freq1)
    return freq

def TGMA_offset(offset='140'):
    if v:
        TGMA_offset.offset = offset
    return TGMA_offset.offset
TGMA_offset.offset = '0'

