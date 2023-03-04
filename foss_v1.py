#Python 3

#packages
from PIL import Image, ImageEnhance
import os


in_path = os.getcwd()+"/input"


if os.path.exists(in_path) == True:
	in_list = os.listdir(in_path)
	#os.chdir(in_path)
	if len(in_list) == 0:
		print("Note: Please add some image files for preprocessing")
	else:
		os.makedirs(os.getcwd()+'/preprocessed/', exist_ok=True)
		#ouput directory creation
		os.makedirs(os.getcwd()+'/output/', exist_ok=True)
		for img in in_list:
			with Image.open(os.getcwd()+"/input/"+img) as im:
				#convert into grayscale
				grayscaleImg = im.convert("L")
				
				#image contrast enhancer
				enhancer = ImageEnhance.Contrast(grayscaleImg)
				
				factor = 1.5 #increase contrast
				contrastImg = enhancer.enhance(factor)
				
				#image brightness enhancer
				enhancer = ImageEnhance.Brightness(contrastImg)

				factor = 2 #increase Brightness
				im_output = enhancer.enhance(factor)
				
				#im_output.show("more-brightness-image.png")
				im_output.save(os.getcwd()+'/preprocessed/'+img)

						
else:
	print("Note: Please create the input directories with image files")
	

pr_path = os.getcwd()+"/preprocessed/"
pr_list = os.listdir(pr_path)

for img in pr_list:
	with Image.open(os.getcwd()+"/preprocessed/"+img) as im:
		width, height = im.size
		print(im.size)
		
		# Setting the points for cropped image
		left = 0
		top = 40
		right = 1100
		bottom = 100
		for i in range(0,10):
			img_res = im_output.crop((left, top, right, bottom))
			#img_res = im_output.crop((left, bottom, right, top)) 
			#img_res.save(os.getcwd()+'/output/'+img+str(i)+'.png')
			img_res.save(os.getcwd()+'/output/'+img+str(i)+".png")
			top+=45
			bottom+=45
	
	
