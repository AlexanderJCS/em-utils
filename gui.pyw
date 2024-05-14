import tkinter as tk

import files
import logic

X_PAD = 10
Y_PAD = 10

FONT_BIG = ("Helvetica", 14)
FONT_NORMAL = ("Helvetica", 12)


def run(input_path: str, output_path: str, crop: bool, adjust_brightness: bool, recursive: bool, output_text: tk.Label):
    all_files = files.get_all_images(input_path, recursive)
    logic.run(all_files, crop, adjust_brightness, output_path)


def main():
    # Window configuration
    root = tk.Tk()
    root.title("EM Utils")
    root.resizable(width=False, height=False)
    
    # Main label
    mainlabel = tk.Label(root, text="EM Utils", font=FONT_BIG)
    mainlabel.grid(row=0, column=0, columnspan=2, padx=X_PAD, pady=Y_PAD,)
    
    # Checkboxes
    
    # -Crop checkbox
    crop_var = tk.BooleanVar()
    crop_check = tk.Checkbutton(root, text="Crop", variable=crop_var, font=FONT_NORMAL)
    crop_check.select()  # default to checked
    crop_check.grid(row=1, column=0, padx=X_PAD, pady=Y_PAD)
    
    # -Adjust brightness checkbox
    adjust_brightness_var = tk.BooleanVar()
    adjust_brightness_check = tk.Checkbutton(
        root, text="Adjust Brightness", variable=adjust_brightness_var, font=FONT_NORMAL)
    adjust_brightness_check.select()  # default to checked
    adjust_brightness_check.grid(row=1, column=1, padx=X_PAD, pady=Y_PAD)
    
    # -Recursive file search checkbox
    recursive_search_var = tk.BooleanVar()
    recursive_search_check = tk.Checkbutton(
        root, text="Recursive Search", variable=recursive_search_var, font=FONT_NORMAL)
    recursive_search_check.grid(row=2, column=0, columnspan=2, padx=X_PAD, pady=Y_PAD)
    
    # Image path
    image_path_label = tk.Entry(root, font=FONT_NORMAL)
    image_path_label.insert(0, "No image folder selected")
    image_path_label.grid(row=3, column=1, columnspan=1, padx=X_PAD, pady=Y_PAD)
    
    image_path_button = tk.Button(
        root, text="Select Image Folder", command=lambda: files.select_folder(image_path_label), font=FONT_NORMAL
    )
    image_path_button.grid(row=3, column=0, columnspan=1, padx=X_PAD, pady=Y_PAD)
    
    # Output path
    output_path_label = tk.Entry(root, font=FONT_NORMAL)
    output_path_label.insert(0, "No output folder selected")
    output_path_label.grid(row=4, column=1, columnspan=1, padx=X_PAD, pady=Y_PAD)
    
    output_path_button = tk.Button(
        root, text="Select Output Folder", command=lambda: files.select_folder(output_path_label), font=FONT_NORMAL
    )
    output_path_button.grid(row=4, column=0, columnspan=1, padx=X_PAD, pady=Y_PAD)
    
    # Run button
    run_button = tk.Button(
        root,
        text="Run!", width=30,
        command=lambda: run(
            image_path_label.get(), output_path_label.get(), crop_var.get(), adjust_brightness_var.get(),
            recursive_search_var.get(), output_label
        ),
        font=FONT_NORMAL
    )
    run_button.grid(row=5, column=0, columnspan=2, padx=X_PAD, pady=Y_PAD,)
    
    # Output label
    output_label = tk.Label(root, text="", font=FONT_NORMAL)
    output_label.grid(row=6, column=0, columnspan=2, padx=X_PAD, pady=Y_PAD)
    
    root.mainloop()


if __name__ == "__main__":
    main()
