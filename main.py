import tkinter as tk
from collections import Counter

def count_words():
    text = text_input.get("1.0", tk.END)
    words = text.split()
    word_counts = Counter(words)
    result = "Word Counts\n"
    result += "-" * 20 + "\n"
    for word, count in word_counts.items():
        if len(word) > 15:
            result += f"{word[:15]}-\n{word[15:]}: {count}\n"
        else:
            result += f"{word}: {count}\n"
    result += "-" * 20 + "\n"
    result += f"Total Different Words: {len(word_counts)}"
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, result)
    result_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Word Counter")
root.config(bg="#1c1c1e")

input_frame = tk.Frame(root, bg="#1c1c1e")
input_frame.pack(pady=20)

result_frame = tk.Frame(root, bg="#1c1c1e")
result_frame.pack(pady=20)

text_label = tk.Label(input_frame, text="Enter Text:", bg="#1c1c1e", fg="white", font=("Helvetica", 14))
text_label.pack(pady=5)

text_input = tk.Text(input_frame, height=10, width=40, font=("Helvetica", 12), bg="#262629", fg="white")
text_input.pack(pady=5)

count_button = tk.Button(input_frame, text="Count Words", command=count_words, bg="#4d79ff", fg="white", font=("Helvetica", 12))
count_button.pack(pady=20)

sort_label = tk.Label(result_frame, text="Sort By:", bg="#1c1c1e", fg="white", font=("Helvetica", 14))
sort_label.pack(pady=5)

sort_var = tk.StringVar(value="Alphabetical")
sort_dropdown = tk.OptionMenu(result_frame, sort_var, "Alphabetical", "Appearance")
sort_dropdown.config(bg="#262629", fg="white", font=("Helvetica", 12))
sort_dropdown.pack(pady=5)

scrollbar = tk.Scrollbar(result_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

result_text = tk.Text(result_frame, height=15, width=40, yscrollcommand=scrollbar.set, bg="#262629", fg="white", font=("Helvetica", 12), state=tk.DISABLED)
result_text.pack()

scrollbar.config(command=result_text.yview)

root.mainloop()

