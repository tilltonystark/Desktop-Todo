import tkinter as tk
from tkinter import filedialog
from PIL import Image

# Function to set the desktop wallpaper
def set_wallpaper(file_path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, file_path, 3)

# Function to handle file selection
def select_files():
    files = filedialog.askopenfilenames(title="Select Images", filetypes=(("Image files", "*.jpg *.jpeg *.png"), ("all files", "*.*")))
    if files:
        for file in files:
            image = Image.open(file)
            image = image.resize((1920, 1080))  # Adjust to the resolution of your desktop
            image.save(file)  # Overwrite the original image with the correct resolution
        set_wallpaper(files[0])  # Set the first selected image as the wallpaper

# GUI setup
root = tk.Tk()
root.title("Desktop Wallpaper Changer")

select_button = tk.Button(root, text="Select Photos", command=select_files)
select_button.pack()

root.mainloop()
