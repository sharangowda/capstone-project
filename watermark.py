import tkinter as tk 
from tkinter import filedialog, messagebox 
from PIL import Image, ImageDraw, ImageFont, ImageTk 



class WatermarkApp: 
    def __init__(self, root): 
        self.root = root 
        self.root.title("Image Watermarker") 
        self.canvas = tk.Canvas(root, width=500, height=500, bg="white") 
        self.canvas.pack() 
        self.btn_upload = tk.Button(root, text="Upload Image", command=self.upload_image) 
        self.btn_upload.pack(pady=10) 
        self.btn_watermark = tk.Button(root, text="Add Watermark", command=self.add_watermark) 
        self.btn_watermark.pack(pady=5) 
        self.btn_save = tk.Button(root, text="Save Watermarked Image", command=self.save_image)
        self.btn_save.pack(pady=5) 
        self.image_path = None 
        self.watermark_text = "Watermark" 
        self.watermark_font = ImageFont.load_default() 
        self.watermark_position = (10, 10) 
        self.watermark_opacity = 128 
    
    def upload_image(self): 
        self.image_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]) 
        if self.image_path: 
            self.image = Image.open(self.image_path) 
            self.display_image() 
    
    def display_image(self): 
        self.image.thumbnail((400, 300)) 
        self.photo = ImageTk.PhotoImage(self.image) 
        # Use ImageTk.PhotoImage to create PhotoImage object 
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo) 
    
    def add_watermark(self): 
        if self.image_path: 
            self.image_with_watermark = self.image.copy() 
            draw = ImageDraw.Draw(self.image_with_watermark) 
            draw.text(self.watermark_position, self.watermark_text, fill=(255, 255, 255, self.watermark_opacity), font=self.watermark_font) 
            self.display_image_with_watermark() 
    
    def display_image_with_watermark(self): 
        self.image_with_watermark.thumbnail((400, 300)) 
        self.photo_with_watermark = ImageTk.PhotoImage(self.image_with_watermark) 
        # Use ImageTk.PhotoImage to create PhotoImage object 
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_with_watermark) 
    
    def save_image(self): 
        if self.image_path: 
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")]) 
        if save_path: 
            self.image_with_watermark.save(save_path) 
            messagebox.showinfo("Success", "Watermarked image saved successfully!") 

root = tk.Tk() 
app = WatermarkApp(root) 
root.mainloop()