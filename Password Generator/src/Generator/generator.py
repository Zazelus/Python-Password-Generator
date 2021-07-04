'''
Created on Jul 3, 2021

@author: Zazelus
'''

from os import path
import os.path
import random
from tkinter import *

import tkinter as tk


background = "#35323b"
button = "#91C3D5"
white = "#FFFFFF"

root = Tk()
root.title('Password Generator')
root.geometry("500x500")
root.configure(bg=background)

# Generates a new random password.
def new_rand():
    available_chars = allowed_characters()

    # Clearing entry box.
    output_entry.delete(0, END)

    # Get the password length.
    pw_length = int(user_entry.get())

    password = ''

    char_list = Convert(available_chars)

    for x in range(pw_length):
        password += random.choice(char_list)

    # Password sent to screen.
    output_entry.insert(0, password)


# Python code to convert string to list character-wise
def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

# Copies generated password to clipboard.
def copy():
    root.clipboard_clear()
    root.clipboard_append(output_entry.get())

# Checks checkboxes in order to find which characters are available.
def allowed_characters():
    special_chars = "!$%@#"
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    available_chars = ""

    if (var1.get() == 1):
        available_chars += special_chars
    if (var2.get() == 1):
        available_chars += numbers
    if (var3.get() == 1):
        available_chars += lower_case
    if (var4.get() == 1):
        available_chars += upper_case

    return available_chars

def add_to_file():
    if (path.exists("../../passwords/passwords.txt")):
        with open('../../passwords/passwords.txt', 'a') as file:
            file.write(output_entry.get() + "\n")
    else:
        with open('../../passwords/passwords.txt', 'w') as file:
            file.write(output_entry.get() + "\n")

# Frame for the label.
label = LabelFrame(root, text="How Many Characters?", bg=background, fg=white)
label.pack(pady=20)

# Entry box to enter desired number of characters.
user_entry = Entry(label, font=("Helvetica", 24))
user_entry.pack(pady=20, padx=20)

# Setting up checkboxes for a more customizable password.
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
c1 = tk.Checkbutton(label, text='Include Symbols ( e.g. @#$% ):',variable=var1, onvalue=1, offvalue=0,
                    selectcolor=background, bg=background, fg=white)
c1.pack()
c2 = tk.Checkbutton(label, text='Include Numbers:',variable=var2, onvalue=1, offvalue=0,
                    selectcolor=background, bg=background, fg=white)
c2.pack()
c3 = tk.Checkbutton(label, text='Include Lowercase Characters:',variable=var3, onvalue=1, offvalue=0,
                    selectcolor=background, bg=background, fg=white)
c3.pack()
c4 = tk.Checkbutton(label, text='Include Uppercase Characters:',variable=var4, onvalue=1, offvalue=0,
                    selectcolor=background, bg=background, fg=white)
c4.pack()

# Frame for the output label.
output_label = LabelFrame(root, text="Generated Password", bg=background, fg=white)
output_label.pack(pady=20)

# 'Invisible' entry box for returned password.
output_entry = Entry(output_label, text='', font=("Helvetica", 24), bd=0, bg=background, fg=white)
output_entry.pack(pady=20)

my_frame = Frame(root, bg=background)
my_frame.pack(pady=20)

# Generate password button that calls new_rand().
generate_button = Button(my_frame, text="Generate Password", command=new_rand,
                         bg=button, fg=white)
generate_button.grid(row=0, column=0, padx=10)

# Copy to clipboard button that copies the generated password.
copy_button = Button(my_frame, text="Copy To Clipboard", command=copy,
                     bg=button, fg=white)
copy_button.grid(row=0, column=1, padx=10)

# Create and add to file or append to an existing file.
file_button = Button(my_frame, text="Create/Add to File", command=add_to_file,
                     bg=button, fg=white)
file_button.grid(row=0, column=2, padx=10)

root.mainloop()


