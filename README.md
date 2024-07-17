# Image Processing & Enhancement
# Overview
The "Image Processing & Enhancement" project aims to provide a user-friendly web application for performing various image processing operations directly in the browser. This project leverages OpenCV.js, a JavaScript binding for OpenCV, to enable real-time image manipulation without the need for server-side processing.

# Key Features
* Upload and Process Images: Users can upload images from their local devices and apply a variety of image processing techniques.
* Multiple Operations: Includes operations such as Gaussian Blur, Median Blur, Sharpen, Edge Detection, Noise Reduction, Brightness Adjustment, Contrast Adjustment, Histogram Equalization, Saturation Adjustment, and Gamma Correction.
* Interactive Interface: Simple and intuitive interface with options to adjust intensity for each operation.
* Immediate Feedback: Processed images are displayed in real-time on the canvas, allowing users to instantly see the effects of their selected operations.

This project is ideal for developers, researchers, and enthusiasts looking to explore image processing techniques directly within a web browser environment.
 
# Prerequisites and Dependencies
To run the "Image Processing & Enhancementr" project, ensure you have the following prerequisites and dependencies installed:
1. ### Web Browser:
* Ensure you have a modern web browser that supports HTML5 canvas and JavaScript.
* Recommended browsers include Google Chrome, Mozilla Firefox, or Microsoft Edge.
2. ### OpenCV.js:
* Include the OpenCV.js library in your project. You can use the CDN link provided in your index.html file:
### html
Copy code
```bash
  <script src="https://docs.opencv.org/4.x/opencv.js"></script>
```
- This library provides the core image processing functionalities in JavaScript.
 ### Python (Optional for Alternative Implementation):
- If you choose to use the Python alternative implementation provided, ensure you have Python installed on your system (Python 3.x recommended).
- Required Python packages include tkinter, PIL, opencv-python, and numpy.
### Local Web Server (Optional):
* While not mandatory, using a local web server can prevent issues related to browser security restrictions.
* You can install a simple web server like http-server for Node.js or use Python's built-in http.server.

# Installation Instructions

1. ### Clone the Repository
Clone the GitHub repository to your local machine using Git. Open a terminal and run:
bash
Copy code


```bash
git clone https://github.com/Bhushanmv007/Cgi.git
```

Alternatively, download the repository as a ZIP file and extract it to a local directory.

2. ### Set Up the Project Files
Navigate into the project directory:
bash
Copy code
```bash
cd Cgi
```
3. ### Configure Environment
For Browser-Based Implementation:
### Open the index.html file in a text editor.
Ensure you have an active internet connection to load the OpenCV.js library:
html
Copy code
```bash
<script src="https://docs.opencv.org/4.x/opencv.js"></script>
```

### For Python Alternative (Optional):
Ensure Python 3.x is installed on your system.
Install necessary Python packages using pip:
bash
Copy code
```bash
pip install opencv-python-headless pillow
```

4. ### Run the Application
Using a Web Browser:
Open index.html file in your preferred web browser (Google Chrome, Mozilla Firefox, etc.).
Upload an image using the file input field and apply various image processing operations as per the UI instructions.
Using Python Alternative (Optional):
Run the Python script main.py using Python 3.x:
bash
Copy code
```bash
python main.py
```

The GUI application will open. Use it to load an image file, apply filters or enhancements, and view the processed image.

5. ### Adjust Browser Settings (if necessary)
Ensure your web browser allows local file access to upload images directly from your device.
Adjust browser settings or run the project on a local web server if you encounter issues related to file access or security restrictions.

6. ### Explore and Customize
Explore different image processing operations available in the application.
Customize the project as per your requirements by modifying HTML, CSS, and JavaScript files in the Cgi directory.

# Operations Available
The different options Available are:
* Gaussian Blur
* Median Blur
* Sharpen
* Edge Detection
* Noise Reduction
* Brightness Adjustment
* Contrast Adjustment
* Histogram Equalization
* Saturation Adjustment
* Gamma Correction

# Screenshots

## Upload Interface
![Alt Text](https://github.com/Bhushanmv007/Cgi/blob/master/pictures/interface.png?raw=true)

## Options Selection
![Alt Text](https://github.com/Bhushanmv007/Cgi/blob/master/pictures/operations.png?raw=true)

## Processed Image
![Alt Text](https://github.com/Bhushanmv007/Cgi/blob/master/pictures/processed%20img.png?raw=true)
## License

[MIT](https://github.com/Bhushanmv007/Cgi/blob/master/LICENSE.md)

