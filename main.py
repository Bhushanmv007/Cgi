import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np

def load_image():
    global original_image
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        if image is not None:
            original_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            display_image(original_image, original_panel)

def display_image(image, panel):
    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image)
    panel.config(image=image)
    panel.image = image

def apply_filter_or_enhancement():
    global original_image
    if original_image is None:
        messagebox.showerror("Error", "No image loaded")
        return

    try:
        intensity = float(intensity_slider.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid intensity value")
        return

    if intensity < 0 or intensity > 5:
        messagebox.showerror("Error", "Intensity must be between 0 and 5")
        return

    option = option_menu_var.get()

    if option == "Gaussian Blur":
        processed_image = apply_gaussian_blur(original_image, intensity)
    elif option == "Median Blur":
        processed_image = apply_median_blur(original_image, intensity)
    elif option == "Sharpen":
        processed_image = apply_sharpen(original_image, intensity)
    elif option == "Edge Detection":
        processed_image = apply_edge_detection(original_image, intensity)
    elif option == "Noise Reduction":
        processed_image = apply_noise_reduction(original_image, intensity)
    elif option == "Brightness Adjustment":
        processed_image = adjust_brightness(original_image, intensity)
    elif option == "Contrast Adjustment":
        processed_image = adjust_contrast(original_image, intensity)
    elif option == "Histogram Equalization":
        processed_image = histogram_equalization(original_image, intensity)
    elif option == "Saturation Adjustment":
        processed_image = adjust_saturation(original_image, intensity)
    elif option == "Gamma Correction":
        processed_image = gamma_correction(original_image, intensity)

    display_image(processed_image, processed_panel)

def apply_gaussian_blur(image, intensity=1):
    ksize = int(15 * intensity)
    if ksize % 2 == 0:
        ksize += 1
    return cv2.GaussianBlur(image, (ksize, ksize), 0)

def apply_median_blur(image, intensity=1):
    ksize = int(15 * intensity)
    if ksize % 2 == 0:
        ksize += 1
    return cv2.medianBlur(image, ksize)

def apply_sharpen(image, intensity=1):
    kernel = np.array([[0, -1, 0], 
                      [-1, 5 + intensity, -1],
                      [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)

def apply_edge_detection(image, intensity=1):
    return cv2.Canny(image, 100 * intensity, 200 * intensity)

def apply_noise_reduction(image, intensity=1):
    return cv2.fastNlMeansDenoisingColored(image, None, 10 * intensity, 10 * intensity, 7, 21)

def adjust_brightness(image, intensity=1):
    value = int(30 * intensity)
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, value)
    v = np.clip(v, 0, 255)
    final_hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2RGB)

def adjust_contrast(image, intensity=1):
    alpha = 1 + intensity
    return cv2.convertScaleAbs(image, alpha=alpha, beta=0)

def histogram_equalization(image, intensity=1):
    img_yuv = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)
    img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
    if intensity > 1:
        for _ in range(int(intensity) - 1):
            img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
    return cv2.cvtColor(img_yuv, cv2.COLOR_YUV2RGB)

def adjust_saturation(image, intensity=1):
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(hsv)
    s = cv2.multiply(s, intensity)
    s = np.clip(s, 0, 255)
    final_hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2RGB)

def gamma_correction(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in range(256)]).astype("uint8")
    return cv2.LUT(image, table)

# Main Application
root = tk.Tk()
root.title("Image Processing App")

# Global variables
original_image = None

# UI Elements
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

load_button = tk.Button(frame, text="Load Image", command=load_image)
load_button.grid(row=0, column=0, padx=5, pady=5)

option_menu_var = tk.StringVar()
option_menu_var.set("Gaussian Blur")
options = [
    "Gaussian Blur", "Median Blur", "Sharpen", "Edge Detection", "Noise Reduction",
    "Brightness Adjustment", "Contrast Adjustment", "Histogram Equalization",
    "Saturation Adjustment", "Gamma Correction"
]
option_menu = ttk.OptionMenu(frame, option_menu_var, *options)
option_menu.grid(row=0, column=1, padx=5, pady=5)

intensity_slider = tk.Scale(frame, from_=0, to_=5, resolution=0.1, orient=tk.HORIZONTAL, label="Intensity")
intensity_slider.grid(row=0, column=2, padx=5, pady=5)

apply_button = tk.Button(frame, text="Apply", command=apply_filter_or_enhancement)
apply_button.grid(row=0, column=3, padx=5, pady=5)

original_panel = tk.Label(frame, text="Original Image")
original_panel.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

processed_panel = tk.Label(frame, text="Processed Image")
processed_panel.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()
