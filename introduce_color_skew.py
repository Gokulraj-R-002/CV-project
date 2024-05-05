from PIL import Image, ImageEnhance, ImageOps
import os
import numpy as np

base_dir = './data/archive'
dirs = {
    'saturation_increased': './data/saturation_increased_kodak',
    'saturation_decreased': './data/saturation_decreased_kodak',
    'brightness_increased': './data/brightness_increased_kodak',
    'brightness_decreased': './data/brightness_decreased_kodak',
    'hue_increased': './data/hue_shifted_positive_kodak',
    'hue_decreased': './data/hue_shifted_negative_kodak'
}

for dir in dirs.values():
    os.makedirs(dir, exist_ok=True)

saturation_increase_factor = 1.5  # 50% increase
saturation_decrease_factor = 0.5  # 50% decrease
brightness_increase_factor = 1.5  # 50% increase
brightness_decrease_factor = 0.5  # 50% decrease
hue_shift_increase = 30           # +30 degrees
hue_shift_decrease = -30          # -30 degrees

for img_name in os.listdir(base_dir):
    if img_name.lower().endswith(('jpg', 'jpeg', 'png')):
        img_path = os.path.join(base_dir, img_name)
        img = Image.open(img_path)

        # Saturation changes
        enhancer = ImageEnhance.Color(img)
        saturation_img_inc = enhancer.enhance(saturation_increase_factor)
        saturation_img_dec = enhancer.enhance(saturation_decrease_factor)
        saturation_img_inc.save(os.path.join(dirs['saturation_increased'], img_name))
        saturation_img_dec.save(os.path.join(dirs['saturation_decreased'], img_name))

        # Brightness changes
        enhancer = ImageEnhance.Brightness(img)
        brightness_img_inc = enhancer.enhance(brightness_increase_factor)
        brightness_img_dec = enhancer.enhance(brightness_decrease_factor)
        brightness_img_inc.save(os.path.join(dirs['brightness_increased'], img_name))
        brightness_img_dec.save(os.path.join(dirs['brightness_decreased'], img_name))

        # Hue changes
        img_hsv = img.convert('HSV')
        np_img = np.array(img_hsv)
        np_img[..., 0] = (np_img[..., 0] + hue_shift_increase) % 256
        hue_img_inc = Image.fromarray(np_img, 'HSV').convert('RGB')
        np_img[..., 0] = (np_img[..., 0] + hue_shift_decrease) % 256
        hue_img_dec = Image.fromarray(np_img, 'HSV').convert('RGB')
        hue_img_inc.save(os.path.join(dirs['hue_increased'], img_name))
        hue_img_dec.save(os.path.join(dirs['hue_decreased'], img_name))

        img.close()  # Close the image to free up resources
