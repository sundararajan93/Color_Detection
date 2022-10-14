import pandas as pd
import cv2


# image_path = "image.jpg"
image_path = input("Enter the Image path: ")


# creating index to the csv file
index = ["Color", "Color Name", "Hex Value", "R", "G", "B"]
# Reading the csv file
df = pd.read_csv("colors.csv", names=index, header=None)

# # Slicling the csv for particular index, value
# print(df.head(10))
# print(df.loc[9])
# print(df.loc[9,"Color Name"])

# Reading the image
img = cv2.imread(image_path)

# Resizing image 
img = cv2.resize(img, (900, 600))

clicked = False
r = g = b = xpos = ypos = 0

# functions
def get_color(R,G,B):
    minimum = 1000
    for i in range(len(df)):
        data = abs(R - int(df.loc[i, 'R'])) + abs(G - int(df.loc[i, 'G'])) + abs(B - int(df.loc[i, 'B']))
        if data <= minimum:
            minimum = data
            cname = df.loc[i, 'Color Name']
    return cname

def click_function(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global clicked, r, g, b, xpos, ypos
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

cv2.namedWindow(image_path)
cv2.setMouseCallback(image_path, click_function)

# # Reading the image pixels
# print(img)

# Creating the window with name and show the image window in the display
while True:
    cv2.imshow(image_path, img)

    if clicked:
        # print("Clicked!!!")
        cv2.rectangle(img, (20,20), (850, 70), (b, g, r), -1)
        text = f"Color name - {get_color(r,g,b)} RGB - {r,g,b}"
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0,0,0), 1, cv2.LINE_AA)

    if cv2.waitKey(1) & 0xFF == 27:
        break
