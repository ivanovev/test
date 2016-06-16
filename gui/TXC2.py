
from collections import OrderedDict as OD
from util.columns import *
from util import Data, process_cb, control_cb, monitor_cb, dev_io_cb
from ..tools.plottxc2 import PlotTXC2

def startup_cb(apps, mode, dev):
    if mode == 'ch1up':
        return PlotTXC2(dev, '1', True)
    if mode == 'ch1down':
        return PlotTXC2(dev, '1', False)
    if mode == 'ch2up':
        return PlotTXC2(dev, '2', True)
    if mode == 'ch2down':
        return PlotTXC2(dev, '2', False)

def columns():
    return get_columns([c_serial])

def get_menu(dev):
    menu = OD()
    for ch in [1, 2]:
        k = 'ODP.CH%d' % ch
        menu[k] = OD()
        menu[k]['Voltage up'] = lambda dev, ch=ch: process_cb('ch%dup' % ch, dev)
        menu[k]['Voltage down'] = lambda dev, ch=ch: process_cb('ch%ddown' % ch, dev)
    return menu

def get_ctrl(dev):
    data = Data('TestControl', send=True, io_cb=dev_io_cb)
    data.add('ctrl1', label='Test ctrl value1', wdgt='spin', value={'min':0, 'max':50, 'step':0.001}, text='7')
    data.add('ctrl2', label='Test ctrl value2', wdgt='spin', value={'min':0, 'max':50, 'step':0.001}, text='15')
    return data

def get_mntr(dev):
    data = Data('TestMonitor', send=True, io_cb=dev_io_cb)
    data.add('mntr1', wdgt='entry', msg='Test mntr value1', width=20)
    data.add('mntr2', wdgt='entry', msg='Test mntr value2', width=20)
    return data

