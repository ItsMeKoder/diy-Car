all :
	nuitka3 ./car.py -o car 
	nuitka3 --module ./about.py
	nuitka3 --module ./preference.py
	nuitka3 --module ./window.py
	rm  -rf *.build
	rm -rf *.pyi
test :
	python3 car.py
install : all
	mkdir -p $(DESTDIR)/usr/share/car-wifi-control/
	mkdir -p $(DESTDIR)/usr/share/applications/
	mkdir -p $(DESTDIR)/usr/bin/
	cp car $(DESTDIR)/usr/share/car-wifi-control/
	cp icon.svg $(DESTDIR)/usr/share/car-wifi-control/
	cp com.github.kavishdev.car-wifi-control.desktop $(DESTDIR)/usr/share/applications/
	cp  *.so $(DESTDIR)/usr/share/car-wifi-control
	./.link
