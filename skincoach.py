import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Function to recommend skincare routine based on skin type
def recommend_skincare():
    while True:
        skin_type = var.get()
        if skin_type == 1:  # Dry skin
            routine = "Go for Products containing Hyaluronic acid\n1. Use a gentle cleanser\n2. Apply a hydrating moisturizer \n3. Use a rich night cream\n4. Products like\n\t i.pond's Hydra light face wash\n\t ii.lakme peach milk light moisturizer\n\t iii.lakme peach milk light moisturizer\n5.End with spf 50 sunscreen"
        elif skin_type == 2:  # Oily skin
            routine = " Go for products containing salycilic acid,niacinamide\n1. Use a foaming cleanser\n2. Apply an oil-free moisturizer \n3. Use a clay mask once a week\n4.Products like\n\t i. MamaEarth tea tree face wash\n\t ii.mamaearth tea tree moisturizer\n\t iii.mamearth  C3 face mask\n5.End with spf 50 sunscreen "
        elif skin_type == 3:  # Combination skin
            routine = "Go For containing Glycolic acid,niacinamide,Hyaluronic acid\n1. Use a gentle cleanser\n2. Apply a lightweight moisturizer\n3. Use a balancing toner\n4.products like\n\t i.cetaphil gentle skin Cleanser\n\tii. Cetaphil  Daily Advance Ultra Hydrating Lotion\n5.End with spf 50 sunscreen"
        elif skin_type == 4:  # Sensitive skin
            routine = "go for ingredients like hyaluronic acid,\n1. Use a fragrance-free cleanser\n2. Apply a gentle moisturizer\n3. Use sunscreen with SPF 30+\n4.Products like\n\t i.pond's Hydra light face wash\n\t ii.lakme peach milk light moisturizer\n\t iii.lakme peach milk light moisturizer "
        elif skin_type == 5:  # normal skin
            routine = "go for ingredients like hyaluronic acid, Vitamin C\n 1. Use a fragrance-free cleanser\n2. Apply a gentle moisturizer\n3. Use sunscreen with SPF 30+\n4.Products like\n\t i.cetaphil gentle skin\n\t ii.mamearth Vitamin C day cream \n\t iii.lakme peach milk light moisturizer"   
        else:
            routine = "Please select a skin type."

    # Update the label text with recommended routine
        result_label.config(text=routine)
        window.update()  

# Create main tkinter window
window = tk.Tk()
#window.geometry("600x600")
window.title("Skin Coach")
background_image = Image.open("background.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas to place the background image
canvas = tk.Canvas(window, width=background_image.width, height=background_image.height)
canvas.pack(fill=tk.BOTH, expand=True)
canvas.create_image(0, 0, image=background_photo, anchor=tk.NW)

# Create a label for skin type selection
label=tk.Label(window,text="Welcome to Skin Coach and get glowing skin",font=("Helvetica",22))
label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
select_label = tk.Label(window, text="Select your skin type:", font=("Helvetica", 16))
select_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

# Create a tkinter IntVar to store the selected skin type
var = tk.IntVar()

# Create radio buttons for skin type selection
skin_types = [("Dry Skin", 1), ("Oily Skin", 2), ("Combination Skin", 3), ("Sensitive Skin", 4),("Normal Skin",5)]
for skin, val in skin_types:
    skin_radio = tk.Radiobutton(window, text=skin, variable=var, value=val)
    skin_radio.pack(anchor=tk.W)
    skin_radio.place(relx=0.5, rely=0.1 + val * 0.1, anchor=tk.CENTER)

# Create a button to recommend skincare routine
recommend_button = tk.Button(window, text="Recommend Skincare", command=recommend_skincare)
recommend_button.pack()
recommend_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Create a label to display recommended routine
result_label = tk.Label(window, text="", font=("Helvetica", 14), wraplength=400, justify=tk.LEFT)
result_label.pack()
result_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)


# Run the tkinter event loop
window.mainloop()
