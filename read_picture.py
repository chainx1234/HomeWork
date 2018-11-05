from PIL import Image
import matplotlib.image as mping
import matplotlib.pyplot as plt

'''def open_image(path):
  newImage = Image.open(path)
  return newImage

# Save Image
def save_image(image, path):
  image.save(path , 'png')

# Create a new image with the given size
def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image

# Get the pixel from the given image
def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
      return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel'''

path = '/home/vnc/work/AI/application/img_0000_i.png'
#path2 = '/home/vnc/work/AI/application/img_0000_i2.png'

img = Image.open(path)
rgb_im = img.convert('RGBA')
width, height = rgb_im.size
#r, g, b = img.getpixel((230, 250))
#print(r,g,b)

# put color

#r,g,b = img.getpixel((0,0))

#pixel = get_pixel(img, 300, 300)
#print("{}, {},{}".format(r,g,b))
for x in range(width):
   for y in range(height):
       print(y)
       current_color = rgb_im.getpixel( (x,y) )
       #print(type(current_color))

       rgb_im.putpixel((x,y), new_color)
rgb_im.save('test', 'png')
#plt.imshow(img)
#plt.show()

