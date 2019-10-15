import os
import math
import time

import matplotlib.pyplot as plt
from PIL import Image

from app import APP_ENV

IMG_DIRPATH = os.path.join(os.path.dirname(__file__), "..", "img")
BASE_IMG_FILEPATH = os.path.abspath(os.path.join(IMG_DIRPATH, "up_gauge.png"))

def save_brexit_image(score, img_filepath=None):
    """
    Plots a colored dial from 0 to 1, with an arrow marking the specific polarity score in-between.
    Saves the image to the desired filepath.
    Params:
        score (float) between 0 and 1, like 0.55
        img_filepath (str) optional
    """

    if not img_filepath:
        timestamp = str(int(time.time())) #> 1571164912
        img_filepath = os.path.join(IMG_DIRPATH, "plots", f"dial_{timestamp}.png")

    fig, ax = plt.subplots()

    # ax.set_aspect('equal')
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    base_img = Image.open(BASE_IMG_FILEPATH)
    width, height = base_img.size #> 1976, 706
    ax.imshow(base_img)

    arrow_angle = (score*1000/float(1000)) * 3.14159
    arrow_x = - height / 2 * math.cos(arrow_angle)
    arrow_y = - height / 2 * math.sin(arrow_angle)
    ax.arrow(width / 2, height, arrow_x, arrow_y,
        width = width / 200,
        head_width = height / 10,
        head_length = 2 * height / 10,
        fc="k",
        ec="k"
    )

    if(score>=0.5):
        plt.text(
            x = width/2*(1-0.3*math.cos(0.5*arrow_angle)),
            y = height/2*(1-0.3*math.sin(0.5*arrow_angle)),
            s = str(int(score*100))+'% ',
            size = 15,
            fontweight="bold"
        )
    else:
        plt.text(
            x = width/2*(1-0.3*math.cos(1*arrow_angle)),
            y = height/2*(1-0.3*math.sin(1*arrow_angle)),
            s = str(int(score*100))+'%',
            size = 15,
            fontweight="bold"
        )

    plt.savefig(img_filepath, bbox_inches="tight", pad_inches=0.5)

    return img_filepath #, fig, ax

if __name__ == "__main__":

    if APP_ENV is not "production":

        polarity = 0.44
        polarity_input = input("Please choose a polarity score between 0 and 1 (e.g. 0.44): ")
        if polarity_input != "":
            polarity = float(polarity_input)

        img_filepath = save_brexit_image(polarity) #> matplotlib.pyplot
        print(os.path.abspath(img_filepath))
        plt.show()
