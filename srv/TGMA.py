
from misc.srv.TG124A import TG124A_freq
from misc.srv.MA24118A import MA24118A_freq

def TGMA_freq(freq='1000'):
    TG124A_freq(freq)
    freq1 = '%g' % (float(freq)/1000)
    MA24118A_freq(TGMA_port.port, freq1)
    return freq

def TGMA_port(port = 'ttyACM0'):
    if port:
        TGMA_port.port = port
    return TGMA_port.port
TGMA_port.port = 'ttyACM0'

def TGMA_offset(offset='140'):
    if offset:
        TGMA_offset.offset = offset
    return TGMA_offset.offset
TGMA_offset.offset = '0'

