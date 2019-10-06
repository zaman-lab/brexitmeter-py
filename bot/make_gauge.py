import matplotlib.pyplot as plt
from PIL import Image
import math
import time

# function plotting a colored dial
def plotGauge2(score,figname):

    # create figure and specify figure name
    fig, ax = plt.subplots()
    # ax.set_aspect('equal')

    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    im=Image.open('up_gauge.png')
    width, height = im.size
    ax.imshow(im)

    arrow_angle = (score*1000/float(1000))*3.14159
    arrow_x = -height/2*math.cos(arrow_angle)
    arrow_y = -height/2*math.sin(arrow_angle)
    ax.arrow(width/2,height,arrow_x,arrow_y, width=width/200, head_width=height/10, \
        head_length=2*height/10, fc='k', ec='k')

    if(score>=0.5):
        plt.text(x = width/2*(1-0.3*math.cos(0.5*arrow_angle)), y = height/2*(1-0.3*math.sin(0.5*arrow_angle)), s = str(int(score*100))+'% ', size = 15, fontweight='bold')
    else:
        plt.text(x = width/2*(1-0.3*math.cos(1*arrow_angle)), y = height/2*(1-0.3*math.sin(1*arrow_angle)), s = str(int(score*100))+'%', size = 15, fontweight='bold')

    t=str(int(time.time()))
    plt.savefig('plots/'+figname+'_'+t+'.png', bbox_inches='tight',pad_inches=0.5) 
    return figname+'_'+t+'.png'
     

