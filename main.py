import re
import tkinter as tk
from tkinter import ttk, scrolledtext
from PIL import Image, ImageTk
from lexer import tokenize
from SymbolTable import SymbolTable
from First_Follow import grammar
from hash_table import HashTable

def process_code():
    code = code_input.get("1.0", tk.END).strip()  
    tokens = tokenize(code)  
    
    symbol_table = SymbolTable()
    symbol_table.generate_table(code)  

    hash_table = HashTable(hash_max=3)
    hash_table.process_code(code)

    token_output.delete("1.0", tk.END)
    token_output.insert(tk.END, "🔹Tokens and Lexemes:\n")
    token_output.insert(tk.END, " -----------------\n\n")
    for token in tokens:
        token_output.insert(tk.END, f" {token[0]}: {token[1]}\n\n")

    symbol_table_output.delete("1.0", tk.END)
    symbol_table_output.insert(tk.END, "🔹Symbol Table:\n")
    symbol_table_output.insert(tk.END, " -----------------\n\n")
    headers = ["Counter", "Variable Name", "Address", "Data Type", "No. of Dimensions", "Line Declaration", "Line References"]
    table_data = symbol_table.get_table_data()

    table_str = f"  {headers[0]:<10}  {headers[1]:<15}  {headers[2]:<10}  {headers[3]:<10}   {headers[4]:<15}   {headers[5]:<15}   {headers[6]:<20}\n"
    table_str += "-" * 110 + "\n"
    for row in table_data:
        table_str += f"  {row[0]:<10}     {row[1]:<15}   {row[2]:<10}  {row[3]:<10}       {row[4]:<15}       {row[5]:<15}       {row[6]:<20}\n"
        table_str += "-" * 110 + "\n"
    symbol_table_output.insert(tk.END, table_str)
    

    hash_table_output.delete("1.0", tk.END)
    hash_table_output.insert(tk.END, "🔹Hash Table:\n")
    hash_table_output.insert(tk.END, " -----------------\n\n")
    hash_table_output.insert(tk.END, f"{'Hash Value':<15}{'Identifier'}\n")
    hash_table_output.insert(tk.END, "-" * 30 + "\n")

    for hash_value in sorted(hash_table.get_table_data().keys()):
        identifiers = " ".join(hash_table.get_table_data()[hash_value])  
        hash_table_output.insert(tk.END, f"{hash_value:<12}{identifiers}\n")



    first_output.delete("1.0", tk.END)
    first_output.insert(tk.END, "🔹Grammar:\n")
    first_output.insert(tk.END, " -----------------\n\n")
    for non_terminal, productions in grammar.rules.items():
        first_output.insert(tk.END, f"{non_terminal}: {productions}\n\n")
    first_output.insert(tk.END, "🔹FIRST Sets:\n")
    first_output.insert(tk.END, " -----------------\n\n")
    for non_terminal, first_set in grammar.first.items():
        first_output.insert(tk.END, f"{non_terminal}: {first_set}\n\n")


    follow_output.delete("1.0", tk.END)
    follow_output.insert(tk.END, "🔹Grammar:\n")
    follow_output.insert(tk.END, " -----------------\n\n")
    for non_terminal, productions in grammar.rules.items():
        follow_output.insert(tk.END, f"{non_terminal}: {productions}\n\n")
    follow_output.insert(tk.END, "🔹FOLLOW Sets:\n")
    follow_output.insert(tk.END, " ----------------\n\n")
    for non_terminal, follow_set in grammar.follow.items():
        follow_output.insert(tk.END, f"{non_terminal}: {follow_set}\n\n")

def clear_all():
    
    code_input.delete("1.0", tk.END)
    token_output.delete("1.0", tk.END)
    symbol_table_output.delete("1.0", tk.END)
    hash_table_output.delete("1.0", tk.END)
    first_output.delete("1.0", tk.END)
    follow_output.delete("1.0", tk.END)

def show_main_app():
    welcome_frame.pack_forget()
    main_frame.pack(fill=tk.BOTH, expand=True)
    

app = tk.Tk()
app.title("Mini Compiler")
app.geometry("1000x900")  

app.configure(bg="#F9F4F4")


welcome_frame = tk.Frame(app, bg="#F9F4F4")
welcome_frame.pack(fill=tk.BOTH, expand=True)


welcome_title = tk.Label(welcome_frame, text="\n\nWelcome to Mini Compiler 😊", font=("Arial", 24, "bold"), bg="#F9F4F4", fg="#4B8BBE")
welcome_title.pack(pady=15)


image = Image.open("compilerphoto.jpg")  
image = image.resize((450, 450))
icon = ImageTk.PhotoImage(image)
icon_label = tk.Label(welcome_frame, image=icon, bg="#F9F4F4")
icon_label.pack(pady=20)

start_button = tk.Button(welcome_frame, text=" Start ", font=("Arial", 20), command=show_main_app, bg="#B2ADEF")
start_button.pack(pady=23)


main_frame = tk.Frame(app, bg="#F9F4F4")


title_frame = tk.Frame(main_frame, bg="#F9F4F4")
title_frame.pack(fill=tk.X, pady=10)


title_label = tk.Label(title_frame, text=" \n⚙️ Mini Compiler\n", font=("Arial", 28, "bold"), bg="#F9F4F4", fg="#4B8BBE")
title_label.pack(side=tk.TOP, padx=10)

tab_control = ttk.Notebook(main_frame)
input_tab = ttk.Frame(tab_control)
tokens_tab = ttk.Frame(tab_control)
symbol_table_tab = ttk.Frame(tab_control)
hash_table_tab = ttk.Frame(tab_control)
first_tab = ttk.Frame(tab_control)
follow_tab = ttk.Frame(tab_control)

tab_control.add(input_tab, text=" Input Code ")
tab_control.add(tokens_tab, text=" Tokens ")
tab_control.add(symbol_table_tab, text="  Symbol Table  ")
tab_control.add(hash_table_tab, text="  Hash Table  ")
tab_control.add(first_tab, text=" FIRST Sets ")
tab_control.add(follow_tab, text=" FOLLOW Sets ")
tab_control.pack(expand=1, fill="both")


code_input = scrolledtext.ScrolledText(input_tab, height=18, font=("Courier", 16), bg="#E8E8E8")  
code_input.pack(fill=tk.BOTH, expand=False, padx=10, pady=10)

button_frame = tk.Frame(input_tab, bg="#F9F4F4")
button_frame.pack(pady=5)

tk.Button(button_frame, text="Process Code", font=("Arial", 18), command=process_code, bg="#B2ADEF").pack(side=tk.LEFT, padx=8) 
tk.Button(button_frame, text="Clear", font=("Arial", 18), command=clear_all, bg="#20A473").pack(side=tk.LEFT, padx=8)  


token_output = scrolledtext.ScrolledText(tokens_tab, height=20, font=("Courier", 14), bg="#E8E8E8")
token_output.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)


symbol_table_output = scrolledtext.ScrolledText(symbol_table_tab, height=20, font=("Courier", 14), bg="#E8E8E8")
symbol_table_output.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

hash_table_output = scrolledtext.ScrolledText(hash_table_tab, height=20, font=("Courier", 14), bg="#E8E8E8")
hash_table_output.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

first_output = scrolledtext.ScrolledText(first_tab, height=20, font=("Courier", 14), bg="#E8E8E8")
first_output.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

follow_output = scrolledtext.ScrolledText(follow_tab, height=20, font=("Courier", 14), bg="#E8E8E8")
follow_output.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

app.mainloop()
