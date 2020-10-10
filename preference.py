import gi
import os,sys,getopt


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
class PreferenceDialog(Gtk.Dialog):
    def __init__(self):

        ipath=os.getcwd()+"/icon.svg"
        Gtk.Window.__init__(self, title="Car Control Preferences")
        self.set_border_width(10)
        self.set_default_size(400, 300)
        
        self.set_icon_from_file(ipath)
        hb = Gtk.HeaderBar()

        hb.set_show_close_button(True)
        hb.props.title = "Preferences for Car Control"

        box=self.get_content_area()
        #self.add(box)
        label=Gtk.Label(label="a")
##        label1=Gtk.Label(label="b")
##        label2=Gtk.Label(label="c")
##        label3=Gtk.Label(label="d")
##            
##        grid=Gtk.Grid()
##        grid.attach(label1,1,1,1,1)
##        grid.attach(label,2,2,1,1)
##        grid.attach(label2,1,0,1,1)
##        grid.attach(label3,0,0,1,1)
        
        box.pack_start(label,True,True,0)
        self.set_titlebar(hb)
##        self.run()
##        self.destroy()
