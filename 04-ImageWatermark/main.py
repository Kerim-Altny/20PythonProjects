from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont


window = Tk()
window.title("Image Watermarking App")
window.geometry("600x800")
window.config(padx=50, pady=50) 


label = Label(text="Watermark Your Images", font=("Arial", 24, "bold"))
label.pack(pady=20)


canvas = Canvas(width=400, height=300, bg="gray")
canvas.pack()


original_image = None
img_preview = None
watermarked_image = None

def select_image():
    global original_image, img_preview
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        original_image = Image.open(file_path)
        preview_copy = original_image.copy()
        preview_copy.thumbnail((400, 300))
        img_preview = ImageTk.PhotoImage(preview_copy)
        canvas.create_image(200, 150, image=img_preview)

def add_watermark():
    global original_image, watermarked_image, img_preview
    if original_image:
        watermarked_image = original_image.copy()
        draw = ImageDraw.Draw(watermarked_image)
        text = "© KerimAltny"
        draw.text((20, 20), text, fill=(255, 255, 255))
        preview_copy = watermarked_image.copy()
        preview_copy.thumbnail((400, 300))
        img_preview = ImageTk.PhotoImage(preview_copy)
        canvas.create_image(200, 150, image=img_preview)
        messagebox.showinfo("Success", "Watermark applied!")
    else:
        messagebox.showwarning("Warning", "Please select an image first!")

def save_image():
    global watermarked_image
    if watermarked_image:
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            watermarked_image.save(path)
            messagebox.showinfo("Saved", "Successfully saved!")


select_button = Button(text="Select Image", command=select_image)
select_button.pack(pady=10)

add_button = Button(text="Add Watermark", command=add_watermark)
add_button.pack(pady=10)

save_button = Button(text="Save Image", command=save_image)
save_button.pack(pady=10)

window.mainloop()