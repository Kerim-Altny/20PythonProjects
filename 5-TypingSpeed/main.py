from tkinter import *
import random


TIME_LIMIT = 60
words = []
current_word_index = 0
correct_word_count = 0
wrong_word_count = 0
time_left = TIME_LIMIT
game_running = False


try:
    with open("words.txt", "r", encoding="utf-8") as file:
        all_content = file.read().split()
        words = random.sample(all_content, min(len(all_content), 300))
except FileNotFoundError:
    words = ["text", "file", "not", "found", "create", "words.txt"]




def update_word_display():
    global current_word_index
    current=words[current_word_index]
    upcoming = " ".join(words[current_word_index+1:current_word_index+6])

    label_current_word.config(state="normal")
    label_current_word.delete("1.0", END)
    label_current_word.insert("1.0", current)
    label_current_word.tag_remove("correct", "1.0", "end")
    label_current_word.tag_remove("wrong", "1.0", "end")
    label_current_word.tag_add("center", "1.0", "end")
    label_current_word.config(state="disabled")
    label_upcoming_words.config(text=upcoming)
    label_score.config(text=f"Correct: {correct_word_count} | Wrong: {wrong_word_count}")


def start_timer():
    global time_left, game_running
    if time_left > 0:
        time_left -= 1
        label_timer.config(text=f"Time: {time_left}s")
        window.after(1000, start_timer)
    else:
        finish_test()


def check_char(event):
    global game_running
    typed_content = entry.get().lstrip()
    if not typed_content:
        label_current_word.config(state="normal")
        label_current_word.tag_remove("correct", "1.0", "end")
        label_current_word.tag_remove("wrong", "1.0", "end")
        label_current_word.config(state="disabled")
        return
    if not game_running:
        game_running = True
        start_timer()
    target_word = words[current_word_index]
    label_current_word.config(state="normal")
    label_current_word.tag_remove("correct", "1.0", "end")
    label_current_word.tag_remove("wrong", "1.0", "end")

    for i in range (len(typed_content)):
        if i< len(target_word):
            start_index = f"1.{i}"
            end_index = f"1.{i + 1}"
            if typed_content[i] == target_word[i]:
                label_current_word.tag_add("correct", start_index, end_index)
            else:
                label_current_word.tag_add("wrong", start_index, end_index)
    label_current_word.config(state="disabled")


def check_word(event):
    global current_word_index, correct_word_count, wrong_word_count
    if not game_running:
        return

    typed_word = entry.get().strip()
    target_word = words[current_word_index]
    if typed_word == target_word:
        correct_word_count += 1
    else:
        wrong_word_count += 1
    current_word_index += 1

    entry.delete(0, END)
    update_word_display()
    return "break"



def finish_test():
    global game_running
    game_running = False
    entry.config(state="disabled")
    label_score.config(text=f"FINAL WPM: {correct_word_count}")



window = Tk()
window.title("Typing Speed Test")
window.geometry("800x500")
window.config(padx=40, pady=40, bg="#f5f6fa")


header_frame = Frame(window, bg="#f5f6fa")
header_frame.pack(fill="x")

label_score = Label(header_frame, text="Correct: 0 | Wrong: 0", font=("Arial", 12, "bold"), bg="#f5f6fa")
label_score.pack(side="left")

label_timer = Label(header_frame, text=f"Time: {TIME_LIMIT}s", font=("Arial", 12, "bold"), fg="#e84118", bg="#f5f6fa")
label_timer.pack(side="right")


label_current_word = Text(window, font=("Consolas", 50, "bold"), height=1, width=20,
                          bg="#f5f6fa", bd=0, highlightthickness=0, state="disabled")
label_current_word.tag_configure("center", justify='center')
label_current_word.tag_configure("correct", foreground="#4cd137")
label_current_word.tag_configure("wrong", foreground="#e84118")
label_current_word.pack(pady=(80, 5))

label_upcoming_words = Label(text="", font=("Consolas", 18), fg="#7f8c8d", bg="#f5f6fa")
label_upcoming_words.pack(pady=10)


entry = Entry(font=("Arial", 22), justify="center", bd=2, relief="flat")
entry.pack(pady=40, ipady=10)
entry.focus()


update_word_display()

entry.bind("<KeyRelease>", check_char)
entry.bind("<space>", check_word)

window.mainloop()