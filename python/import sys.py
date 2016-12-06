import scipy.io as sio #remove this?
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import scipy
from scipy.interpolate import PchipInterpolator as pchip
import PCA as PCA
from mpl_toolkits.mplot3d import Axes3D
import hyperalign as hyp


def animator(data):
    
    def is_list(x):
        if type(x[0][0])==np.ndarray:
            return True
        elif type(x[0][0])==np.int64 or type(x[0][0])==int:
            return False
        
    def interp(z):
        x=np.arange(0, len(z), 1)
        xx=np.arange(0, len(z)-1, .1)
        q=pchip(x,z)
        return q(xx)
        #interpolate over the data, for smoothness

    array=np.zeros((data[0].shape[0]*10, 3))
    smoothed=[array]*len(data)
    #make np array of zeros to hold the smoothed data

    for idx, x in enumerate(data):
        smoothed[idx]=PCA.reduc(x, 3)
        smoothed[idx]= interp(smoothed[idx])
        #interpolate over each column in each array of the data
      
        
    def animate2(i):
        ax1.clear()

        for x in smoothed:
            if i<=15:  
                ax1.set_color_cycle(['red','red','red'])
                ax1.view_init(elev=10., azim=i)
                ax1.plot(x[0:i, 0], x[0:i, 1], x[0:i, 2])
                #first plot the just the data
            
                ax1.grid(False)
                ax1.set_xticklabels([])
                ax1.set_yticklabels([])
                ax1.set_zticklabels([])
                #aesthetic
                
            if i>15 and i<18:
                ax1.set_color_cycle(['red','red','red'])
                ax1.view_init(elev=10., azim=i)
                ax1.plot(x[i-15:i, 0], x[i-15:i, 1], x[i-15:i, 2])
                #then, plot only the data through the last 15 data points

                ax1.grid(False)
                ax1.set_xticklabels([])
                ax1.set_yticklabels([])
                ax1.set_zticklabels([])
                #aesthetic

            if i>=18 and i<58:
                ax1.set_color_cycle(['red', 'red','grey','purple','purple','grey','orange','orange','grey'])
                ax1.view_init(elev=10., azim=i)
                ax1.plot(x[i-15:i, 0], x[i-15:i, 1], x[i-15:i, 2])
                ax1.plot(x[i-18:i-15,0],x[i-18:i-15,1],x[i-18:i-15,2], ":")
                ax1.plot(x[0:i-18,0],x[0:i-18,1],x[0:i-18,2], ":")
                #once up to 18, start plotting the data with trailing dots
                
                ax1.grid(False)
                ax1.set_xticklabels([])
                ax1.set_yticklabels([])
                ax1.set_zticklabels([])
                #aesthetic
                
            if i>=58:
                if i<360:
                    ax1.view_init(elev=10., azim=i)
                    #if still under 360 animation frames, use the frame as the camera angle
                else:
                    Az=i-(int(i/360)*360)
                    #if above 360 animation frames, still use animation frame, subtracting 360 appropriate number of times
                    ax1.view_init(elev=10., azim=Az)
                ax1.set_color_cycle(['red', 'red','grey','purple','purple','grey','orange','orange','grey'])
                ax1.plot(x[i-15:i, 0], x[i-15:i, 1], x[i-15:i, 2])
                ax1.plot(x[i-18:i-15,0],x[i-18:i-15,1],x[i-18:i-15,2], ":")
                ax1.plot(x[i-58:i-18,0],x[i-58:i-18,1],x[i-58:i-18,2], ":")
                #once up to 58, start plotting the data with double trailing dots

                ax1.grid(False)
                ax1.set_xticklabels([])
                ax1.set_yticklabels([])
                ax1.set_zticklabels([])

                
    #a = np.zeros((smoothed[0].shape[1],len(smoothed)))
    
    #for idx,s in smoothed:
        #for n in range(0,s.shape[1]):
            #a[idx,0]=max(s[:,0])
            #a[idx,1]=max(s[:,1])
            #a[idx,2]=max(s[:,2])
            
    #^^to control plot size        

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, projection='3d')
    ax1.axes.get_xaxis().set_visible(False)
    ax1.grid(True)

    
    anim=animation.FuncAnimation(fig1, animate2, interval=8, repeat=True)#frames=range(1, len(test_interp)), 
    
    plt.show()
