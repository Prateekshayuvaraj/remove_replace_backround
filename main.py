import cv2

class ImageProcessor:    #class
    def __init__(self, image):  #class constructor
        if image is None:
            raise ValueError("Image not loaded successfully.")
        self.image = image

    def resize(self, width, height):   #resize
        return cv2.resize(self.image, (width, height))

    def to_grayscale(self):  #grayscale
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

class ThresholdProcessor:
    def __init__(self, threshold):
        self.threshold = threshold

    def apply_threshold(self, image):
        _, thresholded_image = cv2.threshold(image, self.threshold, 255, cv2.THRESH_BINARY)
        return thresholded_image

class MaskProcessor:
    def invert_mask(self, mask):  #invert binary
        return 255 - mask

class BackgroundChanger:
    def __init__(self, original_image_path, new_background_path, threshold=125):
        self.original_image = cv2.imread(original_image_path)
        self.new_background = cv2.imread(new_background_path)
        self.threshold = threshold

        if self.original_image is None or self.new_background is None:
            raise ValueError("Image(s) not loaded successfully.")

    def change_background(self):
        # Image Processing
        resized_input_image = cv2.resize(
            self.original_image, (self.new_background.shape[1], self.new_background.shape[0])
        )
        grayscale_image = cv2.cvtColor(resized_input_image, cv2.COLOR_BGR2GRAY)

        # Threshold Processing
        _, thresholded_image = cv2.threshold(grayscale_image, self.threshold, 255, cv2.THRESH_BINARY)

        # Mask Processing
        inverted_mask = 255 - thresholded_image

        # Foreground Image
        foreground_image = cv2.bitwise_and(resized_input_image, resized_input_image, mask=inverted_mask)

        # Resize the new background image to the same size as the foreground image
        resized_new_background_image = cv2.resize(
            self.new_background, (resized_input_image.shape[1], resized_input_image.shape[0])
        )

        # New Background
        new_background = cv2.bitwise_and(resized_new_background_image, resized_new_background_image, mask=thresholded_image)

        # Final Output
        output_image = cv2.add(foreground_image, new_background)

        return output_image

if __name__ == "__main__":
    try:
        
    #creating an object
        background_changer = BackgroundChanger('image_3.jpg', 'gbb.jpg')
        output_image = background_changer.change_background() # calling o

        # Display the output image
        cv2.imshow('Output Image', output_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except ValueError as e:
        print(f"Error: {e}")