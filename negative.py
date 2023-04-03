import os
import cv2
#import pytesseract
from PIL import Image
#import numpy as np


#input directory
in_path = os.getcwd()+"/cropped/"


if os.path.exists(in_path) == True:
	in_list = os.listdir(in_path)
	#print(in_list)
	if len(in_list) == 0:
		print("Note: Please add some images files inside cropped directory for ground truth Generation")
	else:
		#os.makedirs(os.getcwd()+'/ground_truth/', exist_ok=True)
		os.makedirs(os.getcwd()+'/negative/', exist_ok=True)
		print("[+] Negative Image generation started...")
		for img in in_list:
			#print(img)
			image = cv2.imread(str(in_path+img))
			#print(img.dtype)
			img_neg = 255 - image
			im = img.split(".")
			cv2.imwrite('./negative/'+im[0]+'.tif',img_neg)
			
		print("[+] Negative Image generation completed")
	print("[+] Ground truth generation started...")
	os.system("./groundtruth.sh")
	print("[+] ground truth generation stopped")
	
	
else:
	print("Note: Please create the input directories with image files")
