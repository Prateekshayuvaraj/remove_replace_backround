# Background Changer 🖼️

This Python script allows you to change the background of an image by replacing it with a new background image.

## Features
- **Image Processing**: Utilizes OpenCV for image processing tasks such as resizing and converting to grayscale.
- **Threshold Processing**: Applies a threshold to create a binary mask separating the foreground and background.
- **Mask Processing**: Inverts the binary mask to isolate the foreground.
- **Background Replacement**: Replaces the background with a new image while preserving the foreground.
- **Customizable Threshold**: Allows you to adjust the threshold value for fine-tuning the foreground/background separation.

## How to Use
1. **Setup**: Ensure you have Python installed along with the required dependencies specified in `requirements.txt`.
2. **Input Images**: Prepare the original image (with the subject) and the new background image.
3. **Run Script**: Execute the script `background_changer.py` and specify the paths to the original and new background images.
4. **Output**: The script will generate an image with the background replaced and display it.

## Dependencies
- Python 3.x
- OpenCV
  
## Acknowledgements
- Inspired by the concept of background replacement in image processing.
