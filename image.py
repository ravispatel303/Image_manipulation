# To blur, resize and create thumbnail of image.

from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

# to blur image
filtered = img.filter(ImageFilter.BLUR)
filtered.save('blur.png', 'png')
filtered.show()

# to create thumbnail
thumb = img
thumb.thumbnail((200,100))
thumb.save('thumbnail.jpg')
thumb.show()

# to resize image
rez = img
rez.resize((100,100))
rez.save('rz.png','png')
rez.show()