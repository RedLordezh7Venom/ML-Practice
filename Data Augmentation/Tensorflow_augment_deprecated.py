import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define the augmentation
datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Load your data
train_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
    'path/to/train',  # Directory containing the training images
    target_size=(150, 150),  # Resize images
    batch_size=32,
    class_mode='binary'  # For binary classification
)

# Augment and fit your model
model = tf.keras.models.Sequential([...])  # Define your model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(train_generator, steps_per_epoch=len(train_generator), epochs=50)
