import random
import tkinter as tk
import string

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '_', '+', '-', '=', '[', ']', '{', '}', '\\', '|',
    ';', ':', "'", '"', ',', '.', '<', '>', '/', '?',
    '`', '~'
]

# ----- GUI Setup -----
root = tk.Tk()
root.title("Password Generator")
root.geometry("380x450")
root.configure(bg="lightblue")

# Input Labels and Entry Boxes
label1 = tk.Label(root, text = ' Enter the Letters quantity you want to', font=('Times New Roman',14, 'bold'), bg="white")
label1.pack(pady=2)
entry1 = tk.Entry(root, font = ('Times New Roman',12,'normal'))
entry1.pack(pady=2)

label2 = tk.Label(root, text = 'Enter the symbols quantity you want to', font=('Times New Roman',14, 'bold'), bg="white")
label2.pack(pady=2)
entry2 = tk.Entry(root, font = ('Times New Roman',12,'normal'))
entry2.pack(pady=2)

label3 = tk.Label(root, text = 'Enter the numbers quantity you want to', font=('Times New Roman',14, 'bold'), bg="white")
label3.pack(pady=2)
entry3 = tk.Entry(root, font = ('Times New Roman',12,'normal'))
entry3.pack(pady=2)

# Output Label
result_label = tk.Label(root, text="Your Password:", font=('Times New Roman',12, 'bold'), bg="white")
result_label.pack(pady=5)

# Output Box
password_var = tk.StringVar()
output_box = tk.Entry(root, textvariable=password_var, font=('Times New Roman',12,'normal'), justify='center')
output_box.pack(pady=5)



def password_generator():
    password_list=[]
    password=""
    
    n_letters = int(entry1.get())
    n_symbols = int(entry2.get())
    n_numbers = int(entry3.get())
   

    if (n_letters + n_symbols + n_numbers) >=8:
        for i in range(1,n_letters+1):
            char=random.choice(letters)
            password_list.append(char)
            
        for i in range(1,n_symbols+1):
            char=random.choice(symbols)
            password_list.append(char)
        for i in range(1,n_numbers+1):
            char=random.choice(numbers)
            password_list.append(char)
        random.shuffle(password_list)
        print(password_list)    
        for char in password_list:
            password += char

        print("Password generated:", password)
        password_var.set(password)
    else:
        print("Error: Maximum total characters allowed is 8.")
        password_var.set("Max 8 only")


btn = tk.Button(root, text="Password Generate", font=('calibre',10,'bold'), bg="green", fg="white", command=password_generator)
btn.pack(pady=10)

root.mainloop()

