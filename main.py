#!/usr/bin/python

import clock
from gi.repository import Gtk, GdkPixbuf, Gdk, GLib
import threading
import time


class MainWindow(Gtk.Window):
    main_grid = Gtk.Grid()
    head_grid = Gtk.Grid()
    body_grid = Gtk.Grid()

    footer_clock = Gtk.Grid()
    footer_alarm = Gtk.Grid()
    footer_timer = Gtk.Grid()
    footer_settings = Gtk.Grid()

    def __init__(self):

        def fill_footer(widget):
            widget.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse("white"))

        def empty_footer(widget):
            widget.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0, 0, 0, 0))

        def clock_button_enter(eventbox, event):
            fill_footer(self.footer_clock)

        def clock_button_exit(eventbox, event):
            empty_footer(self.footer_clock)

        def alarm_button_enter(eventbox, event):
            fill_footer(self.footer_alarm)

        def alarm_button_exit(eventbox, event):
            empty_footer(self.footer_alarm)

        def timer_button_enter(eventbox, event):
            fill_footer(self.footer_timer)

        def timer_button_exit(eventbox, event):
            empty_footer(self.footer_timer)

        def settings_button_enter(eventbox, event):
            fill_footer(self.footer_settings)

        def settings_button_exit(eventbox, event):
            empty_footer(self.footer_settings)

        Gtk.Window.__init__(self, title="Alarm Clock")
        self.set_default_size(600, 500)
        self.set_border_width(10)
        self.set_resizable(False)
        self.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0.19, 0.24, 0.55, 0.9))

        self.main_grid.set_row_spacing(150)
        self.add(self.main_grid)

        self.head_grid.set_column_spacing(100)
        self.head_grid.set_row_spacing(5)

        clock_image = Gtk.Image()
        clock_image.set_from_pixbuf(GdkPixbuf.Pixbuf.new_from_file_at_size('./res/clock.png', 32, 32))
        clock_event_box = Gtk.EventBox()
        clock_event_box.add(clock_image)
        clock_event_box.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0, 0, 0, 0))
        clock_event_box.connect("enter-notify-event", clock_button_enter)
        clock_event_box.connect("leave-notify-event", clock_button_exit)
        self.head_grid.attach(clock_event_box, 2, 1, 2, 2)
        self.head_grid.attach_next_to(self.footer_clock, clock_event_box, Gtk.PositionType.BOTTOM, 2, 2)

        alarm_image = Gtk.Image()
        alarm_image.set_from_pixbuf(GdkPixbuf.Pixbuf.new_from_file_at_size('./res/alarm.png', 32, 32))
        alarm_event_box = Gtk.EventBox()
        alarm_event_box.add(alarm_image)
        alarm_event_box.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0, 0, 0, 0))
        alarm_event_box.connect("enter-notify-event", alarm_button_enter)
        alarm_event_box.connect("leave-notify-event", alarm_button_exit)
        self.head_grid.attach_next_to(alarm_event_box, clock_event_box, Gtk.PositionType.RIGHT, 2, 2)
        self.head_grid.attach_next_to(self.footer_alarm, alarm_event_box, Gtk.PositionType.BOTTOM, 2, 2)

        timer_image = Gtk.Image()
        timer_image.set_from_pixbuf(GdkPixbuf.Pixbuf.new_from_file_at_size('./res/timer.png', 32, 32))
        timer_event_box = Gtk.EventBox()
        timer_event_box.add(timer_image)
        timer_event_box.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0, 0, 0, 0))
        timer_event_box.connect("enter-notify-event", timer_button_enter)
        timer_event_box.connect("leave-notify-event", timer_button_exit)
        self.head_grid.attach_next_to(timer_event_box, alarm_event_box, Gtk.PositionType.RIGHT, 2, 2)
        self.head_grid.attach_next_to(self.footer_timer, timer_event_box, Gtk.PositionType.BOTTOM, 2, 2)

        settings_image = Gtk.Image()
        settings_image.set_from_pixbuf(GdkPixbuf.Pixbuf.new_from_file_at_size('./res/settings.png', 32, 32))
        settings_event_box = Gtk.EventBox()
        settings_event_box.add(settings_image)
        settings_event_box.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(0, 0, 0, 0))
        settings_event_box.connect("enter-notify-event", settings_button_enter)
        settings_event_box.connect("leave-notify-event", settings_button_exit)
        self.head_grid.attach_next_to(settings_event_box, timer_event_box, Gtk.PositionType.RIGHT, 2, 2)
        self.head_grid.attach_next_to(self.footer_settings, settings_event_box, Gtk.PositionType.BOTTOM, 2, 2)

        self.main_grid.add(self.head_grid)
        self.body_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.main_grid.attach_next_to(self.body_box, self.head_grid, Gtk.PositionType.BOTTOM, 3, 3)

        self.clock_show = Gtk.Label()
        self.body_box.add(self.clock_show)

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
