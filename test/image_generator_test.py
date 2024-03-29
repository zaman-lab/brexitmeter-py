
import os
from matplotlib import pyplot as plt
#from matplotlib.figure import Figure
#from matplotlib.axes import AxesSubplot # or something

from app.image_generator import save_brexit_image

def test_save_brexit_image():
    mock_img_filepath = os.path.join(os.path.dirname(__file__), "img", "mock_dial.png")

    # setup:
    if os.path.isfile(mock_img_filepath):
        os.remove(mock_img_filepath)
    assert not os.path.isfile(mock_img_filepath)

    img_filepath = save_brexit_image(0.99, mock_img_filepath)
    assert img_filepath == mock_img_filepath
    assert os.path.isfile(mock_img_filepath)
