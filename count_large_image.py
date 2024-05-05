import os
from PIL import Image

train_dir = './data/val_images/train'
test_dir = './data/val_images/test'

def count_large_images(image_dir):
    cnt = 0
    for filename in os.listdir(image_dir):
        image_path = os.path.join(image_dir, filename)
        with Image.open(image_path) as img:
            width, height = img.size
            if width > 256 and height > 256:
                cnt += 1
            else:
                os.remove(image_path)

    return cnt

print(count_large_images(train_dir))
print(count_large_images(test_dir))
