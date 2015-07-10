
from collections import OrderedDict as OD
from util import Data, get_columns, control_cb, dev_serial_io_cb
from util.columns import *

def columns():
    return get_columns([c_serial])

def tooltips(*args):
    return {c_serial:'MA24118A serial port'}

def get_menu(dev):
    return OD([('Control', control_cb)])

def get_ctrl(dev):
    data = Data('ctrl', send=True, io_cb=dev_serial_io_cb)
    data.add('freq', label='Frequency, MHz', wdgt='spin', value=Data.spn(0.1, 12400, 0.1), text='1000')
    data.add('offset', label='TG - MA, MHz', wdgt='spin', value=Data.spn(0.1, 12400, 0.1), text='140')
    return data

