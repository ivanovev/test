
from . import gui, srv
from util.columns import *
from util.misc import app_devtypes

devdata = lambda: get_devdata('TEST', get_columns([c_serial]), app_devtypes(gui))

