from PIL import Image 
 
  
img = Image.open("sample.jpg") 


left = 10
top = 140
right = 620
bottom = 170
for i in range(0,10):
	img_res = img.crop((left, top, right, bottom)) 
	#img_res.show() 
	img_res.save("image"+str(i)+".png")
	top+=30
	bottom+=30
