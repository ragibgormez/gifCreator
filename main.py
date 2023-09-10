import numpy as np
import imageio.v2 as imageio

imagePaths = [
    '/Users/ragibgormez/PycharmProjects/gifCreator/image.jpeg',
    '/Users/ragibgormez/PycharmProjects/gifCreator/image2.png',
    '/Users/ragibgormez/PycharmProjects/gifCreator/image3.jpg'
]


frameDuration = 10  # Örneğin, her kareyi 0.2 saniyede göstermek için.

# Gif dosyasının çıkış yolunu belirtin.
outputGifPath = 'output.gif'

# Gif dosyasını oluşturun.
images = []
for imagePath in imagePaths:
    image = imageio.imread(imagePath)
    images.append(image)

# Gif dosyasını oluşturun ve her bir kareyi ekleyin.
with imageio.get_writer(outputGifPath, mode='I', duration=frameDuration) as writer:
    for image in images:
        writer.append_data(image)
