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

## Learning Roadmap

The following image processing topics will be studied using the same three-stage approach:

* [x] Grayscale conversion
* [ ] Average blur
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
