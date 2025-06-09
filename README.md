# Assistance of Blind People using OpenCV & Tesseract

This project presents a smart assistive system to support visually impaired individuals in navigating both familiar and unfamiliar environments. It utilizes computer vision techniques, speech synthesis, and distance measurement to provide real-time audio feedback for enhanced independence.

## Overview

The system is designed to detect and recognize objects, extract and read out text from images, measure distances to obstacles, and identify faces. It uses a Raspberry Pi integrated with sensors and a camera, combining OpenCV, Tesseract OCR, and machine learning models to provide accurate and responsive assistance.

## Features

- Object detection using SSD MobileNet and YOLO
- Distance measurement using ultrasonic sensors
- Face recognition using Haar Cascade and landmark estimation
- Text extraction using Tesseract OCR
- Text-to-speech conversion using Google Text-to-Speech (gTTS)
- Real-time voice-based feedback to guide users

## Technologies Used

| Component             | Description                                     |
|----------------------|-------------------------------------------------|
| OpenCV               | Real-time image processing and detection        |
| Tesseract OCR        | Optical character recognition for text in images|
| YOLO / SSD MobileNet | Fast neural networks for object detection       |
| gTTS                 | Google Text-to-Speech API                       |
| Haar Cascade         | Face and facial landmark detection              |
| Raspberry Pi 4       | Central processing hardware                     |
| Ultrasonic Sensor    | For obstacle distance detection                 |
| PyCharm              | Development environment for Python              |

## System Architecture

1. The camera captures input from the surrounding environment.
2. Objects are detected using pre-trained models.
3. Text from images is extracted using Tesseract OCR.
4. The extracted information is converted into speech using gTTS.
5. Ultrasonic sensors detect obstacles and measure distances.
6. Audio output is provided to the user via speakers or earphones.

## Output Screens

- Object Detection
- Text Extraction
- Distance Measurement
- Text-to-Speech Conversion

## Accuracy and Performance

| Function               | Accuracy       |
|------------------------|----------------|
| Object Detection       | 95.19%         |
| Object Recognition     | 99.69%         |
| Navigation System      | Approximately 98% |

## Future Scope

- Expand the dataset with more object types
- Improve object detection accuracy at oblique angles
- Implement a full speech-based command system
- Enhance coverage of indoor navigation with additional landmarks
- Integrate stair and door recognition

## References

Published in:

**International Journal of Innovative Research in Computer and Communication Engineering**  
Volume 11, Issue 1, January 2023  
DOI: [10.15680/IJIRCCE.2023.1101016](http://www.ijircce.com/)

## Authors

- R.M. Vishaalini – UG Student, Department of CSE, Kumaraguru College of Technology  
- V. Senthilkumar – Assistant Professor, Department of CSE, Kumaraguru College of Technology  
- M. Devasenan – UG Student, Department of CSE  
- Gokul S – UG Student, Department of AI & DS

## License

This project is intended for educational and research use only.
