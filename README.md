# Haar_Cascade2
Detects multiple shapes. Based off of https://github.com/Senpat/Haar_Cascade 

### Steps
Store frames of video as png files. Use https://www.isimonbrown.co.uk/vlc-export-frames/ Make sure to run vlc as administrator.

Run rotate_and_flip.py to generate all test cases. Triangles are stored trianglepos and squares are stored in squarepos.

Use haar-object-marker to generate description file and manually generate ROI. 

`python haar_positive_creator.py squarepos bgsquare.txt`

Run cropper.py to convert description file to images (only does one crop per line). You need this for negative data.

`python cropper.py inputdescriptionfile outputfolder outputdescriptionfile` or `python cropper.py bgsquare.txt squarecrop squarecrop.txt`

Note that the description file for negative data is formatted differently than positives. cropper.py will create a file called squarecrop that contains a path to all of the files in squarecrop. The idea is you copy the contents of squarecrop.txt to the negative description file of triangle and all the other shapes (but not square).

Run opencv_createsamples to create a positives vector file. 

`opencv_createsamples -info [positive description file] -num [number of data] -w 20 -h 20 -vec [name of positives vector file]`

For example: `opencv_createsamples -info bgsquare.txt -num 450 -w 20 -h 20 -vec positivessquare.vec`

### Files
bgtriangle.txt -> triangle positive description file

bgsquare.txt -> square positive description file

negatives -> negative images for all (grass)

squarecrop -> square pictures converted from bgsquare.txt (for negative data for triangle)

trianglecrop -> triangle pictures converted from bgtriangle.txt (for negative data for square)

squarecrop.txt -> text file containing path to all pictures in squarecrop

trianglecrop.txt -> text file containing path to all pictures in trianglecrop 

squareneg.txt -> negative description file for squares - contains allnegatives and trianglecrop.txt

triangleneg.txt -> negative description file for triangles - contains allnegatives squarecrop.txt
