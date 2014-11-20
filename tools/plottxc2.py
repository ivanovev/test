
from util.plot import Plot, PlotData, get_cmdsx
import tkinter as tk
import tkinter.ttk as ttk
from util.columns import *
import pdb

class PlotTXC2(Plot):
    def __init__(self, dev, odpch='1', sign=True):
        self.odpch = odpch
        self.start = False
        self.sign = sign
        data = self.get_data(dev)
        data.dev = dev
        Plot.__init__(self, 'fx', data=data)
        self.root.title(self.odpcmd)

    def get_data(self, dev):
        data = PlotData()
        data.add_page('x')
        self.odpcmd = 'ODP3032.SCH%sV' % self.odpch
        data.add(self.odpcmd, cmd=self.odpcmd, send=True, dev={'type':'TXC2', 'server':dev[c_server], 'name':'txc2'})
        data.add_page('y')
        data.add('fetch', label='Current, A', cmd='TH1951.fetch %s' % dev[c_serial], send=True, dev={'type':'TH1951', 'server':dev[c_server], 'name':'TH1951'})
        data.update(get_cmdsx('fx'))
        data.set_value('min', '7')
        data.set_value('max', '16')
        data.set_value('step', '0.01')
        #data.print_data()
        return data

    def plot_cb3(self):
        Plot.plot_cb3(self, io_start_after_idle=self.start)
        #self.root.after_idle(self.io.start)
        return True

    def init_layout(self):
        Plot.init_layout(self)
        self.add_wdgts()
        self.fig.canvas.mpl_connect('button_press_event', self.double_button_cb)
        #self.root.after_idle(self.io.start)

    def add_wdgts(self):
        self.data.select('fx')
        self.data.cmds.pop('step')
        self.data.add_page('wdgts')
        self.data.cmds.columns=20
        self.data.add('step', wdgt='combo', width=5, value=['0.01', '0.05', '0.1', '0.5', '1'], text='1', label='Step (%s)' % ('+' if getattr(self, 'sign', True) else '-'))
        self.data.add('step_do', wdgt='button', text='Step', click_cb=self.step_cb)
        self.data.add('step_undo', wdgt='button', text='Undo', click_cb=self.undo_cb)
        self.data.add('reset', wdgt='button', text='Reset', click_cb=self.reset_cb)
        fb1 = tk.Frame(self.fb)
        fb1.grid(column=0, row=1, sticky=tk.W, columnspan=2)
        self.init_frame(fb1, self.data.cmds)
        self.data.cmds.f.pack(fill=tk.BOTH, expand=1, padx=5)

    def step_cb(self):
        step1 = float(self.data.get_value('step'))
        if not hasattr(self, 'step'):
            self.step = step1
        else:
            step = self.step
            if step1 < step:
                self.step = step1
        self.root.after_idle(self.io.start)

    def undo_cb(self):
        cmds = self.data['y']
        x1, x2 = self.get_xlim()
        xprev = x1
        for k,v in cmds.items():
            if len(v.xx) == 1 and len(v.xx[0]) <= 1:
                continue
            v.xx[-1].pop(-1)
            v.yy[-1].pop(-1)
            if len(v.xx[-1]) == 0:
                if len(v.xx) > 1:
                    v.xx.pop(-1)
                    v.yy.pop(-1)
            if len(v.xx) >= 1 and len(v.xx[-1]) > 0:
                xprev = v.xx[-1][-1]
        self.redraw_all()
        self.data.select('x')
        k,v = list(self.data.cmds.items())[0]
        self.data.set_value(k, '%g' % x1)
        self.data.do_cmds(self.qo, read=False)
        self.qo.put('sleep 3')
        self.data.set_value(k, '%g' % xprev)
        self.data.do_cmds(self.qo, read=False)
        self.x = xprev
        self.root.after_idle(lambda: self.io.start(do_cb1=False))

    def reset_cb(self):
        self.start = False
        self.clear_plot()
        self.root.after_idle(self.io.start)

    def start_stop_io_cb(self, start=True):
        self.start = start
        if start:
            self.root.after_idle(self.io.start)

    def clear_plot(self):
        cmds = self.data['y']
        for k,v in cmds.items():
            v.xx = [[]]
            v.yy = [[]]
        self.redraw_all()
        delattr(self, 'x')
        delattr(self, 'step')

    def double_button_cb(self, evt):
        if evt.dblclick and not self.start:
            x1, x2 = self.get_xlim()
            x = self.round_to(evt.xdata, float(self.data.get_value('step')))
            #print(x, self.x, evt.xdata)
            if (x > self.x) if getattr(self, 'sign', True) else (x < self.x):
                self.data.select('x')
                k,v = list(self.data.cmds.items())[0]
                self.data.set_value(k, '%g' % x)
                #print(self.data.get_value(k))
                self.data.do_cmds(self.qo, read=False)
                self.data.select('y')
                self.data.do_cmds(self.qo, read=True)
                self.root.after_idle(lambda: self.io.start(do_cb1=False))
                self.x = x

    def round_to(self, n, precission):
        correction = 0.5 if n >= 0 else -0.5
        return int(n/precission+correction)*precission

