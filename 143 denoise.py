import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image_path = '/content/143.jpeg'
image = Image.open(image_path).convert('L')

image_array = np.array(image)



def median_filter(image, filter_size=3):

    m, n = image.shape
    pad_size = filter_size // 2
    padded_image = np.pad(image, pad_size, mode='edge')
    filtered_image = np.zeros_like(image)

    for i in range(m):
        for j in range(n):
            neighborhood = padded_image[i:i + filter_size, j:j + filter_size]
            filtered_image[i, j] = np.median(neighborhood)

    return filtered_image


denoised_image = median_filter(image_array, filter_size=3)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image_array, cmap='gray')
plt.title('Noisy Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(denoised_image, cmap='gray')
plt.title('Denoised Image (Median Filter)')
plt.axis('off')
plt.savefig('denoised_image.png', bbox_inches='tight', pad_inches=1)
plt.show()

denoised_image_output = 'output_143.png'
Image.fromarray(denoised_image).save(denoised_image_output)