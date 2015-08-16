#!/usr/bin/python

import clock
from gi.repository import Gtk, GdkPixbuf, Gdk

class mainWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Alarm Clock")
		self.set_default_size(600, 500)
	#	self.set_resizable(False)

		main_grid = Gtk.Grid()
                main_grid.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0.19, 0.24, 0.55, 0.7))
		self.add(main_grid)
		
		head_grid = Gtk.Grid()
		head_grid.set_column_spacing(80)

		clock_button = Gtk.Button()
                clock_image = Gtk.Image()
		clock_image.set_from_pixbuf(GdkPixbuf.Pixbuf.new_from_file_at_size('./res/clock.png', 32, 32))
		clock_button.set_relief(Gtk.ReliefStyle.NONE)
		#clock_button.set_focus_on_click(True)
		clock_button.set_image(clock_image)
		head_grid.attach(clock_button, 2, 1, 2, 2)

		alarm_button = Gtk.Button()
                alarm_image = Gtk.Image()
		alarm_image.set_from_pixbuf(GdkPixbuf.Pixbuf.new_from_file_at_size('./res/alarm.png', 32, 32))
		alarm_button.set_relief(Gtk.ReliefStyle.NONE)
		alarm_button.set_image(alarm_image)
		head_grid.attach_next_to(alarm_button, clock_button, Gtk.PositionType.RIGHT,2, 2)

		timer_button = Gtk.Button()
                timer_image = Gtk.Image()
		timer_image.set_from_pixbuf(GdkPixbuf.Pixbuf.new_from_file_at_size('./res/timer.png', 32, 32))
		timer_button.set_relief(Gtk.ReliefStyle.NONE)
		timer_button.set_image(timer_image)
		head_grid.attach_next_to(timer_button, alarm_button, Gtk.PositionType.RIGHT,2, 2)

		settings_button = Gtk.Button()
                settings_image = Gtk.Image()
		settings_image.set_from_pixbuf(GdkPixbuf.Pixbuf.new_from_file_at_size('./res/settings.png', 32, 32))
		settings_button.set_relief(Gtk.ReliefStyle.NONE)
		settings_button.set_image(settings_image)
		head_grid.attach_next_to(settings_button, timer_button, Gtk.PositionType.RIGHT,2, 2)
		
		main_grid.add(head_grid)

		body_grid = Gtk.Grid()
        	main_grid.attach_next_to(body_grid, head_grid, Gtk.PositionType.BOTTOM, 3, 3)
		
#		stack = Gtk.Stack()
#       	stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
#	        stack.set_transition_duration(1000)
		
                self.clock_show = Gtk.Label()
                body_grid.attach(self.clock_show, 5, 3, 5, 5)
		

win = mainWindow()
#while True:
curr_time = clock.clock().__get_time__()
win.clock_show.set_markup('<span font = "80" foreground = "#FFFFFF">' + curr_time + '</span>')

win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
