# Image pre processing for Tess5-hw-training.

This script used to pre process the hand written image and get groung truth to train tesseract model to increase the accuracy of Tesseract OCR engine. 

`clone`

```
▶ git clone https://github.com/vigneshkannan255/Tess5-hw-training.git
```


## Required Python Packages

`Python packages installation`

```
▶ pip3 install Image
```
```
▶ pip3 install opencv-python
```

## Required Linux Packages

`tesseract-ocr Installation`

```
▶ sudo apt install tesseract-ocr
```

`tesseract-ocr Tamil Language Installation`
```
▶ sudo apt install tesseract-ocr-tam
```


## Process

- [x]  Orginal to grayscale.
- [x]  Contrast Increase.
- [x]  Brightness Increase.
- [x]  Cropping Images line by line.
- [x]  Generating Negative Image from cropped Image.
- [x]  Generating ground truth from cropped Image.
- [x]  Generating ground truth from Negative Image.



## Sample Input Image.

<p align="left"><img src="https://github.com/vigneshkannan255/Tess5-hw-training/blob/19ecca4cbd93649b6152345643886e0f6c0d65de/input/i1.jpeg" width="300"/> </p>



## Preprocessed Image.

<p align="left"><img src="https://github.com/vigneshkannan255/Tess5-hw-training/blob/19ecca4cbd93649b6152345643886e0f6c0d65de/preprocessed/i1.jpeg" width="300"/>



## Sample Cropped Image.

<p align="left"><img src="https://github.com/vigneshkannan255/Tess5-hw-training/blob/19ecca4cbd93649b6152345643886e0f6c0d65de/cropped/i1_10.jpeg" width="300"/>


## Negative Image.

<p align="left"><img src="https://github.com/vigneshkannan255/Tess5-hw-training/blob/b11b0a01924e9f0aa3ea73536e3cb7075fee6c32/negative/i1_0.jpg" width="300"/>



