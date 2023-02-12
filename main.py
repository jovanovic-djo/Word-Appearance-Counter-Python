from tkinter import *
from collections import Counter
import string

def count_words():
    text = input_field.get("1.0", END)
    words = [word for word in text.split() if not word[0] in string.punctuation]
    word_counts = Counter(words)
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    output_field.delete("1.0", END)
    output_field.insert(END, "Total number of different words: " + str(len(word_counts)) + "\n\n")
    for word, count in sorted_word_counts:
        output_field.insert(END, word + ": " + str(count) + "\n")

def sort_alphabetically():
    text = input_field.get("1.0", END)
    words = [word for word in text.split() if not word[0] in string.punctuation]
    word_counts = Counter(words)
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[0])
    output_field.delete("1.0", END)
    output_field.insert(END, "Total number of different words: " + str(len(word_counts)) + "\n\n")
    for word, count in sorted_word_counts:
        output_field.insert(END, word + ": " + str(count) + "\n")

root = Tk()
root.geometry("350x400")
root.config(bg='#1c1c1e')

input_field = Text(root, height=10, width=30, bg='#2b2b2e', fg='#ffffff')
input_field.pack()

output_field = Text(root, height=10, width=30, bg='#2b2b2e', fg='#ffffff')
output_field.pack()

count_button = Button(root, text="Count words", command=count_words, bg='#3b3b3e', fg='#ffffff')
count_button.pack()

sort_alphabetically_button = Button(root, text="Sort alphabetically", command=sort_alphabetically, bg='#3b3b3e', fg='#ffffff')
sort_alphabetically_button.pack()

root.mainloop()
