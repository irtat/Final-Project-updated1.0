import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Initialize NLTK resources
nltk.download('punkt')
nltk.download('vader_lexicon')

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is PyBot and I'm here to assist you about python.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!",]
    ],
    [
        r"(.*) (good|great|well) ?",
        ["That's awesome to hear!",]
    ],
    [
        r"who created you?",
        ["I'm created by a Muhammad Irtat Mobin",]
    ],
    [
        r"what is the name of his Institute?",
        ["BANO QABIL 2.0",]
    ],
    [
        r"what is the name of their Instructor?",
        ["Fahad Bin Ashfaq",]
    ],
    [
        r"what is python?",
        ["Python is a high-level programming language known for its simplicity, readability, and versatility.",]
    ],
    [
        r"What is Python?",
        ["Python is a high-level programming language known for its simplicity, readability, and versatility.",]
    ],
    [
        r"What is python?",
        ["Python is a high-level programming language known for its simplicity, readability, and versatility.",]
    ],
    [
        r"what is Python?",
        ["Python is a high-level programming language known for its simplicity, readability, and versatility.",]
    ],
    [
        r"what is python",
        ["Python is a high-level programming language known for its simplicity, readability, and versatility.",]
    ],
    [
        r"What is Python",
        ["Python is a high-level programming language known for its simplicity, readability, and versatility.",]
    ],
    [
        r"What is python",
        ["Python is a high-level programming language known for its simplicity, readability, and versatility.",]
    ],
    [
        r"what is Python",
        ["Python is a high-level programming language known for its simplicity, readability, and versatility.",]
    ],
    [
        r"what is variable?",
        ["A variable in Python is a named storage location used to store data that can be referenced and manipulated within a program.",]
    ],
    [
        r"What is Variable?",
        ["A variable in Python is a named storage location used to store data that can be referenced and manipulated within a program.",]
    ],
    [
        r"What is variable?",
        ["A variable in Python is a named storage location used to store data that can be referenced and manipulated within a program.",]
    ],
    [
        r"what is Variable?",
        ["A variable in Python is a named storage location used to store data that can be referenced and manipulated within a program.",]
    ],
    [
        r"how many data types are there in python?",
        ["Python includes several built-in data types such as integers, floats, complex numbers, strings, lists, tuples, dictionaries, sets, and booleans.",]
    ],
    [
        r"How many data types are there in python?",
        ["Python includes several built-in data types such as integers, floats, complex numbers, strings, lists, tuples, dictionaries, sets, and booleans.",]
    ],
    [
        r"how many data types are there in python",
        ["Python includes several built-in data types such as integers, floats, complex numbers, strings, lists, tuples, dictionaries, sets, and booleans.",]
    ],
    [
        r"How many data types are there in python",
        ["Python includes several built-in data types such as integers, floats, complex numbers, strings, lists, tuples, dictionaries, sets, and booleans.",]
    ],
    [
        r"how many loops are used in python?",
        ["In Python, there are two main types of loops: the for loop and the while loop. Additionally, Python supports loop control statements such as break and continue to modify loop behavior.",]
    ],
    [
        r"How many loops are used in python?",
        ["In Python, there are two main types of loops: the for loop and the while loop. Additionally, Python supports loop control statements such as break and continue to modify loop behavior.",]
    ],
    [
        r"how many loops are used in python",
        ["In Python, there are two main types of loops: the for loop and the while loop. Additionally, Python supports loop control statements such as break and continue to modify loop behavior.",]
    ],
    [
        r"How many loops are used in python",
        ["In Python, there are two main types of loops: the for loop and the while loop. Additionally, Python supports loop control statements such as break and continue to modify loop behavior.",]
    ],
    [
        r"how many things can we do using python?",
        ["The possibilities with Python are virtually limitless. Some common applications of Python include web development, data analysis, machine learning, artificial intelligence, automation, scripting, game development, scientific computing, and more. Python's extensive standard library and vast ecosystem of third-party packages enable developers to tackle a wide range of tasks efficiently and effectively.",]
    ],
    [
        r"How many things can we do using python?",
        ["The possibilities with Python are virtually limitless. Some common applications of Python include web development, data analysis, machine learning, artificial intelligence, automation, scripting, game development, scientific computing, and more. Python's extensive standard library and vast ecosystem of third-party packages enable developers to tackle a wide range of tasks efficiently and effectively.",]
    ],
    [
        r"how many things can we do using python",
        ["The possibilities with Python are virtually limitless. Some common applications of Python include web development, data analysis, machine learning, artificial intelligence, automation, scripting, game development, scientific computing, and more. Python's extensive standard library and vast ecosystem of third-party packages enable developers to tackle a wide range of tasks efficiently and effectively.",]
    ],
    [
        r"How many things can we do using python",
        ["The possibilities with Python are virtually limitless. Some common applications of Python include web development, data analysis, machine learning, artificial intelligence, automation, scripting, game development, scientific computing, and more. Python's extensive standard library and vast ecosystem of third-party packages enable developers to tackle a wide range of tasks efficiently and effectively.",]
    ],
    [
        r"who invented python?",
        ["Python was created by Guido van Rossum, a Dutch programmer, in the late 1980s.",]
    ],
    [
        r"Who invented Python?",
        ["Python was created by Guido van Rossum, a Dutch programmer, in the late 1980s.",]
    ],
    [
        r"who invented python",
        ["Python was created by Guido van Rossum, a Dutch programmer, in the late 1980s.",]
    ],
    [
        r"Who invented Python",
        ["Python was created by Guido van Rossum, a Dutch programmer, in the late 1980s.",]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I can help you with that. What do you need assistance with?",]
    ],
    [
        r"how many operators are there in python?",
        ["Python has various operators, including arithmetic, comparison, assignment, logical, bitwise, membership, and identity operators. In total, there are 33 operators in Python.",]
    ],
    [
        r"How many operators are there in python?",
        ["Python has various operators, including arithmetic, comparison, assignment, logical, bitwise, membership, and identity operators. In total, there are 33 operators in Python.",]
    ],
    [
        r"how many operators are there in python",
        ["Python has various operators, including arithmetic, comparison, assignment, logical, bitwise, membership, and identity operators. In total, there are 33 operators in Python.",]
    ],
    [
        r"How many operators are there in python",
        ["Python has various operators, including arithmetic, comparison, assignment, logical, bitwise, membership, and identity operators. In total, there are 33 operators in Python.",]
    ],
    [
        r"what is comments in python?",
        ["In Python, comments are pieces of text in the code that are ignored during execution. They help explain the code and make it easier to understand. You can use a hash symbol (#) for single-line comments or triple quotes for multi-line comments.",]
    ],
    [
        r"What is comments in python?",
        ["In Python, comments are pieces of text in the code that are ignored during execution. They help explain the code and make it easier to understand. You can use a hash symbol (#) for single-line comments or triple quotes for multi-line comments.",]
    ],
    [
        r"what is comments in python",
        ["In Python, comments are pieces of text in the code that are ignored during execution. They help explain the code and make it easier to understand. You can use a hash symbol (#) for single-line comments or triple quotes for multi-line comments.",]
    ],
    [
        r"What is comments in python",
        ["In Python, comments are pieces of text in the code that are ignored during execution. They help explain the code and make it easier to understand. You can use a hash symbol (#) for single-line comments or triple quotes for multi-line comments.",]
    ],
    [
        r"how many conditional statements are there in python?",
        ["There are three conditional statements in Python: `if`, `elif` (else if), and `else`.",]
    ],
    [
        r"How many conditional statements are there in python?",
        ["There are three conditional statements in Python: `if`, `elif` (else if), and `else`.",]
    ],
    [
        r"how many conditional statements are there in python",
        ["There are three conditional statements in Python: `if`, `elif` (else if), and `else`.",]
    ],
    [
        r"How many conditional statements are there in python",
        ["There are three conditional statements in Python: `if`, `elif` (else if), and `else`.",]
    ],
    [
        r"what is loops?",
        ["Loops in programming are used to repeat a block of code until a certain condition is met. There are two main types in Python: `for` loops, which iterate over a sequence, and `while` loops, which repeat until a condition is no longer true.",]
    ],
    [
        r"what is loops",
        ["Loops in programming are used to repeat a block of code until a certain condition is met. There are two main types in Python: `for` loops, which iterate over a sequence, and `while` loops, which repeat until a condition is no longer true.",]
    ],
    [
        r"define loops?",
        ["Loops in programming are used to repeat a block of code until a certain condition is met. There are two main types in Python: `for` loops, which iterate over a sequence, and `while` loops, which repeat until a condition is no longer true.",]
    ],
    [
        r"define loops",
        ["Loops in programming are used to repeat a block of code until a certain condition is met. There are two main types in Python: `for` loops, which iterate over a sequence, and `while` loops, which repeat until a condition is no longer true.",]
    ],
    [
        r"what is lists?",
        ["Lists in Python are ordered collections of items that can contain different data types. They are enclosed in square brackets ([]), and their elements can be modified after creation. Lists are versatile and commonly used for storing and manipulating data.",]
    ],
    [
        r"what is lists",
        ["Lists in Python are ordered collections of items that can contain different data types. They are enclosed in square brackets ([]), and their elements can be modified after creation. Lists are versatile and commonly used for storing and manipulating data.",]
    ],
    [
        r"define lists?",
        ["Lists in Python are ordered collections of items that can contain different data types. They are enclosed in square brackets ([]), and their elements can be modified after creation. Lists are versatile and commonly used for storing and manipulating data.",]
    ],
    [
        r"define lists",
        ["Lists in Python are ordered collections of items that can contain different data types. They are enclosed in square brackets ([]), and their elements can be modified after creation. Lists are versatile and commonly used for storing and manipulating data.",]
    ],
    [
        r"what is dictionaries?",
        ["A dictionary in Python is a collection of key-value pairs. Keys are unique and immutable, while values can be of any data type. They are enclosed in curly braces ({ }). Dictionaries are used for efficient data lookup and representation.",]
    ],
    [
        r"what is dictionaries",
        ["A dictionary in Python is a collection of key-value pairs. Keys are unique and immutable, while values can be of any data type. They are enclosed in curly braces ({ }). Dictionaries are used for efficient data lookup and representation.",]
    ],
    [
        r"define dictionaries?",
        ["A dictionary in Python is a collection of key-value pairs. Keys are unique and immutable, while values can be of any data type. They are enclosed in curly braces ({ }). Dictionaries are used for efficient data lookup and representation.",]
    ],
    [
        r"define dictionaries",
        ["A dictionary in Python is a collection of key-value pairs. Keys are unique and immutable, while values can be of any data type. They are enclosed in curly braces ({ }). Dictionaries are used for efficient data lookup and representation.",]
    ],
    [
        r"what is tuples?",
        ["Tuples in Python are ordered collections of items enclosed in parentheses (()). They are similar to lists but immutable, meaning their elements cannot be changed after creation. Tuples are commonly used for representing fixed collections of items.",]
    ],
    [
        r"what is tuples",
        ["Tuples in Python are ordered collections of items enclosed in parentheses (()). They are similar to lists but immutable, meaning their elements cannot be changed after creation. Tuples are commonly used for representing fixed collections of items.",]
    ],
    [
        r"define tuples?",
        ["Tuples in Python are ordered collections of items enclosed in parentheses (()). They are similar to lists but immutable, meaning their elements cannot be changed after creation. Tuples are commonly used for representing fixed collections of items.",]
    ],
    [
        r"define tuples",
        ["Tuples in Python are ordered collections of items enclosed in parentheses (()). They are similar to lists but immutable, meaning their elements cannot be changed after creation. Tuples are commonly used for representing fixed collections of items.",]
    ],
    [
        r"what is sets?",
        ["Sets in Python are unordered collections of unique elements enclosed in curly braces ({ }). They don't allow duplicates and support various set operations.",]
    ],
    [
        r"what is sets",
        ["Sets in Python are unordered collections of unique elements enclosed in curly braces ({ }). They don't allow duplicates and support various set operations.",]
    ],
    [
        r"define sets?",
        ["Sets in Python are unordered collections of unique elements enclosed in curly braces ({ }). They don't allow duplicates and support various set operations.",]
    ],
    [
        r"define sets",
        ["Sets in Python are unordered collections of unique elements enclosed in curly braces ({ }). They don't allow duplicates and support various set operations.",]
    ],
    [
        r"what is functions?",
        ["Functions in Python are reusable blocks of code defined using `def`. They perform specific tasks and can optionally return values. Functions help in organizing code, promoting reusability, and making programs easier to manage.",]
    ],
    [
        r"what is functions",
        ["Functions in Python are reusable blocks of code defined using `def`. They perform specific tasks and can optionally return values. Functions help in organizing code, promoting reusability, and making programs easier to manage.",]
    ],
    [
        r"define functions?",
        ["Functions in Python are reusable blocks of code defined using `def`. They perform specific tasks and can optionally return values. Functions help in organizing code, promoting reusability, and making programs easier to manage.",]
    ],
    [
        r"define functions",
        ["Functions in Python are reusable blocks of code defined using `def`. They perform specific tasks and can optionally return values. Functions help in organizing code, promoting reusability, and making programs easier to manage.",]
    ],
    [
        r"what is classes?",
        ["Classes in Python are templates for creating objects. They define properties (attributes) and behaviors (methods) that objects of the class will have. Classes are used to structure code in an object-oriented manner, promoting code reuse and modularity.",]
    ],
    [
        r"what is classes",
        ["Classes in Python are templates for creating objects. They define properties (attributes) and behaviors (methods) that objects of the class will have. Classes are used to structure code in an object-oriented manner, promoting code reuse and modularity.",]
    ],
    [
        r"define classes?",
        ["Classes in Python are templates for creating objects. They define properties (attributes) and behaviors (methods) that objects of the class will have. Classes are used to structure code in an object-oriented manner, promoting code reuse and modularity.",]
    ],
    [
        r"define classes",
        ["Classes in Python are templates for creating objects. They define properties (attributes) and behaviors (methods) that objects of the class will have. Classes are used to structure code in an object-oriented manner, promoting code reuse and modularity.",]
    ],
    [
        r"what is modules?",
        ["Modules in Python are files containing reusable Python code. They can define functions, classes, and variables. Modules help organize code and facilitate reuse across different scripts by using the `import` statement.",]
    ],
    [
        r"what is modules",
        ["Modules in Python are files containing reusable Python code. They can define functions, classes, and variables. Modules help organize code and facilitate reuse across different scripts by using the `import` statement.",]
    ],
    [
        r"define modules?",
        ["Modules in Python are files containing reusable Python code. They can define functions, classes, and variables. Modules help organize code and facilitate reuse across different scripts by using the `import` statement.",]
    ],
    [
        r"define modules",
        ["Modules in Python are files containing reusable Python code. They can define functions, classes, and variables. Modules help organize code and facilitate reuse across different scripts by using the `import` statement.",]
    ],
    [
        r"what is packages?",
        ["Packages in Python are directories containing Python modules, with an added `__init__.py` file. They organize related modules and sub-packages, making it easier to manage and distribute code.",]
    ],
    [
        r"what is packages",
        ["Packages in Python are directories containing Python modules, with an added `__init__.py` file. They organize related modules and sub-packages, making it easier to manage and distribute code.",]
    ],
    [
        r"define packages?",
        ["Packages in Python are directories containing Python modules, with an added `__init__.py` file. They organize related modules and sub-packages, making it easier to manage and distribute code.",]
    ],
    [
        r"define packages",
        ["Packages in Python are directories containing Python modules, with an added `__init__.py` file. They organize related modules and sub-packages, making it easier to manage and distribute code.",]
    ],
    [
        r"what is exceptions?",
        ["Exceptions in Python are errors that disrupt the normal flow of a program. They can be caught and handled using `try` and `except` blocks, allowing for graceful error recovery.",]
    ],
    [
        r"what is exceptions",
        ["Exceptions in Python are errors that disrupt the normal flow of a program. They can be caught and handled using `try` and `except` blocks, allowing for graceful error recovery.",]
    ],
    [
        r"define exceptions?",
        ["Exceptions in Python are errors that disrupt the normal flow of a program. They can be caught and handled using `try` and `except` blocks, allowing for graceful error recovery.",]
    ],
    [
        r"define exceptions",
        ["Exceptions in Python are errors that disrupt the normal flow of a program. They can be caught and handled using `try` and `except` blocks, allowing for graceful error recovery.",]
    ],
    [
        r"define exception handling?",
        ["Exception handling is a programming technique used to manage unexpected errors during program execution. It involves using `try` and `except` blocks to catch and handle errors gracefully, preventing the program from crashing.",]
    ],
    [
        r"define exception handling",
        ["Exception handling is a programming technique used to manage unexpected errors during program execution. It involves using `try` and `except` blocks to catch and handle errors gracefully, preventing the program from crashing.",]
    ],
    [
        r"what is constructor?",
        ["A constructor in Python is a special method named `__init__()` that initializes the attributes of an object when it is created.",]
    ],
    [
        r"what is constructor",
        ["A constructor in Python is a special method named `__init__()` that initializes the attributes of an object when it is created.",]
    ],
    [
        r"what is destructor?",
        ["A destructor in Python is a special method named `__del__()` that is called when an object is about to be destroyed or deleted, allowing you to perform cleanup operations.",]
    ],
    [
        r"what is destructor",
        ["A destructor in Python is a special method named `__del__()` that is called when an object is about to be destroyed or deleted, allowing you to perform cleanup operations.",]
    ],
    [
        r"what is inheritance?",
        ["Inheritance is a mechanism in object-oriented programming that allows a class to inherit properties and behaviors from another class. It allows for code reusability and promotes code organization.",]
    ],
    [
        r"what is inheritance",
        ["Inheritance is a mechanism in object-oriented programming that allows a class to inherit properties and behaviors from another class. It allows for code reusability and promotes code organization.",]
    ],
    [
        r"what is polymorphism?",
        ["Polymorphism is a concept in object-oriented programming that refers to the ability of objects of different classes to be treated as if they were of the same class. It allows for code flexibility and promotes code reuse.",]
    ],
    [
        r"what is polymorphism",
        ["Polymorphism is a concept in object-oriented programming that refers to the ability of objects of different classes to be treated as if they were of the same class. It allows for code flexibility and promotes code reuse.",]
    ],
    [
        r"what is encapsulation?",
        ["Encapsulation is a mechanism in object-oriented programming that restricts access to certain attributes and methods of an object. It allows for code security and data hiding.",]
    ],
    [
        r"what is encapsulation",
        ["Encapsulation is a mechanism in object-oriented programming that restricts access to certain attributes and methods of an object. It allows for code security and data hiding.",]
    ],
    [
        r"what is abstraction?",
        ["Abstraction is a concept in object-oriented programming that refers to the process of hiding the implementation details of an object and exposing only the necessary information to the user. It allows for code flexibility and promotes code reuse.",]
    ],
    [
        r"what is abstraction",
        ["Abstraction is a concept in object-oriented programming that refers to the process of hiding the implementation details of an object and exposing only the necessary information to the user. It allows for code flexibility and promotes code reuse.",]
    ],
    [
        r"what is oop?",
        ["Object-oriented programming (OOP) is a programming paradigm based on the concept of objects, which can contain data and code. It allows for code reuse, modularity, and maintainability.",]
    ],
    [
        r"what is oop",
        ["Object-oriented programming (OOP) is a programming paradigm based on the concept of objects, which can contain data and code. It allows for code reuse, modularity, and maintainability.",]
    ],
    [
        r"what is public access modifiers?",
        ["The public access modifier is the direct opposite of the private access modifier. A class, method or variable can be declared as public and it means that it is accessible from any class. Public access modifier can be likened to a public school where anyone can seek admission and be admitted.",]
    ],
    [
        r"what is private access modifiers?",
        ["The members of a class that are declared private are accessible within the class only, private access modifier is the most secure access modifier. Data members of a class are declared private by adding a double underscore ‘__’ symbol before the data member of that class.", ]
    ],
    [
        r"what is protected access modifiers?",
        ["The members of a class that are declared protected are only accessible to a class derived from it. Data members of a class are declared protected by adding a single underscore ‘_’ symbol before the data member of that class.", ]
    ],
    [
        r"what is string?",
        ["A string is a sequence of characters, like letters, numbers, and symbols, used to represent text in programming. For example, Hello, World! is a string.", ]
    ],
    [
        r"what is composite list?",
        ["A composite list in Python is simply a list that contains other lists as its elements. For example: composite_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]", ]
    ],
    [
        r"what is parameterized constructor?",
        ["A parameterized constructor in Python is a method in a class that accepts parameters to initialize object attributes upon creation.", ]
    ],
    [
        r"what is oop",
        ["Object-oriented programming (OOP) is a programming paradigm based on the concept of objects, which can contain data and code. It allows for code reuse, modularity, and maintainability.", ]
    ],
    [
        r"what is oop",
        ["Object-oriented programming (OOP) is a programming paradigm based on the concept of objects, which can contain data and code. It allows for code reuse, modularity, and maintainability.", ]
    ],
    [
        r"what is flask?",
        ["Flask is a web framework for Python that provides a set of tools and features for building web applications. It is designed to be lightweight, flexible, and easy to use.",]
    ],
    [
        r"what is flask",
        ["Flask is a web framework for Python that provides a set of tools and features for building web applications. It is designed to be lightweight, flexible, and easy to use.",]
    ],
    [
        r"what is numpy?",
        ["NumPy is a library for scientific computing in Python. It provides high-performance multidimensional array objects, and tools for working with these arrays.",]
    ],
    [
        r"what is numpy",
        ["NumPy is a library for scientific computing in Python. It provides high-performance multidimensional array objects, and tools for working with these arrays.",]
    ],
    [
        r"what is pandas?",
        ["Pandas is a library for data analysis and manipulation in Python. It provides data structures and data manipulation tools, including data cleaning, filtering, grouping, and visualization.",]
    ],
    [
        r"what is pandas",
        ["Pandas is a library for data analysis and manipulation in Python. It provides data structures and data manipulation tools, including data cleaning, filtering, grouping, and visualization.",]
    ],
    [
        r"what is matplotlib?",
        ["Matplotlib is a plotting library for Python. It provides a wide range of plotting functions, including line plots, bar plots, scatter plots, and histograms.",]
    ],
    [
        r"what is matplotlib",
        ["Matplotlib is a plotting library for Python. It provides a wide range of plotting functions, including line plots, bar plots, scatter plots, and histograms.",]
    ],
    [
        r"what is django?",
        ["Django is a web framework for Python that provides a set of tools and features for building web applications. It is designed to be lightweight, flexible, and easy to use.",]
    ],
    [
        r"what is django",
        ["Django is a web framework for Python that provides a set of tools and features for building web applications. It is designed to be lightweight, flexible, and easy to use.",]
    ],
    [
        r"(.*) (quit|bye|exit) ?",
        ["Goodbye! Have a great day.",]
    ],
]


# Initialize chatbot
chatbot = Chat(pairs, reflections)
sid = SentimentIntensityAnalyzer()


# Define function to handle user input and chatbot response
def send_message(event=None):
    user_input = entry_box.get()
    entry_box.delete(0, tk.END)  # Clear input box
    sentiment_score = sid.polarity_scores(user_input)
    if sentiment_score['compound'] >= 0.5:
        chat_log.insert(tk.END, "You seem positive!\n")
    elif sentiment_score['compound'] <= -0.5:
        chat_log.insert(tk.END, "You seem negative. Is everything okay?\n")
    else:
        chat_log.insert(tk.END, "Your sentiment is neutral.\n")
    response = chatbot.respond(user_input)
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    chat_log.insert(tk.END, "ChatBot: " + response + "\n")
    chat_log.yview(tk.END)  # Auto-scroll to the bottom


# Create tkinter window
root = tk.Tk()
root.title("PyBot Chat")
root.geometry("400x400")

# Create chat log area
chat_log = scrolledtext.ScrolledText(root, width=50, height=20)
chat_log.pack(expand=True, fill=tk.BOTH)

# Create entry box for user input
entry_box = tk.Entry(root, width=50)
entry_box.bind("<Return>", send_message)  # Bind Enter key to send_message function
entry_box.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.X)

# Create send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Focus entry box for immediate typing
entry_box.focus()

# Start tkinter event loop
root.mainloop()
