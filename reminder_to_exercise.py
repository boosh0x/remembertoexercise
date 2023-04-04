import threading
import time
from playsound import playsound
from PyObjCTools import AppHelper
from AppKit import NSApp, NSApplication, NSWindow, NSButton, NSTextField, NSColor, NSTextAlignment, NSFont, NSFontManager, NSFontPanel

class ReminderApp(NSApplication):

    def finishLaunching(self):
        self.main_window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            ((300, 300), (320, 200)),
            15, 2, 0
        )
        self.main_window.setBackgroundColor_(NSColor.lightGrayColor())

        self.timer_label = NSTextField.alloc().initWithFrame_(((20, 150), (280, 40)))
        self.timer_label.setEditable_(False)
        self.timer_label.setBordered_(False)
        self.timer_label.setBackgroundColor_(NSColor.lightGrayColor())
        self.timer_label.setFont_(NSFont.boldSystemFontOfSize_(36))
        self.timer_label.setAlignment_(2)  # 2 corresponds to NSTextAlignmentCenter
        self.main_window.contentView().addSubview_(self.timer_label)

        button_start = NSButton.alloc().initWithFrame_(((20, 100), (60, 40)))
        button_start.setTitle_("Start")
        button_start.setFont_(NSFont.systemFontOfSize_(14))
        button_start.setTarget_(self)
        button_start.setAction_("start:")
        self.main_window.contentView().addSubview_(button_start)

        button_pause = NSButton.alloc().initWithFrame_(((90, 100), (60, 40)))
        button_pause.setTitle_("Pause")
        button_pause.setFont_(NSFont.systemFontOfSize_(14))
        button_pause.setTarget_(self)
        button_pause.setAction_("pause:")
        self.main_window.contentView().addSubview_(button_pause)

        button_reset = NSButton.alloc().initWithFrame_(((160, 100), (60, 40)))
        button_reset.setTitle_("Reset")
        button_reset.setFont_(NSFont.systemFontOfSize_(14))
        button_reset.setTarget_(self)
        button_reset.setAction_("reset:")
        self.main_window.contentView().addSubview_(button_reset)

        button_quit = NSButton.alloc().initWithFrame_(((230, 100), (60, 40)))
        button_quit.setTitle_("Quit")
        button_quit.setFont_(NSFont.systemFontOfSize_(14))
        button_quit.setTarget_(self)
        button_quit.setAction_("terminate:")
        self.main_window.contentView().addSubview_(button_quit)

        self.timer_seconds = 10
        self.update_timer()
        self.timer_event = threading.Event()

        self.main_window.makeKeyAndOrderFront_(None)
        self.main_window.setTitle_("Reminder to Exercise")
        self.activateIgnoringOtherApps_(True)

        self.timer_thread = None


    def update_timer(self):
        minutes, seconds = divmod(self.timer_seconds, 60)
        self.timer_label.setStringValue_("{:02d}:{:02d}".format(minutes, seconds))

    def timer_loop(self):
        while not self.timer_event.is_set() and self.timer_seconds > 0:
            time.sleep(1)
            self.timer_seconds -= 1
            self.performSelectorOnMainThread_withObject_waitUntilDone_(self.update_timer, None, False)
        if not self.timer_event.is_set():
            playsound("./exercise.mp3")

    def start_(self, sender):
        if self.timer_thread and self.timer_thread.is_alive():
            return
        self.timer_event.clear()
        self.timer_thread = threading.Thread(target=self.timer_loop)
        self.timer_thread.start()

    def pause_(self, sender):
        if self.timer_thread.is_alive():
            self.timer_event.set()
            self.timer_thread.join()

    def reset_(self, sender):
        self.pause_(sender)
        self.timer_seconds = 10
        self.update_timer()

if __name__ == "__main__":
    app = ReminderApp.sharedApplication()
    app.setDelegate_(app)
    AppHelper.runEventLoop()

