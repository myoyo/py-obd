#!/usr/bin/python
import pygtk
pygtk.require("2.0")
import gtk

class HelloWorld:
	def __init__(self):
		interface = gtk.Builder()
		interface.add_from_file('design.glade')
		self.Panel = interface.get_object("Panel1")
		self.Panel.fullscreen()
		
		self.myLabel = interface.get_object("HMessage")
		interface.connect_signals(self)

	def on_mainWindow_destroy(self, widget):
		gtk.main_quit()

	def on_myButton_clicked(self, widget):
		self.myLabel.set_text("Yooo World!")

if __name__ == "__main__":
	HelloWorld()
	gtk.main()
