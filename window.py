import gi
import os,sys,getopt
from about import *
from preference import *
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio

class CarWindow(Gtk.Window):


    def on_hbb_clicked(self, button):
        self.popover.set_relative_to(button)
        self.popover.show_all()
        self.popover.popup()

    def print_usage(self):
        print("This is a simple Program to control a car")
    def ip(self,argv):
        opts, args = getopt.getopt(argv,"hi:o:",["ip="])
          
        for opt, arg in opts:
            if opt == '-h':
                self.print_usage()
                sys.exit()
            elif opt == '--h':
                self.print_usage()
                sys.exit()
            elif opt == '--help':
                self.print_usage()
                sys.exit()
            elif opt == '--h':
                self.print_usage()
                sys.exit()
            elif opt in ("i", "--ip"):
                ip = arg
        return ip
        
    def __init__(self):
        
        ipath=os.getcwd()+"/icon.svg"
        Gtk.Window.__init__(self, title="Car Control")
        self.set_border_width(10)
        self.set_default_size(400, 300)
        
        self.set_icon_from_file(ipath)


        
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Car Control"
        self.set_titlebar(hb)


        outerbox = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)
        hb.add(outerbox)
        hbox = Gtk.Box(spacing=6, orientation=Gtk.Orientation.HORIZONTAL)
        hb.add(hbox)
        
        button = Gtk.Button(label="IP")
        button.connect("clicked", self.on_hbb_clicked)
        outerbox.pack_start(button, False, True, 0)

        self.popover = Gtk.Popover()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        entry=Gtk.Entry()
        
        #currentip="192.168.1.73"
        #entry.set_text(currentip)
        
        global changedip
        changedip = ""
        changedip = entry.get_text()
        print(changedip)
        entry.set_text(changedip)
            
        def chip():
            return changedip
        
        vbox.pack_start(entry, False, True, 10)
        self.popover.add(vbox)
        self.popover.set_position(Gtk.PositionType.BOTTOM)
        
        def r(self):
            print(chip())
            print (changedip)
            entry.set_text(changedip)
            os.system("curl "+changedip+"/right")
        def l(self):
            print(chip())
            print (changedip)
            os.system("curl "+changedip+"/right")
        def f(self):
            print(chip())
            print (changedip)
            os.system("curl "+changedip+"/right")
        def b(self):
            print(chip())
            print (changedip)
            os.system("curl "+changedip+"/right")
        
        btRight=Gtk.Button(label="Right")
        btRight.connect('clicked',r)
        btRight.set_halign(Gtk.Align.END)
        btRight.set_valign(Gtk.Align.CENTER)    
        
        
        
        btLeft=Gtk.Button(label="Left")
        btLeft.connect('clicked',l)
        btLeft.set_halign(Gtk.Align.START)
        btLeft.set_valign(Gtk.Align.CENTER)    

        btForward=Gtk.Button(label="Forward")
        btForward.connect('clicked',f)
        btForward.set_halign(Gtk.Align.CENTER)
        btForward.set_valign(Gtk.Align.START)    



        btBackward=Gtk.Button(label="Backward")
        btBackward.connect('clicked',b)
        btBackward.set_halign(Gtk.Align.CENTER)
        btBackward.set_valign(Gtk.Align.END)    

        btAbout=Gtk.Button(label="About")
        btAbout.connect('clicked',self.about)
        btAbout.set_halign(Gtk.Align.CENTER)
        btAbout.set_valign(Gtk.Align.CENTER)

        btPreferences=Gtk.Button(label="Preferences")
        btPreferences.connect('clicked',self.preferences)
        btPreferences.set_halign(Gtk.Align.CENTER)
        btPreferences.set_valign(Gtk.Align.CENTER) 


        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")

        button = Gtk.Button()
        button.add(
            Gtk.Arrow(arrow_type=Gtk.ArrowType.LEFT, shadow_type=Gtk.ShadowType.NONE)
        )
        box.add(button)

        button = Gtk.Button()
        button.add(
            Gtk.Arrow(arrow_type=Gtk.ArrowType.RIGHT, shadow_type=Gtk.ShadowType.NONE)
        )
        box.add(button)

        #hb.pack_start(box)
        
        mainbox=Gtk.Box()
        #self.add(mainbox)


        btRight.set_property("width-request", 100)
        btRight.set_property("height-request", 30)
        
        btBackward.set_property("width-request", 100)
        btBackward.set_property("height-request", 30)
        
        btLeft.set_property("width-request", 100)
        btLeft.set_property("height-request", 30)
        
        btForward.set_property("width-request", 100)
        btForward.set_property("height-request", 30)
            

##        mainbox.pack_start(btLeft,True,True, 0)
        
        vbox.pack_start(btAbout,True,True, 1)
        vbox.pack_start(btPreferences,True,True, 1)


        labelc=Gtk.Label(label="Car Control")
        grid=Gtk.Grid()
        grid.set_column_spacing(100)
        grid.set_row_spacing(100)
        grid.attach(btRight,2,1,1,1)
        grid.attach(btLeft,0,1,1,1)
        grid.attach(labelc,1,1,1,1)
        grid.attach(btForward,1,0,1,1)
        grid.attach(btBackward,1,2,1,1)
##        
##        
##        mainbox.pack_start(btBackward,True,True,0)
##
##        mainbox.pack_start(btForward,True,True,0)
##
##        mainbox.pack_start(btRight,True,True,0)
        self.add(grid)
    def about(self,button) :
        AboutDialog()
        #win = AboutDialog()
        #win.connect("destroy", Gtk.main_quit)
        #win.show_all()
        #Gtk.main()

    def preferences(self,button) :
        win = PreferenceDialog()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()


    #def right(self, button) :
        #r="curl "+i+"/right"
        #os.system(r) 
       
    #def left(self, button):
        #l="curl "+i+"/left"
        #os.system(l)
    #def backward(self, button):
        #b="curl "+i+"/backward"
        #os.system(b) 
    #def forward(self, button):
        #f="curl "+i+"/forward"
        #os.system(f) 



