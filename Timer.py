import tkinter as tk
from time import time
from PIL import Image, ImageTk
import requests
from io import BytesIO

class TimerApp:
    def __init__(self, master):
        self.master = master
        master.title("Lunar Client Timer")
        self.set_window_icon("https://img.icons8.com/?size=512&id=4nNEosqU3iXQ&format=png")
        
        self.bg_color = "#1e1e1e"
        self.text_color = "#ffffff" 
        self.button_bg = "#333333" 
        self.button_fg = "#ffffff"
        self.footer_text_color = "#d3d3d3"

        master.config(bg=self.bg_color)

        self.font_large = ("Arial", 16)
        self.font_medium = ("Arial", 12)
        self.font_small = ("Arial", 10)

        self.timer1 = self.timer2 = self.timer3 = 0
        self.running1 = self.running2 = self.running3 = False
        self.start_time1 = self.start_time2 = self.start_time3 = 0

        self.frame = tk.Frame(master, bg=self.bg_color)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.timer_label1 = tk.Label(self.frame, text="Recording: 00:00:00.0", font=self.font_large, bg=self.bg_color, fg=self.text_color)
        self.timer_label1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.start_button1 = tk.Button(self.frame, text="Start", font=self.font_medium, command=self.start_timer1, bg=self.button_bg, fg=self.button_fg)
        self.start_button1.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.pause_button1 = tk.Button(self.frame, text="Pause", font=self.font_medium, command=self.pause_timer1, bg=self.button_bg, fg=self.button_fg)
        self.pause_button1.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        self.timer_label2 = tk.Label(self.frame, text="Editing: 00:00:00.0", font=self.font_large, bg=self.bg_color, fg=self.text_color)
        self.timer_label2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.start_button2 = tk.Button(self.frame, text="Start ", font=self.font_medium, command=self.start_timer2, bg=self.button_bg, fg=self.button_fg)
        self.start_button2.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.pause_button2 = tk.Button(self.frame, text="Pause", font=self.font_medium, command=self.pause_timer2, bg=self.button_bg, fg=self.button_fg)
        self.pause_button2.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

        self.timer_label3 = tk.Label(self.frame, text="Rendering: 00:00:00.0", font=self.font_large, bg=self.bg_color, fg=self.text_color)
        self.timer_label3.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.start_button3 = tk.Button(self.frame, text="Start", font=self.font_medium, command=self.start_timer3, bg=self.button_bg, fg=self.button_fg)
        self.start_button3.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.pause_button3 = tk.Button(self.frame, text="Pause", font=self.font_medium, command=self.pause_timer3, bg=self.button_bg, fg=self.button_fg)
        self.pause_button3.grid(row=2, column=2, padx=5, pady=5, sticky="ew")

        self.total_time_label = tk.Label(self.frame, text="Total Time: 00:00:00.0", font=self.font_large, bg=self.bg_color, fg=self.text_color)
        self.total_time_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.stop_button = tk.Button(master, text="Calculate", font=self.font_medium, command=self.stop_all, bg="#5bc0de", fg=self.text_color)
        self.stop_button.pack(side=tk.RIGHT, padx=10, pady=10, anchor="se")

        self.reset_button = tk.Button(master, text="Reset", font=self.font_medium, command=self.reset_all, bg="#d9534f", fg=self.text_color)
        self.reset_button.pack(side=tk.RIGHT, padx=10, pady=10, anchor="se")

        self.footer_label = tk.Label(master, text="Created by Venxm", font=self.font_small, bg=self.bg_color, fg=self.footer_text_color)
        self.footer_label.pack(side=tk.LEFT, padx=10, pady=10, anchor="sw")

        self.frame.grid_rowconfigure(3, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)

        self.update_timer()

    def set_window_icon(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            self.icon_photo = ImageTk.PhotoImage(img)
            self.master.iconphoto(True, self.icon_photo)
        except Exception as e:
            raise ValueError(f"Failed to set window icon: {e}")

    def format_time(self, seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds - int(seconds)) * 10)
        return f"{hours:02}:{minutes:02}:{secs:02}.{millis}"

    def start_timer1(self):
        if not self.running1:
            self.start_time1 = time() - self.timer1
            self.running1 = True

    def pause_timer1(self):
        if self.running1:
            self.timer1 = time() - self.start_time1
            self.running1 = False

    def start_timer2(self):
        if not self.running2:
            self.start_time2 = time() - self.timer2
            self.running2 = True

    def pause_timer2(self):
        if self.running2:
            self.timer2 = time() - self.start_time2
            self.running2 = False

    def start_timer3(self):
        if not self.running3:
            self.start_time3 = time() - self.timer3
            self.running3 = True

    def pause_timer3(self):
        if self.running3:
            self.timer3 = time() - self.start_time3
            self.running3 = False

    def stop_all(self):
        if self.running1:
            self.pause_timer1()
        if self.running2:
            self.pause_timer2()
        if self.running3:
            self.pause_timer3()

        total_time = self.timer1 + self.timer2 + self.timer3
        self.total_time_label.config(text=f"Total Time: {self.format_time(total_time)}")

    def reset_all(self):
        self.stop_all()
        self.timer1 = self.timer2 = self.timer3 = 0
        self.running1 = self.running2 = self.running3 = False
        self.start_time1 = self.start_time2 = self.start_time3 = 0
        self.timer_label1.config(text="Recording: 00:00:00.0")
        self.timer_label2.config(text="Editing: 00:00:00.0")
        self.timer_label3.config(text="Rendering: 00:00:00.0")
        self.total_time_label.config(text="Total Time: 00:00:00.0")

    def update_timer(self):
        current_time = time()

        if self.running1:
            elapsed_time1 = current_time - self.start_time1
            self.timer_label1.config(text=f"Recording: {self.format_time(elapsed_time1)}")
        else:
            self.timer_label1.config(text=f"Recording: {self.format_time(self.timer1)}")

        if self.running2:
            elapsed_time2 = current_time - self.start_time2
            self.timer_label2.config(text=f"Editing: {self.format_time(elapsed_time2)}")
        else:
            self.timer_label2.config(text=f"Editing: {self.format_time(self.timer2)}")

        if self.running3:
            elapsed_time3 = current_time - self.start_time3
            self.timer_label3.config(text=f"Rendering: {self.format_time(elapsed_time3)}")
        else:
            self.timer_label3.config(text=f"Rendering: {self.format_time(self.timer3)}")

        self.master.after(50, self.update_timer)

root = tk.Tk()
root.geometry("525x250")
app = TimerApp(root)
root.mainloop()