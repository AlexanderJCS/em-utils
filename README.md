# EM Utils
## Description

A small program created to help reduce the busywork involving EM images. This program is designed to help with the following tasks:
- Cropping the scale bar out of an image
- Adjusting the luminosity so all images have uniform brightness

## Download

### Prerequisites
- Download Python 3.12 or later [here](https://www.python.org/downloads/). This project was developed with Python 3.12. Earlier versions may work but are not guaranteed to work or be supported in the future. However at this time, I have no reason to believe that Python versions after 3.6 will not work.

### Installation
1. On the top of this page, click Code -> Download ZIP
2. Extract the ZIP file and open the extracted folder
3. Run `gui.pyw` with Python (ensure the correct version is being used)


## Usage

To select the input data folder, click "Select Image Folder". In the file dialog, open the folder with all the .tif files. **If the .tif files are scattered within sub-folders, check the "Recursive Search" checkbox.**

Create an empty folder to store the output images. Then click "Select Output Folder" and select the empty folder.

If you only want to crop the scale bar, uncheck "Adjust Brightness". If you only want to adjust brightness in the images, uncheck "Crop Scale Bar".

Click "Run" to begin the processing. The program may take up to one minute depending on the number of images being processed. When complete, a message box will appear with the number of images processed.

Open the output folder to view the processed images.