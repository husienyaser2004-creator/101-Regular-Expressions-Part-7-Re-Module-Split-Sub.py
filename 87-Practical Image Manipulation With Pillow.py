#---------------------------------------------
#--Practical Image Manipulation With Pillow---
#---------------------------------------------

from PIL import Image

# Open The Image
myImage = Image.open(r"D:\Python\Files\play.jpg")

# Show The Image
myImage.show()

# My Cropped Image
myBox = (0, 0, 400, 400)
myNewImge = myImage.crop(myBox)

# Show The New Image 
myNewImge.Show()

# My Converted Mode Image
myConverted = myImage.convert("L")
myConverted.show() 
