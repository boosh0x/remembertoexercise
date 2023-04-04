import time
import threading
from playsound import playsound
from PyObjCTools import AppHelper
from Cocoa import NSApplication, NSApp, NSWindow, NSButton, NSTextField, NSObject, NSMakeRect, NSBackingStoreBuffered, NSWindowStyleMaskTitled, NSWindowStyleMaskClosable, NSWindowStyleMaskMiniaturizable, NSDate

class StretchReminderApp(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        styleMask = (
            NSWindowStyleMaskTitled |
            NSWindowStyleMaskClosable |
            NSWindowStyleMaskMiniaturizable
        )
        frame = NSMakeRect(0, 0, 300, 200)
        self.window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            frame,
            styleMask,
            NSBackingStoreBuffered,
            False
        )
        self.window.setTitle_("Reminder to Exercise")
        self.window.center()

        self.timer_text = NSTextField.alloc().initWithFrame_(NSMakeRect(100, 140, 100, 24))
        self.timer_text.setStringValue_("01:00:00")
        self.window.contentView().addSubview_(self.timer_text)

        self.start_button = NSButton.alloc().initWithFrame_(NSMakeRect(40, 60, 80, 32))
        self.start_button.setTitle_("Start")
        self.start_button.setTarget_(self)
        self.start_button.setAction_("start:")
        self.window.contentView().addSubview_(self.start_button)

        self.pause_button = NSButton.alloc().initWithFrame_(NSMakeRect(140, 60, 80, 32))
        self.pause_button.setTitle_("Pause")
        self.pause_button.setTarget_(self)
        self.pause_button.setAction_("pause:")
        self.window.contentView().addSubview_(self.pause_button)

        self.reset_button = NSButton.alloc().initWithFrame_(NSMakeRect(40, 20, 80, 32))
        self.reset_button.setTitle_("Reset")
        self.reset_button.setTarget_(self)
        self.reset_button.setAction_("reset:")
        self.window.contentView().addSubview_(self.reset_button)

        self.quit_button = NSButton.alloc().initWithFrame_(NSMakeRect(140, 20, 80, 32))
        self.quit_button.setTitle_("Quit")
        self.quit_button.setTarget_(self)
        self.quit_button.setAction_("quit:")
        self.window.contentView().addSubview_(self.quit_button)

        self.window.orderFrontRegardless()
        self.timer = None

    def start_(self, sender):
        if self.timer is None or not self.timer.is_alive():
            self.timer = threading.Thread(target=self.countdown)
            self.timer.start()

    def pause_(self, sender):
        if self.timer is not None:
            self.timer_active = False
            self.timer.join()
            self.timer = None

    def reset_(self, sender):
        self.pause_(None)
        self.timer_text.setStringValue_("01:00:00")

    def quit_(self, sender):
        self.pause_(None)
        NSApp.terminate_(self)

    def countdown(self):
        self.timer_active = True
        total_seconds = 3600  # Change this value to a few seconds for testing
        while total_seconds > 0 and self.timer_active:
            minutes, seconds = divmod(total_seconds, 60)
            hours, minutes = divmod(minutes, 60)
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timer_text.performSelectorOnMainThread_withObject_waitUntilDone_("setStringValue:", time_str, True)
            time.sleep(1)
            total_seconds -= 1

        if self.timer_active:
            playsound("./exercise.mp3")


def main():
    app = NSApplication.sharedApplication()
    delegate = StretchReminderApp.alloc().init()
    app.setDelegate_(delegate)
    AppHelper.runEventLoop()

if __name__ == "__main__":
    main()
