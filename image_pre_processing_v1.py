#Python 3
from PIL import Image, ImageEnhance
import os
import cv2

#from scipy import misc

#opening Image
image1 = Image.open("sample.jpg")


with Image.open("sample.jpg") as im:
    #show the original image
    im.show("Original Image")
    im.save('original-image1.png')
    
    #convert into grayscale
    grayscaleImg = im.convert("L")
 
    #show the grayscale image
    grayscaleImg.show("grayscale Image")
    grayscaleImg.save('grascale-image1.png')
 
    
#image brightness enhancer
enhancer = ImageEnhance.Contrast(image1)

factor = 1 #gives original image
im_output = enhancer.enhance(factor)
im_output.show("original-image2.png")
im_output.save('original-image2.png')

factor = 0.5 #decrease constrast
im_output = enhancer.enhance(factor)
im_output.show("less-contrast-image2.png")
im_output.save('less-contrast-image2.png')

factor = 1.5 #increase contrast
im_output = enhancer.enhance(factor)
im_output.show("more-contrast-image2.png")
im_output.save('more-contrast-image2.png')




'''
#ouput directory creation
os.mkdir(os.getcwd()+'/output/')


#Size
left = 10
top = 140
right = 620
bottom = 170



for i in range(0,10):
	img_res = image1.crop((left, top, right, bottom)) 
	#img_res.show() 
	#img_res.save("image"+str(i)+".png")
	img_res.save(os.getcwd()+'/output/'+"image"+str(i)+".png")
	top+=30
	bottom+=30
'''
