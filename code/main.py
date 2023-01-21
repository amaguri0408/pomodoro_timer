from tkinter import *
from tkinter import ttk


def main():
    root = Tk()
    root.title('ポモドーロ・テクニックタイマー')

    # ウィジェットの作成
    frame1 = ttk.Frame(root, padding=10)
    label1 = ttk.Label(frame1, text='作業中')
    
    time_main = "10:00.00"
    entry1 = ttk.Label(frame1, text=time_main)
    reset = ttk.Button(
        frame1,
        text='reset',
    )
    start_stop = ttk.Button(
        frame1,
        text='start',
    )

    # レイアウト
    frame1.pack()
    label1.pack(side=TOP)
    entry1.pack(side=TOP)
    reset.pack(side=TOP)
    start_stop.pack(side=LEFT)

    # ウィンドウの表示開始
    root.mainloop()


if __name__ == "__main__":
    main()