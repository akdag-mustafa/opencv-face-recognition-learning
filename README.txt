# Image Processing from Scratch

This repository is a learning-focused image processing project that compares ready-made OpenCV functions with manually implemented algorithms in Python and C++.

The main purpose is to understand:

* How image processing algorithms work mathematically
* How pixels and color channels are represented
* The performance difference between Python and C++
* How optimized OpenCV functions compare with manual implementations

## Project Structure

```text
opencv-face-project/
├── opencv/
│   └── grayScale.py
├── python/
│   └── grayScale.py
├── C++/
│   └── grayScale.cpp
├── requirements.txt
└── README.md
```

## Grayscale Implementations

The grayscale conversion is implemented in three different ways.

### 1. Python with OpenCV

File:

```text
opencv/grayScale.py
```

This version uses OpenCV's optimized grayscale conversion function:

```python
cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```

### 2. Manual Python Implementation

File:

```text
python/grayScale.py
```

This version processes every pixel manually without using OpenCV's grayscale conversion function.

The grayscale value is calculated with:

```text
Gray = 0.114 × Blue + 0.587 × Green + 0.299 × Red
```

### 3. Manual C++ Implementation

File:

```text
C++/grayScale.cpp
```

This version applies the same grayscale formula using C++ loops.

OpenCV is used only for:

* Capturing frames from the camera
* Storing image matrices
* Displaying the results

The grayscale conversion itself is implemented manually.

## Requirements

### Python

* Python 3
* OpenCV
* NumPy

Install the Python dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

### C++

* C++17-compatible compiler
* OpenCV 5
* Homebrew on macOS

Install OpenCV:

```bash
brew install opencv
```

## Running the Applications

### OpenCV Python Version

```bash
python3 opencv/grayScale.py
```

### Manual Python Version

```bash
python3 python/grayScale.py
```

### Manual C++ Version

Compile on an Apple Silicon Mac:

```bash
clang++ C++/grayScale.cpp \
-std=c++17 \
-I/opt/homebrew/opt/opencv/include/opencv5 \
-L/opt/homebrew/opt/opencv/lib \
-lopencv_core \
-lopencv_videoio \
-lopencv_highgui \
-o C++/grayscale
```

Run:

```bash
./C++/grayscale
```

Press `q` while the camera window is active to close the application.


## Average Blur Implementations

Average Blur replaces each pixel with the average value of its neighboring pixels. It is used to smooth images, reduce small details, and suppress noise.

The filter is implemented using the same three-stage learning approach.

### 1. Python with OpenCV

File:

```text
opencv/average_blur.py
```

This version uses OpenCV's optimized Average Blur function:

```python
blurred_image = cv2.blur(image, (5, 5))
```

The `(5, 5)` parameter defines a 5×5 kernel containing 25 pixels.

### 2. Manual Python Implementation

File:

```text
python/average_blur.py
```

This version manually moves a kernel over every pixel in the image.

For each pixel:

1. Select the surrounding kernel region
2. Calculate the average Blue, Green, and Red values
3. Write the calculated values to the output image

The output image is initialized with:

```python
blurred_image = np.zeros_like(image)
```

Image borders are extended using:

```python
np.pad(image, ..., mode="edge")
```

This repeats the nearest border pixels so that a complete kernel can also be applied to pixels located at the image boundaries.

### 3. Manual C++ Implementation

File:

```text
C++/average_blur.cpp
```

This version manually iterates over the image and kernel using C++ loops.

The Blue, Green, and Red values are accumulated separately:

```cpp
totalB += pixel[0];
totalG += pixel[1];
totalR += pixel[2];
```

The channel averages are calculated with:

```text
Average channel value = Channel sum / Number of kernel pixels
```

For a 5×5 kernel:

```text
Number of pixels = 5 × 5 = 25
```

Instead of creating a physically padded image, the C++ implementation uses `std::clamp()` to redirect out-of-range coordinates to the nearest valid border pixel:

```cpp
int neighborX = std::clamp(
    x + kernelX,
    0,
    image.cols - 1
);
```

This produces edge-replication behavior without allocating an additional padded image.

### Average Blur Kernel

A 3×3 Average Blur kernel can be represented as:

```text
1/9 ×
[ 1  1  1 ]
[ 1  1  1 ]
[ 1  1  1 ]
```

All neighboring pixels have equal weight.

Larger kernels create stronger blur:

```text
3×3   → Light blur
5×5   → Medium blur
15×15 → Strong blur
```

### What Was Learned

* Kernel-based image processing
* Neighborhood operations
* Average filtering
* Border handling
* NumPy slicing and `np.mean()`
* Image padding with `np.pad()`
* Coordinate limiting with `std::clamp()`
* Separate accumulation of BGR channels
* Differences between Python loops, C++ loops, and optimized OpenCV functions


## Learning Roadmap

The following image processing topics will be studied using the same three-stage approach:

* [x] Grayscale conversion
* [X] Average blur
* [ ] Gaussian blur
* [ ] Thresholding
* [ ] Edge detection
* [ ] Morphological operations
* [ ] Contour detection
* [ ] Object detection and tracking
* [ ] Performance benchmarking

For each topic:

1. Use the ready-made OpenCV implementation
2. Implement the algorithm manually in Python
3. Implement the algorithm manually in C++
4. Compare execution times and results

## Author

Mustafa Akdağ

Electrical and Electronics Engineer
