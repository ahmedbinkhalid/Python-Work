import cv2
import numpy as np

def denoise_image(image, h=10, template_window=5, search_window=15):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Non-Local Means Denoising
    denoised = cv2.fastNlMeansDenoising(gray, None, h, template_window, search_window)

    return denoised

# Load the noisy image
noisy_image = cv2.imread('noisy_image.jpg')

# Apply denoising
denoised_image = denoise_image(noisy_image)

# Display the results
cv2.imshow('Noisy Image', noisy_image)
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
