import tkinter
root = tkinter.Tk()

#title bar name
root.title('Test App')


# Resize the window
root.resizable(width="false", height="false")

#  minimized

root.minsize(width=300, height=300)
root.maxsize(width=300, height=300)

'''
        Frame
'''
frame_labels = tkinter.Frame(root, relief="ridge")
frame_labels.grid(column=0, row=0, sticky="ns")


frame_buttons = tkinter.Frame(root, relief="ridge")
frame_buttons.grid(column=1, row=0)

'''
        New Window
'''
new_window = tkinter.Toplevel()
new_window.withdraw()

simple_label = tkinter.Label(root, text="Hello ! Whats up?")
another_label = tkinter.Label(root, text="More Text")    #   Widget Orientation


close_button = tkinter.Button(frame_buttons, text="Close", command=root.destroy)
another_button = tkinter.Button(frame_buttons, text="Do Nothing")  #  Widget Orientation
window_button = tkinter.Button(frame_buttons, text="Show new window", command=new_window.deiconify) #New Window added


######  Widget Orientation   #########
simple_label.grid(column=0, row=0, sticky="ew")
another_label.grid(column=0, row=1, sticky="ew")

close_button.grid(column=1, row=0, sticky="ew")
another_button.grid(column=1, row=1, sticky="ew")


#
# simple_label.pack()
# another_label.pack()
#
# close_button.pack(fill ="x")
# another_button.pack(fill ="x")

root.mainloop()