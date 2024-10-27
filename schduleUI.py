import customtkinter
import scheduler

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x800")



# addroombutton = customtkinter.CTkButton(master=app,text="Create room", command=button_function)

#adding a room we will want to make this selectable from a list
#also write this size to a list using a matrix array that has a length of 16 and a height depending on the amount of locations

# def button_function():
#     print("button pressed")

# Use CTkButton instead of tkinter Button
# button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()
 
