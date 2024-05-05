import os
import shutil
import random

# Path to the directory where your 50,000 images are stored
source_dir = './data/val_images/'

# Paths to the train and test directories
train_dir = './data/val_images/train'
test_dir = './data/val_images/test'

# Create train and test directories if they don't exist
if not os.path.exists(train_dir):
    os.makedirs(train_dir)
if not os.path.exists(test_dir):
    os.makedirs(test_dir)

# Get a list of all image filenames in the source directory
all_files = os.listdir(source_dir)
random.shuffle(all_files)  # Shuffle the list to ensure randomness

# Split the files into train and test
train_files = all_files[:40000]
test_files = all_files[40000:]

# Function to move files
def move_files(files, destination):
    for file in files:
        shutil.move(os.path.join(source_dir, file), os.path.join(destination, file))

# Move the files
move_files(train_files, train_dir)
move_files(test_files, test_dir)

print("Files have been successfully moved to train and test directories.")

