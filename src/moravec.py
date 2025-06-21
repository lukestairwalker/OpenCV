import cv2
import numpy as np

def moravec_corner_detector(img_gray, window_size=3, threshold=10000):
    corners = np.zeros_like(img_gray, dtype=np.float32)
    offset = window_size // 2

    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            shifted = np.roll(img_gray, shift=(dy, dx), axis=(0, 1))
            ssd = (img_gray - shifted) ** 2
            corners += cv2.boxFilter(ssd, -1, (window_size, window_size))

    corners[corners < threshold] = 0
    return corners