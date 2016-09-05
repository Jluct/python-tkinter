from tkinter import *

root = Tk()
root.title("Мессаджер")
root.minsize(800, 500)
root.maxsize(800, 500)

user_name = Label(root,
                  text="Иванов Иван Иванович",
                  fg="red",
                  justify='center',
                  font="Arial 20",
                  # width=50,
                  )

user_name.grid(row=1, column=2, columnspan=3)

friend_list_view = Frame(root, bd=1)
friend_list_view.grid(row=2, column=1, rowspan=3)

dialog_view = Frame(root, bd=3, bg="blue")
dialog_view.grid(row=2, column=2, rowspan=3, columnspan=2)

text1 = Text(friend_list_view, height=1, width=30, font='Arial 12', wrap=WORD)
text2 = Text(friend_list_view, height=1, width=30, font='Arial 12', wrap=WORD)
text1.grid(row=1, column=1)
text2.grid(row=2, column=1)

root.mainloop()
