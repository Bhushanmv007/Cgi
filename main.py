import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(image_path):
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError("Image not found or path is incorrect")
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def display_images(original, processed, title):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(processed)
    plt.title(title)
    plt.axis('off')

    plt.show()

def apply_gaussian_blur(image):
    return cv2.GaussianBlur(image, (15, 15), 0)

def apply_median_blur(image):
    return cv2.medianBlur(image, 15)

def apply_sharpen(image):
    kernel = np.array([[0, -1, 0], 
                      [-1, 5,-1],
                      [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)

def apply_edge_detection(image):
    return cv2.Canny(image, 100, 200)

def apply_noise_reduction(image):
    return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

def adjust_brightness(image, value=30):
    """Adjust brightness of the image."""
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, value)
    v = np.clip(v, 0, 255)
    final_hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2RGB)

def adjust_contrast(image, alpha=1.3):
    """Adjust contrast of the image."""
    return cv2.convertScaleAbs(image, alpha=alpha, beta=0)

def histogram_equalization(image):
    """Apply histogram equalization to the image."""
    img_yuv = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)
    img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
    return cv2.cvtColor(img_yuv, cv2.COLOR_YUV2RGB)

def filter_menu(image):
    print("Choose a filter to apply:")
    print("1: Gaussian Blur")
    print("2: Median Blur")
    print("3: Sharpen")
    print("4: Edge Detection")
    print("5: Noise Reduction")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        return

    if choice == 1:
        processed_image = apply_gaussian_blur(image)
        display_images(image, processed_image, "Gaussian Blur")
    elif choice == 2:
        processed_image = apply_median_blur(image)
        display_images(image, processed_image, "Median Blur")
    elif choice == 3:
        processed_image = apply_sharpen(image)
        display_images(image, processed_image, "Sharpen")
    elif choice == 4:
        processed_image = apply_edge_detection(image)
        display_images(image, processed_image, "Edge Detection")
    elif choice == 5:
        processed_image = apply_noise_reduction(image)
        display_images(image, processed_image, "Noise Reduction")
    else:
        print("Invalid choice. Please select a valid option.")

def enhancement_menu(image):
    print("Choose an enhancement to apply:")
    print("1: Brightness Adjustment")
    print("2: Contrast Adjustment")
    print("3: Histogram Equalization")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
        return

    if choice == 1:
        value = int(input("Enter brightness adjustment value (e.g., 30 or -30): "))
        processed_image = adjust_brightness(image, value)
        display_images(image, processed_image, "Brightness Adjustment")
    elif choice == 2:
        alpha = float(input("Enter contrast adjustment factor (e.g., 1.3): "))
        processed_image = adjust_contrast(image, alpha)
        display_images(image, processed_image, "Contrast Adjustment")
    elif choice == 3:
        processed_image = histogram_equalization(image)
        display_images(image, processed_image, "Histogram Equalization")
    else:
        print("Invalid choice. Please select a valid option.")

def main():
    image_path = input("Enter the path to the image: ")
    print(f"Loading image from: {image_path}")
    
    image = load_image(image_path)
    if image is None:
        return
    
    print("Choose an operation:")
    print("1: Filter")
    print("2: Enhancement")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        return

    if choice == 1:
        filter_menu(image)
    elif choice == 2:
        enhancement_menu(image)
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
