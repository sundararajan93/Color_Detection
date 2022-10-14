# Color Detection on Images

This piece of code would be very helpful in detecting the colors in a particular image at particular pixel position. We are tracking the mouse pointer double click event to capture the pixel from the image and identify the RGB value of the pixel. This RGB value later look up into the 'colors.csv' file which has nearly 900 colors and it's color code with the color name. Using the colors dataset our tool would find up the near matching color and show the name of the color along with its RGB value.

### Requirements

I used cv2 module (opencv) to read the image file and pandas library to open up the csv file and look for the colors. Since they are primary requirements to run this program you would need those module. we can install both the modules through pip

```
pip install pandas
pip install opencv-python
```

### Usage

```
python3 color_detection.py
```

Once we execute the program it asks for the user input to provide the image file path. Provide the path of the image like the below screenshot and hit enter. 

![running](https://i.imgur.com/B6UXoQm.png)

After few seconds the image given would open in a resized window. We resized this window to a fixed height and width to work with any image resolution at any size. 

![color detection](https://i.imgur.com/yYzaBpA.png)

Double click on any color in the image window to identify the color name with its RGB value

![color detection](https://i.imgur.com/npfjyQA.png)
