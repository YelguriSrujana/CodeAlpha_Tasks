from tkinter import *

translations = {
    "hello": "namaste",
    "good morning": "subhodayam",
    "thank you": "dhanyavadalu"
}

def translate():
    text = entry.get().lower()
    result.config(text=translations.get(text, "Translation not found"))

root = Tk()
root.title("Simple Translator")

entry = Entry(root, width=40)
entry.pack(pady=10)

Button(root, text="Translate", command=translate).pack()

result = Label(root, text="")
result.pack(pady=10)

root.mainloop()