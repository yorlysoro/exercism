from tkinter import *
from PIL import Image, ImageTk


class TkInterEX:
    @staticmethod
    def quit_app(event=None):
        root.quit()

    def on_fav_food_select(self, event=None):
        lb_widget = event.widget
        index = int(lb_widget.curselection()[0])
        value = lb_widget.get(index)
        self.fav_food_label['text'] = "I'll get you " + value

    def __init__(self, root):
        root.title("Toolbar Example")
        menubar = Menu(root)
        file_menu = Menu(root, tearoff=0)
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Exit", command=self.quit_app)

        menubar.add_cascade(label="File", menu=file_menu)
        toolbar = Frame(root, bd=1, relief=RAISED)
        open_img = Image.open("open.png")
        save_img = Image.open("save.png")
        exit_img = Image.open("exit.png")

        open_img = ImageTk.PhotoImage(open_img)
        save_img = ImageTk.PhotoImage(save_img)
        exit_img = ImageTk.PhotoImage(exit_img)

        open_button = Button(toolbar, image=open_img)
        save_button = Button(toolbar, image=save_img)
        exit_button = Button(toolbar, image=exit_img, command=self.quit_app)

        open_button.image = open_img
        save_button.image = save_img
        exit_button.image = exit_img

        open_button.pack(side=LEFT, padx=2, pady=2)
        save_button.pack(side=LEFT, padx=2, pady=2)
        exit_button.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)

        root.config(menu=menubar)

        lb_frame = LabelFrame(root, text="Food Options", padx=5, pady=5)
        self.fav_food_label = Label(lb_frame,
                                    text="What is your favorite food?")
        self.fav_food_label.pack()
        list_box = Listbox(lb_frame)

        list_box.insert(1, "Pizza")
        list_box.insert(2, "Hamburger")
        list_box.insert(3, "Pasta")
        list_box.insert(4, "Tacos")
        list_box.bind('<<ListboxSelect>>', self.on_fav_food_select)

        list_box.pack()
        lb_frame.pack()

        sb_frame = Frame(root)
        quantity_label = Label(sb_frame,
                               text="How many do you want?")
        quantity_label.pack()
        spin_box = Spinbox(sb_frame, from_=1, to=5)
        spin_box.pack()
        extras_label = Label(sb_frame, text='Add on item')
        extras_label.pack()

        extras_spin_box = Spinbox(sb_frame,
                                  values=('Cheese', 'Lettuce', 'Tomato'))
        extras_spin_box.pack()

        sb_frame.pack()


root = Tk()
root.geometry("600x550")
TkInterEX(root)
root.mainloop()
