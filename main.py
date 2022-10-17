import SearchMark as sm
from tkinter import *
"""
Note: The main file to implement the UI using tkinter 
"""
root = Tk()
root.title("Book Mark Searcher")
enter = Entry(root)
text = Text(root, width=50, height=10)
myLabel = Label(root, text="Search Key")
text.grid(row=3, column=1)


def onClick():
    """
    Note: On click function used to search the URL list when the Search  button is pressed, displays the output URLs
    in a text box.
    """
    text.delete("1.0", "end")
    key = enter.get()
    alist = sm.searchMark(key)
    for val in alist:
        text.insert(END, val + "\n\n")


myButton = Button(root, text="Search", command=onClick)
myLabel.grid(row=0, column=1)
enter.grid(row=1, column=1)
myButton.grid(row=2, column=1)
root.mainloop()
