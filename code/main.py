import time
import threading
import tkinter as tk
from tkinter import ttk
from pathlib import Path

try:
    import pygame
    pygame_available = True
except ModuleNotFoundError:
    pygame_available = False    

pygame.init()

class PomodoroTimer:
    def __init__(self):
        self.running = True
        self.time_list = [5, 3]
        self.phase = 0
        self.main_time = self.time_list[self.phase]
        self.audio_dir = Path("audio")
        self.audio_list = ["鳩時計2.mp3", "目覚まし時計のアラーム.mp3"]
        self.timer_flag = False
        self.phase_list = ["作業中", "休憩中"]
        thread_timer = threading.Thread(target=self.timer_loop)
        thread_timer.start()
        self.make_main_window()
        thread_timer.join()

    def convert_time2str(self, t):
        t += 0.99
        s = int(t % 60)
        t //= 60
        m = int(t % 60)
        t //= 60
        h = int(t)
        res = ""
        if h:
            res += str(h).zfill(2)
            res += ":"
        res += f"{str(m).zfill(2)}:{str(s).zfill(2)}"
        return res

    def next_phase(self):
        if pygame_available:
            pygame.mixer.init()
            pygame.mixer.music.load(self.audio_dir / self.audio_list[self.phase])
            pygame.mixer.music.play()
        self.phase = (self.phase + 1) % len(self.phase_list)
        self.main_time = self.time_list[self.phase]
        self.main_window["phase"].configure(text=self.phase_list[self.phase])
        self.main_window["timer"].configure(text=self.convert_time2str(self.main_time))

    def timer_loop(self):
        while self.running:
            if not self.timer_flag: continue
            self.main_time -= 0.1
            if self.main_time <= 0:
                self.next_phase()
            self.main_window["timer"].configure(text=self.convert_time2str(self.main_time))
            time.sleep(0.1)

    def btn_reset(self):
        self.phase = 0
        self.main_time = self.time_list[self.phase]
        self.timer_flag = False
        self.main_window["start_stop"].configure(text="Start")
        self.main_window["phase"].configure(text=self.phase_list[self.phase])
        self.main_window["timer"].configure(text=self.convert_time2str(self.main_time))

    def btn_start_stop(self):
        if self.timer_flag:
            self.timer_flag = False
            self.main_window["start_stop"].configure(text="Start")
        else:
            self.timer_flag = True
            self.main_window["start_stop"].configure(text="Stop")

    def on_move_press(self, event):
        self.mouse_x = event.x_root - self.main_window["root"].winfo_x()
        self.mouse_y = event.y_root - self.main_window["root"].winfo_y()

    def on_move_motion(self, event):
        self.main_window["root"].geometry(f"+{event.x_root - self.mouse_x}+{event.y_root - self.mouse_y}")
    
    def make_main_window(self):
        self.main_window = dict()
        self.main_window["root"] = tk.Tk()
        self.main_window["root"].title('ポモドーロ・テクニックタイマー')
        self.main_window["root"].attributes("-topmost", True)

        # windowの内部でドラッグ可能に
        self.main_window["root"].bind("<Button-1>", self.on_move_press)
        self.main_window["root"].bind("<B1-Motion>", self.on_move_motion)

        # ウィジェットの作成
        self.main_window["frame1"] = tk.Frame(self.main_window["root"], padx=10, pady=10)
        self.main_window["phase"] = tk.Label(
            self.main_window["frame1"], 
            font=("MSゴシック", 10),
            text=self.phase_list[self.phase]
        )
        
        # タイマー
        self.main_window["timer"] = tk.Label(
            self.main_window["frame1"], 
            text=self.convert_time2str(self.main_time),
            font=("MSゴシック", "20", "bold"),
        )

        # ボタン配置フレーム
        self.main_window["btn_frame"] = tk.Frame(self.main_window["frame1"])
        # ボタン
        self.main_window["reset"] = tk.Button(
            self.main_window["btn_frame"],
            text='Reset',
            width=4,
            font=("MSゴシック", 9),
            command=self.btn_reset,
        )
        self.main_window["start_stop"] = tk.Button(
            self.main_window["btn_frame"],
            text='Start',
            width=4,
            font=("MSゴシック", 9),
            command=self.btn_start_stop,
        )

        # レイアウト
        self.main_window["frame1"].pack()
        self.main_window["phase"].pack(side="top")
        self.main_window["timer"].pack(side="top")
        self.main_window["btn_frame"].pack(side="top")
        self.main_window["reset"].pack(side="left", padx=3)
        self.main_window["start_stop"].pack(side="left", padx=3)

        # windowの最低サイズ変更
        self.main_window["root"].update()
        width = self.main_window["root"].winfo_width()
        height = self.main_window["root"].winfo_height()
        self.main_window["root"].minsize(width=width, height=height)

        # ウィンドウの表示開始
        self.main_window["root"].mainloop()
        self.running = False


def main():
    PomodoroTimer()


if __name__ == "__main__":
    main()