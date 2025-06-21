import cv2
import numpy as np

def harris_corner_detector(img_gray, window_size=3, k=0.04, threshold=1e-6):
    """
    Harris Corner Detector
    Parameters:
        img_gray (ndarray): Input grayscale image
        window_size (int): Window size for corner detection (odd number)
        k (float): Harris detector free parameter (typically 0.04 - 0.06)
        threshold (float): Minimum response value to consider a corner
    Returns:
        harris_response (ndarray): 2D array of corner responses
    """
    # Compute gradients
    Ix = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
    Iy = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)

    # Compute products of derivatives
    Ixx = Ix ** 2
    Iyy = Iy ** 2
    Ixy = Ix * Iy

    # Apply box filter (smoothing)
    Sxx = cv2.boxFilter(Ixx, -1, (window_size, window_size))
    Syy = cv2.boxFilter(Iyy, -1, (window_size, window_size))
    Sxy = cv2.boxFilter(Ixy, -1, (window_size, window_size))

    # Harris response R = det(M) - k * trace(M)^2
    detM = (Sxx * Syy) - (Sxy ** 2)
    traceM = Sxx + Syy
    harris_response = detM - k * (traceM ** 2)

    # Thresholding
    harris_response[harris_response < threshold * harris_response.max()] = 0

    return harris_response