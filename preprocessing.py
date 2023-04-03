#Python 3
#packages
from PIL import Image, ImageEnhance
import os
import cv2


in_path = os.getcwd()+"/input"


if os.path.exists(in_path) == True:
	in_list = os.listdir(in_path)
	#os.chdir(in_path)
	if len(in_list) == 0:
		print("Note: Please add some image files for preprocessing")
	else:
		os.makedirs(os.getcwd()+'/preprocessed/', exist_ok=True)
		#ouput directory creation
		os.makedirs(os.getcwd()+'/cropped/', exist_ok=True)
		for img in in_list:
			with Image.open(os.getcwd()+"/input/"+img) as im:
				print("[+] Preprocessing started...")
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
				print("[+] Preprocessing completed")
				
				im_ap = cv2.imread(os.getcwd()+'/preprocessed/'+img)
				
				
				# Convert to grayscale
				gray = cv2.cvtColor(im_ap, cv2.COLOR_BGR2GRAY)
				
				# Apply binary thresholding
				#thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
				
				ret,thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_OTSU|cv2.THRESH_BINARY_INV)
				
				#--- choosing the right kernel
				#--- kernel size of 3 rows (to join dots above letters 'i' and 'j')
				#--- and 10 columns to join neighboring letters in words and neighboring words
				rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 5))
				dilation = cv2.dilate(thresh, rect_kernel, iterations = 10)
				#cv2.imshow('dilation', dilation)
				
				#---Finding contours ---_, 
				contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
				
				im_mark = im_ap.copy()
				for cnt in contours:
					x, y, w, h = cv2.boundingRect(cnt)
					cv2.rectangle(im_mark, (x, y), (x + w, y + h), (0, 255, 0), 2)
					#cv2.imshow('final', im2)
					#cv2.imwrite('./cropped/lines'+img+'.jpeg', im_mark)
				
				print("[+] Image Cropping started...")	
				img = img.split(".")
				#print(img[0])
				for i, contour in enumerate(contours):
				    x, y, w, h = cv2.boundingRect(contour)
				    roi = im_mark[y:y+h, x:x+w]
				    cv2.imwrite('./cropped/'+img[0]+'_'+str(i)+'.jpeg', roi)
				
				print("[+] Image Cropping completed")
		os.system("python3 negative.py")
				
							
				

						
else:
	print("Note: Please create the input directories with image files")
