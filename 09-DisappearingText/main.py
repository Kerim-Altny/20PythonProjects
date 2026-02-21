import tkinter as tk


WAIT_TIME = 5  
timer = None

def erase_text():
    
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, "")
    timer_label.config(text="Time's Up! You lost everything 😈", fg="red")

def reset_timer(event):
 
    global timer
    if timer:
        window.after_cancel(timer)

    timer_label.config(text="Keep writing...", fg="green")
    
    timer = window.after(WAIT_TIME * 1000, erase_text)


window = tk.Tk()
window.title("Disappearing Text App")
window.config(padx=50, pady=50)


title_label = tk.Label(text="Don't Stop Writing!", font=("Arial", 24, "bold"))
title_label.pack()


subtitle_label = tk.Label(text=f"If you stop for {WAIT_TIME} seconds, all progress will be lost.", font=("Arial", 12))
subtitle_label.pack(pady=10)


timer_label = tk.Label(text="Type to start...", font=("Arial", 14), fg="grey")
timer_label.pack(pady=5)


text_area = tk.Text(window, height=15, width=60, font=("Arial", 14))
text_area.pack(pady=20)
text_area.focus()


window.bind("<Key>", reset_timer)

window.mainloop()