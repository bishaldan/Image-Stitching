# Image Stitching with OpenCV

This project demonstrates the use of OpenCV to create panoramic images by stitching multiple images together. The script processes images from different folders, resizes them, and attempts to stitch them into a single panoramic image.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/bishaldan/Image-Stitching.git
   cd Image-Stitching
   ```

2. **Install the required dependencies:**
   Make sure you have Python installed on your machine. You can install the required libraries using pip:

   ```bash
   pip install opencv-python
   ```

## Usage

1. **Prepare your images:**
   - Create a folder named `img` in the root directory of the project.
   - Inside the `img` folder, create subfolders where each subfolder contains images that you want to stitch into a panorama.

2. **Run the script:**
   Execute the Python script:

   ```bash
   python main.py
   ```

   The script will detect the images in each subfolder, attempt to stitch them into a panorama, and display the resulting image.

## Project Structure

```
├── img/
│   ├── folder1/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ...
│   ├── folder2/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ...
│   └── ...
├── main.py
└── README.md
```

- `img/`: Directory containing subfolders of images to be stitched.
- `main.py`: The main script that handles the image stitching.
- `README.md`: Documentation file explaining the project.

## How It Works

1. The script reads the contents of the `img` folder and lists all subfolders.
2. For each subfolder, it reads and resizes the images.
3. The images are then fed into OpenCV's `Stitcher` class, which attempts to create a panorama.
4. If successful, the panorama is displayed using OpenCV's `imshow`. Otherwise, an error message is printed.

### Important Notes
- The images within each subfolder should be related and overlap to ensure successful stitching.
- The script resizes images by 80% to ensure they fit within memory and processing constraints.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
