from tkinter import *
from tkinter import scrolledtext

def count_words():
    input_text = input_field.get("1.0", "end-1c")
    words = input_text.lower().split()
    word_count = {}

    for word in words:
        if word.isalpha():
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    result = ""

    result = "Total number of different words: " + str(len(word_count)) + "\n\n"
    for word, count in sorted_words:
        result += f"{word}: {count}\n"

    output_field.delete("1.0", END)
    output_field.insert(END, result)

def sort_alphabetically():
    input_text = input_field.get("1.0", "end-1c")
    words = input_text.lower().split()
    word_count = {}

    for word in words:
        if word.isalpha():
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    sorted_words = sorted(word_count.items(), key=lambda x: x[0])
    result = ""

    result = "Total number of different words: " + str(len(word_count)) + "\n\n"
    for word, count in sorted_words:
        result += f"{word}: {count}\n"

    output_field.delete("1.0", END)
    output_field.insert(END, result)

root = Tk()
root.geometry("350x450")
root.title("Word Counter")
root.config(bg='#1c1c1e')

input_field = scrolledtext.ScrolledText(root, height=10, width=40, bg='#2b2b2e', fg='#ffffff')
input_field.pack(padx=10, pady=10)

output_field = scrolledtext.ScrolledText(root, height=10, width=40, bg='#2b2b2e', fg='#ffffff')
output_field.pack(padx=10, pady=5)

sort_by_count_button = Button(root, text="Sort by count", command=count_words, bg='#3b3b3e', fg='#ffffff')
sort_by_count_button.pack(pady=5)

sort_alphabetically_button = Button(root, text="Sort alphabetically", command=sort_alphabetically, bg='#3b3b3e', fg='#ffffff')
sort_alphabetically_button.pack(pady=5)

root.mainloop()
