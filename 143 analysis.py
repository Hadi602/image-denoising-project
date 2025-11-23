import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image_path = '/content/143.jpeg'
image = Image.open(image_path).convert('L')

output_image_name = 'output_image.jpeg'
image.save(output_image_name)

plt.figure(figsize=(5, 5))
plt.imshow(image, cmap='gray')
plt.title('Uploaded Image')
plt.axis('off')
plt.show()

image_array = np.array(image)

def calculate_histogram(image_array):
    histogram = [0] * 256

    for row in image_array:
        for pixel in row:
            histogram[pixel] += 1

    return histogram

histogram = calculate_histogram(image_array)

plt.figure(figsize=(10, 5))
plt.bar(range(256), histogram, color='gray')
plt.title('Histogram of the Noisy Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

histogram_output = 'histogram_output.png'
plt.savefig(histogram_output)
plt.show()