# CV-Assignment
Cartoonish Filter
Atif-Ur-Rehman Nizamani
CV Assignment
2K18-IT-27


# Output

![before and after 1](https://user-images.githubusercontent.com/73813273/127029097-ea4dcb5b-e4c8-479f-8937-9c6dc150969e.png)

![before and after 2](https://user-images.githubusercontent.com/73813273/127029127-bb4dae8d-a26e-4581-a21b-f34216e04d8e.png)

# report
In this program I've used mostly two common libraries used in Image processing are python's Opencv and Numpy libraries. First, in order to read image i've used imread function, and then resize image according to the computer's resolution. Second, i've used Adaptive histogram equalization called CLAHE(Contrast Limited Adaptive Histogram Equalization), and with the help of this equalization, the contrast is properly done in image. Third, In order to improve image quality pixel by pixel, i've used Super resolution methods from OpenCV, One of the model i've used is called FSRCNN (Fast Super-Resolution Convolutional Neural Network), with the help of this the image's quality is improved. Forth, is to boost color saturation of an image, i've first converted image from BGR to HSV, and then perform some operations pixel by pixel, and then reconvert image back to BGR, And last, i've corrected image gamma with the help of functions provided by Numpy library.Fifth I have also made image to look like cartoon by using Color Quantization method, with the help of this method I have achieved the cartoonish effect. To display images on both side as before and after applying the methods applied to image. i've used imshow method along with waitkey and destroyAllWindows to safely display images.
