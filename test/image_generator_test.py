
import os
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
#from matplotlib.axes import AxesSubplot

from app.image_generator import brexit_image

def test_brexit_image():

    mock_img_filepath = os.path.join(os.path.dirname(__file__), "img", "mock_dial.png")

    if os.path.isfile(mock_img_filepath):
        os.remove(mock_img_filepath)
    assert not os.path.isfile(mock_img_filepath)

    img_filepath, fig, ax = brexit_image(0.99, mock_img_filepath)

    assert isinstance(fig, Figure)
    #assert isinstance(ax, matplotlib.axes._subplots.AxesSubplot)
    assert img_filepath == mock_img_filepath
    assert os.path.isfile(mock_img_filepath)
