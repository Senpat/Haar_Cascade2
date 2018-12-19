# Haar_Cascade2
Detects multiple shapes. Based off of https://github.com/Senpat/Haar_Cascade 

### Steps
Store frames of video as png files. Use https://www.isimonbrown.co.uk/vlc-export-frames/ Make sure to run vlc as administrator.

Run rotate_and_flip.py to generate all test cases. Triangles are stored trianglepos and squares are stored in squarepos.

Use haar-object-marker to generate description file and manually generate ROI. `python haar_positive_creator.py squarepos bgsquare.txt`


### Files
bgtriangle.txt -> triangle positive description file

bgsquare.txt -> square positive description file

negatives -> negative images for all (grass)

negtriangle -> negative images for triangle (grass + square)

negsquare -> negative images for square (grass + triangle)
