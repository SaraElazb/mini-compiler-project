# ⚙️ Mini Compiler Project

The **Mini Compiler Project** is designed to implement the lexical analysis phase of a compiler. This project includes:

- 📝 Generating tokens and lexemes from a defined grammar.
- 📚 Creating an unordered symbol table and a hash-based symbol table.
- 🔍 Generating the First and Follow sets for a subset of production rules.
- 🖥️ Providing a user-friendly GUI for interaction.

This project is developed as part of a **Compiler Design** course to provide hands-on experience with key concepts in lexical analysis and grammar rule processing.

## Features

1. **Token and Lexeme Generation**: 
   - 🧩 Processes source code based on the provided grammar.
   - 📄 Outputs tokens and their corresponding lexemes.

2. **Symbol Table**: 
   - 📋 Maintains two versions of symbol tables:
     - **Unordered Symbol Table**: Stores identifiers in the order of their appearance.
     - **Hash-based Symbol Table**: Stores identifiers using hashing for faster lookup.

3. **First and Follow Sets**:
   - 🧮 Implements algorithms to compute First and Follow sets for given production rules.

4. **Graphical User Interface (GUI)**:
   - 🖱️ A GUI built using `tkinter` for easy interaction with the lexical analyzer and symbol table.

## Project Structure

```
Mini-Compiler/
├── First_Follow.py         # Computes First and Follow sets
├── Grammar.py              # Defines grammar and rule processing
├── hash_table.py           # Implements hash-based symbol table
├── lexer.py                # Handles token and lexeme generation
├── main.py                 # Entry point for running the GUI
├── SymbolTable.py          # Manages the unordered symbol table
```

## How to Run

1. **Setup Environment**:
   - 🛠️ Ensure Python 3.8+ is installed.
   - 📦 Install dependencies using:
     ```
     pip install -r requirements.txt
     ```

2. **Run the Application**:
   - 🚀 Launch the GUI by running:
     ```
     python main.py
     ```

3. **Use the GUI**:
   - 💻 Input source code and interact with lexical analysis features directly from the GUI.

## Input Format
- The input source code must conform to the grammar defined in `Grammar.py`.


## Graphical User Interface (GUI)
<div align="center">
   <img src="https://github.com/SaraElazb/Compilers-Project/blob/main/assets/mini_compiler1.png" alt="Mini_Compiler image" width="580px"><br>
   <img src="https://github.com/SaraElazb/Compilers-Project/blob/main/assets/mini_compiler2.png" alt="Mini_Compiler image" width="580px"><br>
</div>

## Demo
Check out the demo [here](https://drive.google.com/file/d/1NLp5jU7Lzv2S72DuUMV6YTts75TpvxOz/view?usp=drivesdk) 🚀

## How to Contribute
1. 🍴 Fork the repository.
2. 🌿 Create a new branch.
3. 💾 Commit your changes.
4. 📬 Submit a pull request.

## 👩🏻‍💻 Team members
- [Amira Alagha](https://github.com/amira-algha)
- [Sara Elazb](https://github.com/SaraElazb)
- [Sara Elshaer](https://github.com/saraelshaer) 


