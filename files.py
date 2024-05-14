import tkinter as tk
from tkinter import filedialog
from dataclasses import dataclass

import os

from PIL import Image


@dataclass
class ImageData:
    img_name: str
    pil_img: Image


def select_folder(entry: tk.Entry):
    filename = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, filename if filename else "No folder selected")


def get_all_images(img_dir: str, recursive: bool) -> list[ImageData]:
    images: list[ImageData] = []
    
    if recursive:
        for root, dirs, files in os.walk(img_dir):
            for file in files:
                if file.endswith(".tif") or file.endswith(".tiff"):
                    images.append(
                        ImageData(
                            img_name=file,
                            pil_img=Image.open(os.path.join(root, file))
                        )
                    )
    
    else:  # not recursive
        for file in os.listdir(img_dir):
            if file.endswith(".tif") or file.endswith(".tiff"):
                images.append(
                    ImageData(
                        img_name=file,
                        pil_img=Image.open(os.path.join(img_dir, file))
                    )
                )
    
    return images
