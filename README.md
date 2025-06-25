# OpenCV: image recognition & feature detection in Python

#### my goal: learn python (numpy, pandas, OpenCV) with a focus on robotic applications

## Corner Detection Algorithms
This project implements classic corner detection algorithms such as:

- [Moravec Corner Detector](https://mahendrathapa.medium.com/moravec-corner-detector-5191f1c04b30)
- [Harris Corner Detector](https://docs.opencv.org/2.4/doc/tutorials/features2d/trackingmotion/harris_detector/harris_detector.html)

### Feature- or Descriptor-Matching
- [FAST: Features from Accelerated Segment Test](https://docs.opencv.org/4.x/df/d0c/tutorial_py_fast.html)
- SIFT
- SURF: Speeded Up Robust Features
- MSER: Maximally Stable Extremal Regions
- BRIEF: Binary Robust Independent Elementary Features
- ORB:Oriented FAST and Rotated BRIEF

How the Matching works:
1. Features (keypoints) like corners or edges are detected.
2. For every keypoint a descriptor is calculated (a descriptor is often a vector)
3. To calculate the similarity of two descriptors (from two images), you calculate the distance between the vectors (e.g. euclidian distance for SIFT, SURF & Hamming distance for ORB, BRIEF).  

## Filter
Using convolution with a filter on a grayscale image, you can detect corners in an image. The value which is displayed in a grayscale image is the intensity (Helligkeit).
- Sobel
- LaPlace
- Gaussian → smoothing
- Canny

#### Filter combinations

- Laplacian of Gaussian (LoG) = Laplace after Gauss

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
## How to use this project?

Open the notebook `corner_detector.ipynb` to see the detectors in action.
