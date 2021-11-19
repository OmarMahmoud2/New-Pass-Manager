from tkinter import *
import tkinter.font as font 
from tkinter import messagebox 
import random
import pyperclip
import json


def register_wn():
  # ---------------------------- PASSWORD GENERATOR ------------------------------- #
  def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []  
  
    for char in range(nr_letters):
      password_list.append(random.choice(letters))
  
    for char in range(nr_symbols):
      password_list += random.choice(symbols)
  
    for char in range(nr_numbers):
      password_list += random.choice(numbers)
  
    random.shuffle(password_list)
  
    password = ""
    for char in password_list:
      password += char
    passent.delete(0, END)
    passent.insert(0,password)
    try:
      pyperclip.copy(password)
    except:
      pass
  
  # ---------------------------- SAVE PASSWORD ------------------------------- #
  
  def add():
    web = webent.get().lower()
    email = ement.get()
    password = passent.get()
    
    datadict = {web :{'E-Mail': email, 'Password': password}}
    
    if len(web) < 1 or len(email) < 1 or len(password) < 5:
      messagebox.showinfo(title='Oops!', message=' Please Do not leave any fields empty!')
      
    else:
      try:
        with open('data.json', 'r') as file:
          data = json.load(file)
      except FileNotFoundError:
        with open('data.json', 'w') as file:
          json.dump(datadict, file, indent=4)
      else:
        data.update(datadict)
        with open('data.json', 'w') as file:
          json.dump(data, file, indent=4)
      finally:
        webent.delete(0,END)
        ement.delete(0,END)
        passent.delete(0,END)
    
    
  # ---------------------------- UI SETUP ------------------------------- #

  welcome.destroy()
  #windows.destroy()
  window = Tk()
  window.title('Password Registry')
  window.config(padx=50, pady=50, bg='White')
  window.minsize(300, 300)



  canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
  img = PhotoImage(file='logo.png')
  image = canvas.create_image(100, 100, image=img)
  canvas.grid(column=1, row=0)


  webleb = Label(text=('Website: '), bg='white')
  webleb.grid(column=0, row=1)

  emleb = Label(text='E-mail/Username: ', bg='white')
  emleb.grid(column=0, row=2)

  passleb= Label(text='Password: ', bg='white')
  passleb.grid(column=0, row=3)

  webent = Entry(width=35)
  webent.grid(column=1, row=1, columnspan=2)
  webent.focus()
  ement = Entry(width=35)
  ement.insert(0, 'Omarm@gmail.com')
  ement.grid(column=1, row=2, columnspan=2)

  passent = Entry(width=21)
  passent.grid(column=1, row=3)
  #font = font.Font(family='ariel', size=8, weight='bold') 

  passbutt = Button(text='Generate Pass', width = 12, command=generate_pass)
  #passbutt['font'] = font
  passbutt.grid(column=2, row=3)


  addbutt = Button(text= 'Add Password', width= 37, command=add)
  addbutt.grid(column=1, row=4, columnspan=2)
  #addbutt['font'] = font
  
  window.mainloop()


def show():
  
  def get_pass():
    website = entry1.get().lower()
    try:
      with open('data.json', 'r') as file:
        data = json.load(file)
    except FileNotFoundError:
      messagebox.showinfo(title='Oops', message='No Websites saved')
    else:
      if website in data:
        messagebox.showinfo(title=website, message=f"Username: {data[website]['E-Mail']}\n Password: {data[website]['Password']}")
      else:
        messagebox.showinfo(title='Oops!', message=f"You don't have any Passwords saved with this website {website}")
         
        
  welcome.destroy()
  windows = Tk()
  windows.title('Retrieve Old Password')
  windows.config(padx=50, pady=50, bg='White')
  windows.minsize(150, 200)
  
  canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
  img = PhotoImage(file='logo.png')
  image = canvas.create_image(100, 100, image=img)
  canvas.grid(column=1, row=0)
  
  label1= Label(text='Please Enter the Website: ', bg='white')
  label1.grid(column=1, row= 1)
  
  entry1= Entry(width=35)
  entry1.grid(column=1, row=2)
  entry1.focus()
  
  button1= Button(text='Search', width=20, command=get_pass)
  button1.grid(column=1, row=3)
  
  button2= Button(text='Register Password', command=register_wn)
  #button2.grid(column=1, row=4)
  

  
  
  windows.mainloop()
  
  
welcome = Tk()
welcome.title('Password Manager')
welcome.config(padx=50, pady=50, bg='White')
welcome.minsize(200, 200)

canvas = Canvas(width=200, height=200, bg='white',highlightthickness=0)
img = PhotoImage(file='logo.png')
image = canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

add = Button(text='Add New Password', command=register_wn)
add.grid(column=0, row=1)

search = Button(text='Retrieve Old Password', command=show)
search.grid(column=2, row=1)

exbutt = Button(text='Exit', command=welcome.destroy)
exbutt.grid(column=1, row=2)







welcome.mainloop()