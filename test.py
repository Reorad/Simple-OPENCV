import cv2
import matplotlib.pyplot as plt

# Load color image
img = cv2.imread('dog.jpg')
if img is None:
    raise FileNotFoundError("Couldn't load dog.jpg - is it in the project folder?")

# Check dimensions
print(img.shape)  # (height, width, 3)

# Display image (flip BGR -> RGB so colors look right)
plt.imshow(img[:, :, ::-1])
plt.axis('off')
plt.show()

# Save image
cv2.imwrite('dog_copy.jpg', img)