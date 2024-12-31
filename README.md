FaceStamp 

A Face Recogination based attendance system

Conventional methods of attendance tracking often suffer from inaccuracies and inefficiencies. Addressing this issue necessitates the implementation of automated systems in organizations and educational institutions. By automating attendance tracking, manual efforts are minimized, and the likelihood of errors is significantly reduced, thereby enhancing overall accuracy and efficiency.

METHODOLOGY

The project methodology involves using facial recognition technology to automate attendance tracking. It employs image processing algorithms, including the Haar Cascade Classifier for face detection and the LPBH model for face recognition. 

Haar cascade employs rectangular patterns called Haar-like features to distinguish between objects and backgrounds. Trained using positive and negative images, it uses a cascade of classifiers to efficiently evaluate regions of an image, identifying potential objects like faces. This method provides a fast and effective approach to face detection by leveraging basic features and sequential evaluation.

Features
Face Detection:Utilize pre-trained deep learning models for accurate face detection in images/videos.
Face Recognition: Train a deep learning model for face recognition. 
Data Collection: Gather a dataset of images containing faces of individuals whose attendance you want to track. 
Data Preprocessing: Preprocess the images by resizing them to a standard size, converting them to grayscale, and normalizing pixel values. 

Project Setup
Prerequisites
Python 3.x installed
Install the required Python libraries by running the following command:
Use the package manager pip to install

pip install tkinter
pip install pip install tkinter
pip install cv2,os
pip install numpy
pip install PIL 
pip install pandas 