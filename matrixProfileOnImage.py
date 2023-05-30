import numpy as np
import matplotlib.pyplot as plt

def calculate_matrix_profile(image, window_size):
    height, width, _ = image.shape
    matrix_profile = np.zeros((height, width))

    for i in range(height - window_size + 1):
        for j in range(width - window_size + 1):
            window = image[i:i+window_size, j:j+window_size, :]
            matrix_profile[i, j] = np.mean(window)

    return matrix_profile

# Load the image
image = plt.imread('path_to_your_image.jpg')

# Convert the image to numpy array (if necessary)
image = np.array(image)

# Set the window size for the matrix profile
window_size = 5

# Calculate the matrix profile
matrix_profile = calculate_matrix_profile(image, window_size)

# Display the matrix profile
plt.imshow(matrix_profile, cmap='gray')
plt.colorbar()
plt.show()
