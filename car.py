#!/bin/python3
import sys
sys.path.append("$LD_LIBRARY_PATH")

from window import *

win = CarWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
