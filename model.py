from .utils import cache_forever
import imagehash, base64
from PIL import Image
import numpy as np

from io import BytesIO

class Task:
    def __init__(self, task_obj, challenge=None):
        self.challenge = challenge
        self.key = task_obj["task_key"]
        self.url = task_obj["datapoint_uri"]
    
    def _request(self, url, method="GET", http_client=None):
        http_client = http_client if http_client is not None \
                      else self.challenge.http_client
        return http_client.request(
            method,
            url,
            headers={"Accept-Encoding": "gzip, deflate, br"}
        )
    
    #@cache_forever()
    def content(self, **kw) -> bytes:
        resp = self._request(self.url, **kw)
        return resp.content
    
    #@cache_forever()
    def image(self, raw=False, encoded=False, **kw) -> Image.Image:
        content = self.content(**kw)
        if raw: return content
        if encoded: return base64.b64encode(content)
        return Image.open(BytesIO(content))

    #@cache_forever()
    def phash(self, size=16, **kw) -> str:
        image = self.image(**kw)
        phash = str(imagehash.phash(image, size))
        self._phash = phash
        return phash


# Additional Imports

# Additional Utility Class
class ImageProcessor:
    def __init__(self):
        pass

    def grayscale(self, image):
        return image.convert("L")

    def rotate(self, image, angle):
        return image.rotate(angle)

    def apply_filter(self, image, kernel):
        # Apply a convolutional filter to the image
        img_array = np.array(image)
        filtered_image = np.convolve(img_array, kernel, mode='same')
        return Image.fromarray(filtered_image)

    def resize(self, image, size):
        return image.resize(size)

    def crop(self, image, box):
        return image.crop(box)

# Additional Function in the Task Class
    def histogram(self, **kw) -> np.ndarray:
        image = self.image(**kw)
        histogram = np.histogram(np.array(image).ravel(), bins=256, range=(0, 256))
        return histogram[0]

    def apply_custom_filter(self, kernel, **kw) -> Image.Image:
        image = self.image(**kw)
        return ImageProcessor().apply_filter(image, kernel)

    def rotate_and_resize(self, angle, size, **kw) -> Image.Image:
        image = self.image(**kw)
        rotated = ImageProcessor().rotate(image, angle)
        resized = ImageProcessor().resize(rotated, size)
        return resized

    def crop_and_grayscale(self, box, **kw) -> Image.Image:
        image = self.image(**kw)
        cropped = ImageProcessor().crop(image, box)
        grayscale = ImageProcessor().grayscale(cropped)
        return grayscale

# Usage Example
if __name__ == "__main__":
    # Create a Task instance
    task_info = {
        "task_key": "12345",
        "datapoint_uri": "https://example.com/image.jpg"
    }
    task = Task(task_info)

    # Perform image processing operations
    histogram = task.histogram()
    custom_filter = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    filtered_image = task.apply_custom_filter(custom_filter)
    rotated_resized_image = task.rotate_and_resize(angle=30, size=(200, 200))
    cropped_grayscale_image = task.crop_and_grayscale(box=(50, 50, 150, 150))

    # Print results
    print("Image Histogram:", histogram)
    filtered_image.show()
    rotated_resized_image.show()
    cropped_grayscale_image.show()


# Additional Utility Class for Complex Image Processing
class AdvancedImageProcessor:
    def __init__(self):
        pass

    def apply_edge_detection(self, image):
        # Apply edge detection algorithm to the image
        # You can use popular edge detection algorithms like Canny or Sobel here.
        # For demonstration, we use a simple edge detection filter.
        edge_filter = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
        return ImageProcessor().apply_filter(image, edge_filter)

    def apply_advanced_filter(self, image):
        # Apply a more advanced image filter
        # You can implement custom filters or use advanced filtering techniques here.
        # For demonstration, we use a sharpening filter.
        sharpening_filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        return ImageProcessor().apply_filter(image, sharpening_filter)

    def apply_color_inversion(self, image):
        # Invert colors in the image
        return ImageOps.invert(image)

# Additional Function in the Task Class
    def apply_edge_detection_filter(self, **kw) -> Image.Image:
        image = self.image(**kw)
        return AdvancedImageProcessor().apply_edge_detection(image)

    def apply_advanced_image_filter(self, **kw) -> Image.Image:
        image = self.image(**kw)
        return AdvancedImageProcessor().apply_advanced_filter(image)

    def invert_image_colors(self, **kw) -> Image.Image:
        image = self.image(**kw)
        return AdvancedImageProcessor().apply_color_inversion(image)

# Usage Example
if __name__ == "__main__":
    # Create a Task instance
    task_info = {
        "task_key": "12345",
        "datapoint_uri": "https://example.com/image.jpg"
    }
    task = Task(task_info)

    # Perform advanced image processing operations
    edge_detected_image = task.apply_edge_detection_filter()
    advanced_filtered_image = task.apply_advanced_image_filter()
    inverted_colors_image = task.invert_image_colors()

    # Print results
    edge_detected_image.show()
    advanced_filtered_image.show()
    inverted_colors_image.show()


