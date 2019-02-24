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
close_button = tkinter.Button(root, text ="Close", command =root.destroy)

simple_label.pack()
close_button.pack()


root.mainloop()