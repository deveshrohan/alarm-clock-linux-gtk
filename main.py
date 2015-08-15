#!/usr/bin/python

from gi.repository import Gtk

class mainWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Alarm Clock")
		self.set_border_width(10)
		self.set_default_size(600, 500)
		self.set_resizable(False)

		hb = Gtk.HeaderBar()
		hb.set_show_close_button(True)
		self.set_titlebar(hb);

		head_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=30)
		Gtk.StyleContext.add_class(head_box.get_style_context(), "linked")

		clock_button = Gtk.Button()
		clock_image = Gtk.Image.new_from_file('./res/clock.png')
		clock_button.set_relief(Gtk.ReliefStyle.NONE)
		#clock_button.set_focus_on_click(True)
		clock_button.add(clock_image)
		head_box.add(clock_button)

		alarm_button = Gtk.Button()
		alarm_image = Gtk.Image.new_from_file('./res/alarm.png')
		alarm_button.set_relief(Gtk.ReliefStyle.NONE)
		alarm_button.add(alarm_image)
		head_box.add(alarm_button)

		timer_button = Gtk.Button()
		timer_image = Gtk.Image.new_from_file('./res/timer.png')
		timer_button.set_relief(Gtk.ReliefStyle.NONE)
		timer_button.add(timer_image)
		head_box.add(timer_button)

		settings_button = Gtk.Button()
		settings_image = Gtk.Image.new_from_file('./res/settings.png')
		settings_button.set_relief(Gtk.ReliefStyle.NONE)
		settings_button.add(settings_image)
		head_box.add(settings_button)
		
		hb.pack_start(head_box)

win = mainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
