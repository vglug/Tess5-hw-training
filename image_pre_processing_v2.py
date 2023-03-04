#Python 3

#packages
from PIL import Image, ImageEnhance
import os



#opening Image
#image1 = Image.open("sample.jpg")


with Image.open("tamil.jpeg") as im:
    #convert into grayscale
    grayscaleImg = im.convert("L")
 
    #grayscale image
    #grayscaleImg.show("grayscale Image")
    grayscaleImg.save('grascale-image.png')
 
    #image contrast enhancer
    enhancer = ImageEnhance.Contrast(grayscaleImg)
    
    factor = 1.5 #increase contrast
    contrastImg = enhancer.enhance(factor)
    #contrastImg.show("more-contrast-image.png")
    contrastImg.save('more-contrast-image.png')
    
    #image brightness enhancer
    enhancer = ImageEnhance.Brightness(contrastImg)
    
    factor = 2 #increase Brightness
    im_output = enhancer.enhance(factor)
    #im_output.show("more-brightness-image.png")
    im_output.save('more-brightness-image.png')





#ouput directory creation
os.makedirs(os.getcwd()+'/output/',exist_ok=True)
#os.makedirs("path/to/directory", exist_ok=True)

#Size
left = 10
top = 140
right = 620
bottom = 170

for i in range(0,10):
	img_res = im_output.crop((left, top, right, bottom)) 
	#img_res.show() 
	#img_res.save("image"+str(i)+".png")
	img_res.save(os.getcwd()+'/output/'+"image"+str(i)+".png")
	top+=30
	bottom+=30

