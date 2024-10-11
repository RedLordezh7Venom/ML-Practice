import os
import cv2
import numpy as np
import random

def augment_image(image_path, output_path):
    img = cv2.imread(image_path)

    # Randomly choose an augmentation
    augmentations = [
        lambda img: cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE),  # Rotate 90 degrees clockwise
        lambda img: cv2.flip(img, 1),  # Horizontal flip
        lambda img: cv2.flip(img, 0),  # Vertical flip
        lambda img: cv2.resize(img, None, fx=random.uniform(0.8, 1.2), fy=random.uniform(0.8, 1.2)),  # Resize
        lambda img: img[10:img.shape[0]-10, 10:img.shape[1]-10],  # Random crop
        lambda img: cv2.GaussianBlur(img, (5, 5), random.uniform(0, 2))  # Blur
    ]

    # Apply a random augmentation
    augmented_img = random.choice(augmentations)(img)

    # Save the augmented image
    cv2.imwrite(output_path, augmented_img)

# Example usage
input_dir = 'path/to/train/'  # Change to your directory
output_dir = 'path/to/augmented/'  # Change to your output directory

os.makedirs(output_dir, exist_ok=True)

# Loop through images in the directory
for filename in os.listdir(input_dir):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, f'aug_{filename}')
        augment_image(input_path, output_path)
