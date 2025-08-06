from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# Create the main window
root = Tk()
root.title("Image Converter with Preview")
root.geometry("400x450")
root.config(bg='white')

selected_file = None

# Upload image function
def upload_image():
    global selected_file
    selected_file = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if selected_file:
        file_label.config(text=f"Selected Image: {os.path.basename(selected_file)}")

        # Show preview
        img = Image.open(selected_file)
        img.thumbnail((200, 200))  # Resize preview
        tk_image = ImageTk.PhotoImage(img)
        image_preview.config(image=tk_image)
        image_preview.image = tk_image

# Convert image function
def convert_image():
    if selected_file is None:
        messagebox.showerror("Error", "No image selected!")
        return

    selected_format = format_var.get()
    save_path = filedialog.asksaveasfilename(
        defaultextension=f".{selected_format}",
        filetypes=[(f"{selected_format.upper()} files", f"*.{selected_format}")]
    )

    if save_path:
        try:
            img = Image.open(selected_file)
            img.save(save_path, selected_format.upper())
            messagebox.showinfo("Success", f"Image converted and saved as {save_path}")
        except Exception as e:
            messagebox.showerror("Conversion Failed", str(e))

# GUI Widgets
upload_btn = Button(root, text="Upload Image", command=upload_image)
upload_btn.pack(pady=10)

file_label = Label(root, text="No image selected", bg="white")
file_label.pack()

image_preview = Label(root, bg="white")
image_preview.pack(pady=10)

format_var = StringVar()
format_var.set("jpg")  # Default format

format_menu = OptionMenu(root, format_var, "jpg", "png", "bmp", "gif")
format_menu.pack(pady=10)

convert_btn = Button(root, text="Convert", command=convert_image)
convert_btn.pack(pady=20)

root.mainloop()
