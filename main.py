import SearchMark as sm
from tkinter import *
import webbrowser

"""key = input("Enter key:")
alist = sm.searchMark(key)
for val in alist:
    print(val)"""
root = Tk()
root.title("Book Mark Searcher")
enter = Entry(root)
text = Text(root, width=50, height=10)
myLabel = Label(root, text="Search Key")
text.grid(row=3, column=1)


def onClick():
    text.delete("1.0", "end")
    key = enter.get()
    alist = sm.searchMark(key)
    # textList = list()
    for val in alist:
        text.insert(END, val + "\n\n")


myButton = Button(root, text="Search", command=onClick)
myLabel.grid(row=0, column=1)
enter.grid(row=1, column=1)
myButton.grid(row=2, column=1)
root.mainloop()

#hyperlink.add(partial(webbrowser.open,val))
