import tkinter as tk
from tkinter import filedialog
from playsound import playsound
import threading
import time

class StretchReminderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stretch Reminder")
        self.geometry("300x200")

        self.audio_file = None
        self.timer_thread = None
        self.running = False

        self.time_left = tk.StringVar()
        self.time_left.set("01:00:00")

        self.label = tk.Label(self, textvariable=self.time_left, font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.start_button = tk.Button(self, text="Start", command=self.start)
        self.start_button.pack(fill="x")

        self.pause_button = tk.Button(self, text="Pause", command=self.pause)
        self.pause_button.pack(fill="x")

        self.reset_button = tk.Button(self, text="Reset", command=self.reset)
        self.reset_button.pack(fill="x")

        self.quit_button = tk.Button(self, text="Quit", command=self.quit_app)
        self.quit_button.pack(fill="x")

        self.open_audio_button = tk.Button(self, text="Select audio file", command=self.open_audio)
        self.open_audio_button.pack(fill="x")

    def countdown(self):
        while self.running:
            time.sleep(1)
            h, m, s = map(int, self.time_left.get().split(':'))
            total_seconds = h * 3600 + m * 60 + s
            total_seconds -= 1

            if total_seconds <= 0:
                self.running = False
                self.play_audio()
                break

            h, m, s = total_seconds // 3600, (total_seconds // 60) % 60, total_seconds % 60
            self.time_left.set(f"{h:02d}:{m:02d}:{s:02d}")

    def start(self):
        if not self.running:
            self.running = True
            self.timer_thread = threading.Thread(target=self.countdown)
            self.timer_thread.start()

    def pause(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time_left.set("01:00:00")

    def quit_app(self):
        self.running = False
        self.destroy()

    def open_audio(self):
        self.audio_file = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("Audio Files", "*.mp3"), ("All Files", "*.*")])

    def play_audio(self):
        if self.audio_file:
            playsound(self.audio_file)

if __name__ == "__main__":
    app = StretchReminderApp()
    app.mainloop()
