import tkinter as tk
from tkinter import ttk


class PomodoroTimer:
    def __init__(self):
        self.main_time = 25 * 60 + 0
        self.phase_list = ["作業中", "休憩中"]
        self.make_main_window()

    def convert_time2str(self, t):
        s = t % 60
        t //= 60
        m = t % 60
        t //= 60
        h = t
        res = ""
        if h:
            res += str(h).zfill(2)
            res += ":"
        res += f"{str(m).zfill(2)}:{str(s).zfill(2)}"
        return res

    def btn_reset(self):
        pass

    def btn_start_stop(self):
        pass
    
    def make_main_window(self):
        self.main_window = dict()
        self.main_window["root"] = tk.Tk()
        self.main_window["root"].title('ポモドーロ・テクニックタイマー')
        # self.main_window["root"].configure(bg="white")

        # ウィジェットの作成
        self.main_window["frame1"] = tk.Frame(self.main_window["root"], padx=10, pady=10)
        self.main_window["phase"] = tk.Label(
            self.main_window["frame1"], 
            font=("MSゴシック", 10),
            text=self.phase_list[0]
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
            command=self.btn_reset(),
        )
        self.main_window["start_stop"] = tk.Button(
            self.main_window["btn_frame"],
            text='Start',
            width=4,
            font=("MSゴシック", 9),
            command=self.btn_start_stop(),
        )

        # レイアウト
        self.main_window["frame1"].pack()
        self.main_window["phase"].pack(side="top")
        self.main_window["timer"].pack(side="top")
        self.main_window["btn_frame"].pack(side="top")
        self.main_window["reset"].pack(side="left", padx=3)
        self.main_window["start_stop"].pack(side="left", padx=3)

        # ウィンドウの表示開始
        self.main_window["root"].mainloop()



def main():
    PomodoroTimer()


if __name__ == "__main__":
    main()