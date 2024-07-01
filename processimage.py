import cv2
import numpy as np
import pytesseract
from PIL import Image
import argparse
import os

def adjust_contrast_brightness(image, contrast=1.0, brightness=0):
    """
    Adjusts the contrast and brightness of an image.
    :param image: input image
    :param contrast: contrast factor
    :param brightness: brightness factor
    :return: adjusted image
    """
    return cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)

def scale_image_with_pil(image, target_width, target_height):
    """
    Scales the image using PIL while maintaining aspect ratio and pads it to the target dimensions.
    :param image: input image
    :param target_width: target width
    :param target_height: target height
    :return: scaled and padded image
    """
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    pil_image.thumbnail((target_width, target_height), Image.LANCZOS)
    
    # Create a new image with the target size and paste the resized image onto it
    new_image = Image.new('RGB', (target_width, target_height), (0, 0, 0))
    new_image.paste(pil_image, ((target_width - pil_image.width) // 2, (target_height - pil_image.height) // 2))
    
    return cv2.cvtColor(np.array(new_image), cv2.COLOR_RGB2BGR)

def crop_with_margin(image, x, y, w, h, margin):
    """
    Crops the image with an additional margin.
    :param image: input image
    :param x: x coordinate of the bounding box
    :param y: y coordinate of the bounding box
    :param w: width of the bounding box
    :param h: height of the bounding box
    :param margin: margin to be added around the bounding box
    :return: cropped image
    """
    height, width = image.shape[:2]
    x1 = max(0, x - margin)
    y1 = max(0, y - margin)
    x2 = min(width, x + w + margin)
    y2 = min(height, y + h + margin)
    return image[y1:y2, x1:x2]

# Set up argument parsing
parser = argparse.ArgumentParser(description="Number Plate Detection with OCR")
parser.add_argument('image_path', type=str, help="Path to the image for testing")
args = parser.parse_args()

# Specify the path to tesseract executable if it's not in your PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path if necessary

# Load the image from the specified path
image_path = args.image_path

# Check if the file exists
if not os.path.exists(image_path):
    print(f"Error: The file at path {image_path} does not exist.")
    exit(1)

image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print(f"Error: The image at path {image_path} could not be loaded.")
    exit(1)

# Scale the image using PIL
target_width = 800
target_height = 600
scaled_image = scale_image_with_pil(image, target_width, target_height)

# Convert to grayscale
gray = cv2.cvtColor(scaled_image, cv2.COLOR_BGR2GRAY)

# Create a mask for white portions
_, white_mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)  # White portions

# Find contours in the mask
contours, _ = cv2.findContours(white_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Get the bounding box of the largest contour
x, y, w, h = cv2.boundingRect(contours[0])

# Crop the image using the bounding box with an additional margin
margin = -2  # Adjust the margin as needed
cropped_image = crop_with_margin(scaled_image, x, y, w, h, margin)

# Increase contrast and brightness
contrast = 1.5  # Contrast factor
brightness = 50  # Brightness factor
adjusted_image = adjust_contrast_brightness(cropped_image, contrast=contrast, brightness=brightness)

# Convert adjusted image to PIL Image
adjusted_pil_image = Image.fromarray(cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2RGB))

# Use Tesseract OCR to recognize characters in the adjusted image
ocr_result = pytesseract.image_to_string(adjusted_pil_image, lang='traindata_all')

# Display the original, mask, cropped, and adjusted images
cv2.imshow('Original Image', image)
cv2.imshow('Scaled Image', scaled_image)
cv2.imshow('White Mask', white_mask)
cv2.imshow('Cropped Image', cropped_image)
cv2.imshow('Adjusted Image', adjusted_image)

# Print the OCR result
print("OCR Result:")
print(ocr_result)

cv2.waitKey(0)
cv2.destroyAllWindows()
