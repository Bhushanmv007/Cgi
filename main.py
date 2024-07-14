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
    """Adjust saturation of the image."""
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(hsv)
    s = cv2.multiply(s, intensity)
    s = np.clip(s, 0, 255)
    final_hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2RGB)

def gamma_correction(image, gamma=1.0):
    """Apply gamma correction to the image.
    
    Parameters:
    gamma (float): Gamma correction factor. 1.0 means no change.
    """
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in range(256)]).astype("uint8")
    return cv2.LUT(image, table)

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
    
    try:
        intensity = float(input("Enter the intensity (0 to 5): "))
        if intensity < 0 or intensity > 5:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 5.")
        return

    if choice == 1:
        processed_image = apply_gaussian_blur(image, intensity)
        display_images(image, processed_image, "Gaussian Blur")
    elif choice == 2:
        processed_image = apply_median_blur(image, intensity)
        display_images(image, processed_image, "Median Blur")
    elif choice == 3:
        processed_image = apply_sharpen(image, intensity)
        display_images(image, processed_image, "Sharpen")
    elif choice == 4:
        processed_image = apply_edge_detection(image, intensity)
        display_images(image, processed_image, "Edge Detection")
    elif choice == 5:
        processed_image = apply_noise_reduction(image, intensity)
        display_images(image, processed_image, "Noise Reduction")
    else:
        print("Invalid choice. Please select a valid option.")

def enhancement_menu(image):
    print("Choose an enhancement to apply:")
    print("1: Brightness Adjustment")
    print("2: Contrast Adjustment")
    print("3: Histogram Equalization")
    print("4: Saturation Adjust")
    print("5: Gamma correction")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
        return

    try:
        intensity = float(input("Enter the intensity (0 to 5): "))
        if intensity < 0 or intensity > 5:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 5.")
        return

    if choice == 1:
        processed_image = adjust_brightness(image, intensity)
        display_images(image, processed_image, "Brightness Adjustment")
    elif choice == 2:
        processed_image = adjust_contrast(image, intensity)
        display_images(image, processed_image, "Contrast Adjustment")
    elif choice == 3:
        processed_image = histogram_equalization(image, intensity)
        display_images(image, processed_image, "Histogram Equalization")
    elif choice == 4:
        processed_image = adjust_saturation(image, intensity)
        display_images(image, processed_image, "Adjusted Saturation")
    elif choice == 5:
        processed_image = gamma_correction(image, intensity)
        display_images(image, processed_image, "Adjusted Saturation")

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
        print("Invalid input. Please enter 1 or 2.")
        return

    if choice == 1:
        filter_menu(image)
    elif choice == 2:
        enhancement_menu(image)
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
