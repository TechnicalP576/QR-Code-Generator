# QR Code Generator
This was my first ever project that i have ever made, i used a combitnation of python, html and css 

Techstack =
Backend = Python 3.13.12, Flask
Frontend = HTML5, CSS3
Libraries: 'qrcode' for image generation and 'os' for file path management

Features =
- Converts any URL into a high-qaulity PNG QR Code
- Automatically saves generated codes to a static directory
- Simple, clean web interface for easy user interaction

How It Works? =
1. Enter a URL of your choice into the web form
2. Flask processes your URL request into QR code by using the 'qrcode' library to create a PNG
3. The app saves the image and displays it back to the user on the screen

Lessons Learned =
When building this QR Code Generator app, i mastered:
- Handling POST requests in Flask
- Managing static folders and CSS linking
- using '.gitignore' to keep my repository clean of temporary files

Screenshots =

Entering the URL:
![Entering URL Screenshot](Entering%20URL%20Screenshot.png)

Generating the QR Code:
![QR Code Generation Screenshot](QR%20Code%20Generation%20Screenshot.png)
---------------------------------------------------------------------------------------------------
Created by TechnicalP576
