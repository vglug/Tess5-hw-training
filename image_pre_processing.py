#Python 3
from PIL import Image 
import os
#from scipy import misc

#opening Image
img = Image.open("sample.jpg")

#ouput directory creation
os.mkdir(os.getcwd()+'/output/')


#Size
left = 10
top = 140
right = 620
bottom = 170


for i in range(0,10):
	img_res = img.crop((left, top, right, bottom)) 
	#img_res.show() 
	#img_res.save("image"+str(i)+".png")
	img_res.save(os.getcwd()+'/output/'+"image"+str(i)+".png")
	top+=30
	bottom+=30
