from ultralytics import YOLO
import argparse
import cv2
import matplotlib.pyplot as plt
import os

# Set up argument parsing
parser = argparse.ArgumentParser(description="Number Plate Detection with YOLO")
parser.add_argument('image_path', type=str, help="Path to the image for testing")
args = parser.parse_args()

# Load the trained model (update the path if needed)
model = YOLO('../yolo model/yolov8.pt')

# Path to the image for testing from command line argument
image_path = args.image_path
results = model.predict(source=image_path, save=True, save_txt=True)

# Read the image using OpenCV
image = cv2.imread(image_path)

# Create a directory to save cropped images
cropped_dir = 'E:/Project/Collab/Number Plate Detection/cropped_objects'
os.makedirs(cropped_dir, exist_ok=True)

# Iterate over the results
for result in results:
    for box in result.boxes:
        # Get coordinates
        x1, y1, x2, y2 = map(int, box.xyxy[0])
       
        # Get label
        label = result.names[int(box.cls[0])]
        # Draw the bounding box
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 255), 2)
        # Put the label
        cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

        # Crop the detected object
        cropped_img = image[y1:y2, x1:x2]

        # Save the cropped image
        cropped_img_path = os.path.join(cropped_dir, f'{label}_{x1}_{y1}.jpg')
        cv2.imwrite(cropped_img_path, cropped_img)
        print(f'Cropped image saved to: {cropped_img_path}')

# Convert BGR image to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image
plt.imshow(cropped_img)
plt.axis('off')
plt.show()