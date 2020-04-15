import tkinter as tk
import pygetwindow as gw
import tkinter.font as tkFont
import startClick


class Application:
    def __init__(self, root, start):
        self.root = root
        self.start = start
        self.root.title("AutoOnmyoji")
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws / 2) - (400 / 2)
        y = (hs / 2) - (200 / 2)
        self.root.geometry('%dx%d+%d+%d' % (400, 200, x, y))
        self.root.resizable(False, False)
        face1(self.root, self.start)


class face1:
    def __init__(self, root, start):
        self.root = root
        self.start = start
        self.face1 = tk.Frame(self.root)
        self.face1.pack()
        self.v = tk.IntVar()
        self.v.set(1)
        fm1 = tk.Frame(self.face1)
        fm2 = tk.Frame(self.face1)
        faceLab = tk.Label(self.face1, text='设置队伍角色',font = tk.font.Font(size = 20))
        backBtn = tk.Button(fm2, text='上一步', state='disabled')
        nextBtn = tk.Button(fm2, text='下一步', command=self.next)
        leader = tk.Radiobutton(fm1, text="队长", value=1, variable=self.v)
        teammate = tk.Radiobutton(fm1, text="队员", value=2, variable=self.v)
        faceLab.pack(ipady=20)
        leader.pack(padx=5, pady=10, side='left')
        teammate.pack(padx=5, pady=10, side='left')
        backBtn.pack(padx=5, pady=10, side='left')
        nextBtn.pack(padx=5, pady=10, side='left')
        fm1.pack()
        fm2.pack()

    def next(self):
        self.face1.destroy()
        self.start.setRole(self.v.get())
        face2(self.root, self.start)

    # def testPrint(self):
    #     print(self.v.get())
    #
    # def selcectLeader(self):
    #     print("select leader")
    #     self.v.set(1)
    #
    # def selcectTeammate(self):
    #     print("select teammate")
    #     self.v.set(2)


class face2:
    def __init__(self, root, start):
        self.root = root
        self.start = start
        self.face2 = tk.Frame(self.root, )
        self.face2.pack()
        fm1 = tk.Frame(self.face2)
        faceLab = tk.Label(self.face2, text='设置点击位置',font = tk.font.Font(size = 20))
        backBtn = tk.Button(fm1, text='上一步', command=self.back)
        nextBtn = tk.Button(fm1, text='下一步', command=self.next)
        faceLab.pack(ipady=20)
        backBtn.pack(padx=5, pady=10, side='left')
        nextBtn.pack(padx=5, pady=10, side='left')
        fm1.pack()
        if self.start.role == 1:
            self.locateStart()

    def locateStart(self):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws * 3 / 4) - (150 / 2)
        y = (hs * 3 / 4) - (150 / 2)
        if self.start.role == 1:
            self.start.setX(ws * 3 / 4)
            self.start.setY(hs * 3 / 4)
        else:
            self.start.setX(ws /2)
            self.start.setY(hs /2)
        self.top = tk.Toplevel()
        # top.overrideredirect(True)
        self.top.attributes('-alpha', 0.6)
        self.top.attributes('-topmost', True)
        self.top.title("开始")
        self.top.geometry('%dx%d+%d+%d' % (150, 150, x, y))

    def next(self):
        self.face2.destroy()
        if self.start.role == 1:
            self.top.destroy()
        face3(self.root, self.start)

    def back(self):
        if self.start.role == 1:
            self.top.destroy()
        self.face2.destroy()
        face1(self.root, self.start)


class face3:
    def __init__(self, root, start):
        self.root = root
        self.start = start
        self.face3 = tk.Frame(self.root, )
        self.face3.pack()
        fm1 = tk.Frame(self.face3)
        faceLab = tk.Label(self.face3, text='请输入每轮时间',font = tk.font.Font(size = 20))
        entry = tk.Entry(self.face3)
        backBtn = tk.Button(fm1, text='上一步', command=self.back)
        nextBtn = tk.Button(fm1, text='下一步', state='disabled')
        startBtn = tk.Button(self.face3, text='开始', command=lambda : self.startClick(entry))
        faceLab.pack(ipady=20)
        entry.pack()
        backBtn.pack(padx=5, pady=10, side='left')
        nextBtn.pack(padx=5, pady=10, side='left')
        fm1.pack()
        startBtn.pack()

    def back(self):
        self.face3.destroy()
        face2(self.root, self.start)

    def startClick(self,entry):
        self.start.setTime(int(entry.get()))
        self.start.click()


if __name__ == "__main__":
    root = tk.Tk()
    start = startClick.start()
    test = Application(root, start)
    root.mainloop()
