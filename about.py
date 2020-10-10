import gi
import os,sys,getopt


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
class AboutDialog(Gtk.AboutDialog):
    def __init__(self):

        ipath=os.getcwd()+"/icon.svg"
        Gtk.Window.__init__(self, title="Car Control")
        self.set_border_width(10)
        self.set_default_size(400, 300)
        
        self.set_icon_from_file(ipath)
        hb = Gtk.HeaderBar()

        hb.set_show_close_button(True)
        hb.props.title = "About Car Control"
        
        #self.set_titlebar(hb)
        self.set_program_name("Car Control")
        self.set_version("0.1")
        self.set_authors("Kavish Devar \n Contributers : Sendil Devar")
        self.set_copyright("(c) Kavish")
        self.set_comments("Car Wifi Controlling")
        self.set_website("https://www.kavish.sendildevar.in")
        self.run()
        self.destroy()
