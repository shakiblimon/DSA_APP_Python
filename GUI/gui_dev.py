import tkinter
root = tkinter.Tk()

#title bar name
root.title('Test App')

# Resize the window
root.resizable(width="false", height="false")

#  minimized

root.minsize(width=300, height=300)
root.maxsize(width=300, height=300)


simple_label = tkinter.Label(root, text="Hello ! Whats up?")
another_label = tkinter.Label(root , text = "More Text")

close_button = tkinter.Button(root, text ="Close", command =root.destroy)
another_button = tkinter.Button(root, text = "Do Nothing")


simple_label.grid(column=0, row=0, sticky="ew")
another_label.grid(column=0, row=1, sticky="ew")

close_button.grid(column=1, row=0, sticky="ew")
another_button.grid(column=1, row=1 , sticky="ew")

# simple_label.pack()
# close_button.pack()


root.mainloop()