#!/usr/bin/python

import clock
from gi.repository import Gtk, GdkPixbuf, Gdk, GLib
import threading
import time


class MainWindow(Gtk.Window):

    def clock_button_pressed(self, eventbox, event):
            print("Event: %s" % event)

    def alarm_button_pressed(self, eventbox, event):
            print("Event: %s" % event)

    def timer_button_pressed(self, eventbox, event):
            print("Event: %s" % event)

    def settings_button_pressed(self, eventbox, event):
            print("Event: %s" % event)

    def __init__(self):
        Gtk.Window.__init__(self, title="Alarm Clock")
        self.set_default_size(600, 500)
        self.set_border_width(10)
        self.set_resizable(False)
        self.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0.19, 0.24, 0.55, 0.9))

        main_grid = Gtk.Grid()
#        main_grid.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0.19, 0.24, 0.55, 0.7))
        main_grid.set_row_spacing(150)
        self.add(main_grid)

        head_grid = Gtk.Grid()
        head_grid.set_column_spacing(100)

#        clock_button = Gtk.Button()
        clock_image = Gtk.Image()
        clock_image.set_from_pixbuf(GdkPixbuf.Pixbuf.new_from_file_at_size('./res/clock.png', 32, 32))
        clock_event_box = Gtk.EventBox()
        clock_event_box.add(clock_image)
        clock_event_box.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0.15, 0.24, 0.45, 0.7))
        clock_event_box.connect("button-press-event", self.clock_button_pressed)
#        clock_button.set_relief(Gtk.ReliefStyle.NONE)
#        clock_button.set_focus_on_click(True)
#        clock_button.set_image(clock_image)
        head_grid.attach(clock_event_box, 2, 1, 2, 2)


#        alarm_button = Gtk.Button()
        alarm_image = Gtk.Image()
        alarm_image.set_from_pixbuf(GdkPixbuf.Pixbuf.new_from_file_at_size('./res/alarm.png', 32, 32))
        alarm_event_box = Gtk.EventBox()
        alarm_event_box.add(alarm_image)
        alarm_event_box.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0.15, 0.24, 0.45, 0.7))
        alarm_event_box.connect("button-press-event", self.alarm_button_pressed)
#        alarm_button.set_relief(Gtk.ReliefStyle.NONE)
#       alarm_button.set_image(alarm_image)
        head_grid.attach_next_to(alarm_event_box, clock_event_box, Gtk.PositionType.RIGHT, 2, 2)

#        timer_button = Gtk.Button()
        timer_image = Gtk.Image()
        timer_image.set_from_pixbuf(GdkPixbuf.Pixbuf.new_from_file_at_size('./res/timer.png', 32, 32))
        timer_event_box = Gtk.EventBox()
        timer_event_box.add(timer_image)
        timer_event_box.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0.15, 0.24, 0.45, 0.7))
        timer_event_box.connect("button-press-event", self.timer_button_pressed)
#        timer_button.set_relief(Gtk.ReliefStyle.NONE)
#       timer_button.set_image(timer_image)
        head_grid.attach_next_to(timer_event_box, alarm_event_box, Gtk.PositionType.RIGHT, 2, 2)

#        settings_button = Gtk.Button()
        settings_image = Gtk.Image()
        settings_image.set_from_pixbuf(GdkPixbuf.Pixbuf.new_from_file_at_size('./res/settings.png', 32, 32))
        settings_event_box = Gtk.EventBox()
        settings_event_box.add(settings_image)
        settings_event_box.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0.15, 0.24, 0.45, 0.7))
        settings_event_box.connect("button-press-event", self.settings_button_pressed)
#        settings_button.set_relief(Gtk.ReliefStyle.NONE)
#        settings_button.set_image(settings_image)
        head_grid.attach_next_to(settings_event_box, timer_event_box, Gtk.PositionType.RIGHT, 2, 2)

        main_grid.add(head_grid)

        body_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        main_grid.attach_next_to(body_box, head_grid, Gtk.PositionType.BOTTOM, 3, 3)

#       stack = Gtk.Stack()
#       stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
#       stack.set_transition_duration(1000)
        self.clock_show = Gtk.Label()
        body_box.add(self.clock_show)

        def set_time(current_time):
            self.clock_show.set_markup('<span font = "80" foreground = "#FFFFFF">' + current_time + '</span>')

        def update_time():
            while True:
                current_time = clock.Clock().__get_time__()
                GLib.idle_add(set_time, current_time)
                time.sleep(0.01)

        clock_set_thread = threading.Thread(target=update_time)
        clock_set_thread.daemon = True
        clock_set_thread.start()


win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
