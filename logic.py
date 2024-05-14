from PIL.Image import Image
import numpy as np

import os


def crop_image(image: Image) -> Image:
    """
    Crops the given image.
    :param image: The image to crop.
    :return: The cropped image
    """
    
    # convert image to numpy array for faster processing
    img_array = np.array(image)
    
    # skip if image is square
    if img_array.shape[0] == img_array.shape[1]:
        return image
    
    # determine where the black bar is, and crop it out
    crop_amount = abs(img_array.shape[0] - img_array.shape[1])
    
    # top bar
    if np.all(img_array[0].flatten() == 0):
        return image.crop((0, crop_amount, img_array.shape[1], img_array.shape[0]))

    # bottom bar
    if np.all(img_array[-1].flatten() == 0):
        return image.crop((0, 0, img_array.shape[1], img_array.shape[0] - crop_amount))
    
    # left bar
    if np.all(img_array[:, 0].flatten() == 0):
        return image.crop((crop_amount, 0, img_array.shape[1], img_array.shape[0]))
    
    # right bar
    if np.all(img_array[:, -1].flatten() == 0):
        return image.crop((0, 0, img_array.shape[1] - crop_amount, img_array.shape[0]))
    
    return image  # bad! no black bar found


def run(files_to_process, crop, adjust_brightness, output_dir):
    if crop:
        for file in files_to_process:
            file.pil_img = crop_image(file.pil_img)
            
    for file in files_to_process:
        filename = file.img_name.split(".")[0]
        filename += "_cropped" if crop else ""
        filename += "_adjustbrightness" if adjust_brightness else ""
        
        file.pil_img.save(os.path.join(output_dir, f"{filename}.tif"))
    