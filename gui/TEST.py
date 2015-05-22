
from collections import OrderedDict as OD
from util import Data, get_columns, control_cb, monitor_cb, dev_io_cb

def columns():
    return get_columns()

def get_menu(dev):
    return OD([('Control', control_cb), ('Monitor', monitor_cb)])

def get_ctrl(dev):
    data = Data('ctrl', send=True, io_cb=dev_io_cb)
    data.add('ctrl1', label='Test ctrl value1', wdgt='spin', value=Data.spn(0, 10), text='0')
    return data

def get_mntr(dev):
    data = Data('mntr', send=True, io_cb=dev_io_cb)
    data.add('mntr1', wdgt='entry', msg='Test mntr value1', width=10)
    return data

