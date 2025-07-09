# OpenCV: image recognition & feature detection in Python

#### my goal: learn python (numpy, pandas, OpenCV) with a focus on robotic applications
This project goes along to the course Automotive Vision from KIT. A good summary of this course can be found here: [Studydrive](https://www.studydrive.net/de/doc/zusammenfassung-h20/912259)

A lot of good Computer Vision Content is provided by the youtube Channel First Principles of Computer Vision. 
- [Edge Detection Playlist](https://youtube.com/playlist?list=PL2zRqk16wsdqXEMpHrc4Qnb5rA1Cylrhx&si=iEJR1xMCJJjKEdBF)
- [Stereo Vision and camera calibration playlist](https://www.youtube.com/watch?v=S-UHiFsn-GI&list=PL2zRqk16wsdoCCLpou-dGo7QQNks1Ppzo)

## Edge & Corner Detection
This project implements classic corner detection algorithms such as:

- [Moravec Corner Detector](https://mahendrathapa.medium.com/moravec-corner-detector-5191f1c04b30)
- [Harris Corner Detector](https://docs.opencv.org/2.4/doc/tutorials/features2d/trackingmotion/harris_detector/harris_detector.html) 

### Feature- or Descriptor-Matching
- [FAST: Features from Accelerated Segment Test](https://docs.opencv.org/4.x/df/d0c/tutorial_py_fast.html)
- SIFT: Scale-invariant feature transform
- SURF: Speeded Up Robust Features
- MSER: Maximally Stable Extremal Regions
- BRIEF: Binary Robust Independent Elementary Features
- ORB:Oriented FAST and Rotated BRIEF

How the Matching works:
1. Features (keypoints) like corners or edges are detected.
2. For every keypoint a descriptor is calculated (a descriptor describes the local surrounding of its feature. This is useful if the camera moved, the image was rotated or scaled. A descriptor is most often a vector)
3. To calculate the similarity of two descriptors (from two images), you calculate the distance between the vectors (e.g. euclidian distance for SIFT, SURF & Hamming distance for binary descriptors from ORB, BRIEF).

### Template Matching
- Sum of Absolute Differences (SAD)
- Sum of Squared Differences (SSD)
- Normalized Cross-Correlation (NCC)

How the Matching works:
Similar to the feature / descriptor matching, you try to match two very similar imagepatches (Pixelblöcke) with each other. But instead of detecting a feature, you simply take the template which you want to find in the other image and use a sliding window to scan the whole image for the template. [Click here for more info](https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html)

## Filter
Using convolution with a filter on a grayscale image, you can detect edges in an image. The value which is displayed in a grayscale image is the intensity (Helligkeit).
- Sobel → first derivative of the image (detects edges; partial derivative in x and y direction → sobel_x filter for vertical edges and sobel_y for horizontal edges)
- LaPlace → second derivative of the image (detects strong changes in intensity → often edges or corners)
- Gaussian → smoothing with a gaussian function
  
#### Filter combinations

- Laplacian of Gaussian (LoG) = Laplace after Gauss
- Canny =
  1. smoothing (Gaussian)
  2. calculate gradients (Sobel Filter)
  3. Non-Maximum Suppression → thins out edges
  4. Hysteresis threshold → to select strong / weak edges

## other algorithms
- Nearest Neighbors (kNN)
- RANSAC
- ReLu

## Parameters of a camera
- f: focal length
- disparity
- K: camera calibration matrix
- resolution
- distance to object

## More complex algorithms
- [SLAM](https://www.youtube.com/watch?v=saVZtgPyyJQ)
- Kalman

# Depth Perception
- [Stereo Vision](https://www.youtube.com/watch?v=6kpBqfgSPRc)
- Time of flight
- structured light

Stereo Vison: Two cameras are used to calculate the depth of an object in an image. The math behind this is called triangulation / epipolar geometry. First you extract the features of both images and try to match them. Then you have two points in the two 2D image coordinate systems. Having only one camera means having only one point in the 2D camera coordinate system. Because of the second camera you can calculate the depth of the feature, because the feature lies on an epipolar line in the second camera. 
To make this process easier you apply rectification, which aligns the epipolar lines horizontally. → Essential Matrix is the product of the roation and translation matrix. 


## How to use this project?

For everything described in this README file, there is a more detailed notebook e.g. `corner_detector.ipynb`, which includes more theory and some code to see the detectors in action.

![alt text](https://github.com/lukestairwalker/OpenCV/blob/main/images/flower.jpg)

<img src="images/flower.jpg" alt="Moravec Beispiel" width="50%"/>
