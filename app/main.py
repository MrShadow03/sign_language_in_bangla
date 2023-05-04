import tkinter as tk
import ttkbootstrap as ttk

def getName():
    output_label.config(font=("Hind Siliguri", 24, "bold"), foreground = "#056eb2")
    output_value.set(input_value.get())
    
#create the main window
window = tk.Tk()

#set the window title and size
window.title("My First GUI Program");
window.geometry("800x600")

# Create a ttk.Style object and set the theme to "journal"
style = ttk.Style(theme="yeti")

#create the label in Bold font
page_heading = ttk.Label(master = window, text = "আমার প্রথম পাইথন অ্যাপ্লিকেশন", font = ("Hind Siliguri", 16, "bold"), foreground = "#1c1c1c")
page_heading.pack()

#input field
input_frame = ttk.Frame(master = window)
input_value = tk.StringVar()
input_field = ttk.Entry(master = input_frame, width = 50, textvariable = input_value)
input_button = ttk.Button(master = input_frame, text = "সাবমিট", width = 10, command= getName)
input_field.pack(side = 'left', padx = 10, pady = 10)
input_button.pack(side = 'left')
input_frame.pack()

#output field
output_value = tk.StringVar()
output_label = ttk.Label(master = window, text = "আপনার নাম লিখুন", font = ("Hind Siliguri", 12), foreground = "#056eb2", textvariable = output_value)
output_label.pack(pady = 10)

#run the main loop
window.mainloop()