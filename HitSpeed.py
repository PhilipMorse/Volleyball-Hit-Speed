import tkinter as tk


class Loadout:
    def __init__(self, image_file, button_choice, x_value, y_value):
        self.image_file = image_file
        self.button_choice = button_choice
        self.x_value = x_value
        self.y_value = y_value


class Picker:
    def __init__(self, master, loadout):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.loadout = loadout

        self.canvas = tk.Canvas(master=self.master, width=500, height=500)

        self.image_file = tk.PhotoImage(file=self.loadout.image_file)
        self.image_file = self.image_file.subsample(2, 2)
        self.canvas.create_image(0, 0, image=self.image_file, anchor=tk.NW, tags=['court'])

        self.ball = tk.PhotoImage(file="ball")
        self.ball = self.ball.subsample(2, 2)


        self.canvas.pack()


if __name__ == '__main__':
    root = tk.Tk()
    loadout1 = Loadout("Court1.png", 1, 1, 1)
    app = Picker(root, loadout1)
    root.mainloop()
