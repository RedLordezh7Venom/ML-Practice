import os
from PIL import Image
import random

def augment_image(image_path, output_path):
    # Open an image file
    with Image.open(image_path) as img:
        # Randomly choose an augmentation
        augmentations = [
            lambda img: img.rotate(random.randint(10, 350)),  # Rotation
            lambda img: img.transpose(Image.FLIP_LEFT_RIGHT),  # Horizontal flip
            lambda img: img.transpose(Image.FLIP_TOP_BOTTOM),  # Vertical flip
            lambda img: img.resize((int(img.width * random.uniform(0.8, 1.2)),
                                     int(img.height * random.uniform(0.8, 1.2))), Image.ANTIALIAS),  # Resize
            lambda img: img.crop((10, 10, img.width - 10, img.height - 10)),  # Random crop
            lambda img: img.filter(ImageFilter.GaussianBlur(radius=random.uniform(0, 2)))  # Blur
        ]

        # Apply a random augmentation
        augmented_img = random.choice(augmentations)(img)
        
        # Save the augmented image
        augmented_img.save(output_path)

# Example usage
input_dir = 'path/to/train/'  # Example directory 
output_dir = 'path/to/augmented/'  #Example output directory

os.makedirs(output_dir, exist_ok=True)

# Loop through images in the directory
for filename in os.listdir(input_dir):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, f'aug_{filename}')
        augment_image(input_path, output_path)
