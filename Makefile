VERSION=4.5

DEBUG=-g -W -pedantic #-pg #-fprofile-arcs
LDFLAGS+=-L/usr/local/hidapi.git/lib -lhidapi-libusb
CXXFLAGS+=-O3 -Wall -DVERSION=\"$(VERSION)\" $(DEBUG) -I/usr/local/hidapi.git/include
CFLAGS+=$(CXXFLAGS)

OBJS=main.o USBaccess.o USBaccessBasic.o error.o
TRANSLATIONS=nl.mo

all: clewarecontrol

nl.mo: nl.po
	msgfmt -o nl.mo nl.po

clewarecontrol: $(OBJS) $(TRANSLATIONS)
	$(CXX) $(OBJS) $(LDFLAGS) -o clewarecontrol

cleware_python cleware_python3:  pyswig
	$(subst cleware_,,$@) setup.py install

pyswig:
	swig -c++ -python cleware.i

cleware_perl:
	swig -c++ -perl5 cleware.i
	g++ -c `perl -MConfig -e 'print join(" ", @Config{qw(ccflags optimize cccdlflags)}, "-I$$Config{archlib}/CORE")'` cleware_wrap.cxx USBaccessBasic.cpp USBaccess.cpp
	g++ `perl -MConfig -e 'print $$Config{lddlflags}'` cleware_wrap.o USBaccessBasic.o USBaccess.o -o cleware.so
	./install-lib.pl

install: clewarecontrol $(TRANSLATIONS)
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	cp clewarecontrol $(DESTDIR)$(PREFIX)/bin
	mkdir -p $(DESTDIR)$(PREFIX)/share/man/man1
	cp clewarecontrol.1 $(DESTDIR)$(PREFIX)/share/man/man1/clewarecontrol.1
	gzip -9 $(DESTDIR)$(PREFIX)/share/man/man1/clewarecontrol.1
	mkdir -p $(DESTDIR)/usr/share/locale/nl/LC_MESSAGES
	cp nl.mo $(DESTDIR)/usr/share/locale/nl/LC_MESSAGES/clewarecontrol.mo

uninstall: clean
	rm -f $(DESTDIR)$(PREFIX)/bin/clewarecontrol
	rm -f $(DESTDIR)$(PREFIX)/share/man/man1/clewarecontrol.1

clean:
	rm -rf $(OBJS) clewarecontrol core gmon.out *.da build cleware_wrap.cxx *cleware*.so cleware.py* cleware.pm *.o

package: clean
	# source package
	rm -rf clewarecontrol-$(VERSION)*
	mkdir clewarecontrol-$(VERSION)
	cp -a *.c* *.h *.i *.pl *py readme*.txt clewarecontrol.1 Makefile LICENSE clewarecontrol-$(VERSION)
	tar cf - examples --exclude=.svn  | tar xvf - -C clewarecontrol-$(VERSION)
	tar czf clewarecontrol-$(VERSION).tgz clewarecontrol-$(VERSION)
	rm -rf clewarecontrol-$(VERSION)

stest:
	cppcheck -v --enable=all --inconclusive -I. . 2> err.txt
