import tkinter as tk
import pandas as pd
import os

class window:
    def __init__(self):
        window_width = 500
        window_height = 200
        self.window_size = f"{window_width}x{window_height}"
        self.max_schedule_index = len(os.listdir("./files/Schedules/"))

        self.root = tk.Tk()
        self.root.withdraw()
        self.main_window()

    def main_window(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Welcome!")
        self.root.geometry(self.window_size)
        self.root.resizable(False, False)

        button1 = tk.Button(self.root, text="Schedules", command=self.schedules_window)
        button1.pack(pady=20,padx=20)

        button2 = tk.Button(self.root, text="Press Me", command=self.test_button)
        button2.pack(pady=20,padx=20)

        self.root.mainloop()

    def schedules_window(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Schedules")
        self.root.geometry(self.window_size)
        self.root.resizable(False, False)
        
        grd = tk.Frame(self.root)
        grd.grid(row=0, column=0)

        close_btn = tk.Button(self.root, text="Menu", command=self.main_window)
        close_btn.grid(row=0, column=1)

        new_schedule = tk.Button(self.root, text="New", command=self.new_schedule)
        new_schedule.grid(row=0, column=2)

        last_schedule = tk.Button(self.root, text="<", command=self.test_button)
        last_schedule.grid(row=0, column=6)

        next_schedule = tk.Button(self.root, text=">", command=self.test_button)
        next_schedule.grid(row=0, column=7)

        self.show_schedule()

    def new_schedule(self):
        empty = [["None"]*7]*3
        df = pd.DataFrame(empty, columns=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
        pd.DataFrame.to_csv(df, f"./files/Schedules/schedule{self.max_schedule_index}.csv")
        self.max_schedule_index += 1
        self.show_schedule(self.max_schedule_index)

    def show_schedule(self, i=-2):
        if i == -2:
            i = self.max_schedule_index
        elif i < 0:
            i = 0
        elif i >= self.max_schedule_index:
            i = self.max_schedule_index
        i -= 1

        df = pd.read_csv(f"./files/Schedules/schedule{i}.csv")
        for col in range(1,8):
            tk.Label(self.root, text=df.columns[col]).grid(row=1, column=col)
        for row in range(len(df)):
            for col in range(1,8):
                tk.Label(self.root, text=df.iat[row,col]).grid(row=row+2, column=col)

    def test_button(self):
        print("pressed")




if __name__ == "__main__":
    window()