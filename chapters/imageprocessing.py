from matplotlib import pyplot as plt

image = plt.imread("/Users/legoses/Downloads/lion.png")
plt.imshow(image)
print image
print image.shape
print image[600][600:650]
plt.show()
