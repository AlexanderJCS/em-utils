from PIL.Image import Image
from PIL.Image import fromarray

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


def avg_luminosity(images: list[Image]) -> float:
    """
    Returns the average luminosity of the given images. Does not include pixels that are below 0.2 brightness, since
    those are likely to be stuff in the image or black bars. It also does not include pixels that equal 255.
    
    :param images: The images to process.
    :return: The average luminosity of the images. Range: 0-255 inclusive
    """
    
    img_arrays = [np.array(image).flatten() for image in images]
    
    # threshold the images
    for i, img_array in enumerate(img_arrays):
        img_arrays[i] = img_array[(img_array > 0.2) & (img_array < 255)]
    
    all_thresholded_pixels = np.concatenate(img_arrays)
    
    return np.mean(all_thresholded_pixels)


def adjust_luminosity(image: Image, target_luminosity: float) -> Image:
    """
    Adjusts the luminosity of the given image to the target luminosity.
    
    :param image: The image to adjust.
    :param target_luminosity: The target luminosity to adjust the image to.
    :return: The adjusted image.
    """
    
    img_array = np.array(image)
    
    # adjust the luminosity
    img_array = img_array * (target_luminosity / avg_luminosity([image]))
    img_array = img_array.astype(np.uint8)
    
    return fromarray(img_array)  # Image.fromarray


def run(files_to_process, crop, adjust_brightness, output_dir):
    if crop:
        for file in files_to_process:
            file.pil_img = crop_image(file.pil_img)
    
    if adjust_brightness:
        avg_lum = avg_luminosity([file.pil_img for file in files_to_process])
        
        for file in files_to_process:
            file.pil_img = adjust_luminosity(file.pil_img, avg_lum)
    
    for file in files_to_process:
        filename = file.img_name.split(".")[0]
        filename += "_cropped" if crop else ""
        filename += "_adjustbrightness" if adjust_brightness else ""
        
        file.pil_img.save(os.path.join(output_dir, f"{filename}.tif"))
    