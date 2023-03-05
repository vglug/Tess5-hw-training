#tessract
#/usr/bin/tesseract
#tesseract tamil.jpeg text_result -l tam
#tesseract I1_1.jpeg I1_1.tif -l tam

for i in ./cropped/*.jpeg; 
do 
tesseract "$i" "./cropped/$(echo $i | awk -F'.' '{print $2}' | awk -F'/' '{print $3}')" -l tam; 
done;


for i in ./negative/*.tif; 
do 
tesseract "$i" "./negative/$(echo $i | awk -F'.' '{print $2}' | awk -F'/' '{print $3}')" -l tam; 
done;

