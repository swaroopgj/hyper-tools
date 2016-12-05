import sys
sys.path.append('../')
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import scipy
from scipy.interpolate import PchipInterpolator as pchip
import PCA as PCA
#import matplotlib as mpl
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
    
    if is_list(data):
        array=np.zeros(data[0].shape)
        smoothed=[array]*len(data)
    else:
        array=np.zeros(data.shape)
        smoothed=[array]*len(data)

    for idx, x in enumerate(data):
        rows=data[idx].shape[0]

        smoothed[idx]=np.zeros((rows*10,3))
        smoothed[idx]=PCA.reduc(x, 3)
        smoothed[idx]= interp(smoothed[idx])
      
        
    def animate2(i):
        ax1.clear()
        #ax2.clear()

        #ax1.set_color_cycle(['red', 'red','grey','purple','purple','grey','orange','orange','grey'])
        #ax2.set_color_cycle(['black'])

        for x in smoothed:
            if i<=15:  
                ax1.set_color_cycle(['red','red','red'])
                ax1.view_init(elev=10., azim=i)
                ax1.plot(x[0:i, 0], x[0:i, 1], x[0:i, 2])
            
                ax1.grid(False)
                ax1.set_xticklabels([])
                ax1.set_yticklabels([])
                ax1.set_zticklabels([])
                
            if i>15 and i<18:
                ax1.set_color_cycle(['red','red','red'])
                ax1.view_init(elev=10., azim=i)
                ax1.plot(x[i-15:i, 0], x[i-15:i, 1], x[i-15:i, 2])
                
                ax1.grid(False)
                ax1.set_xticklabels([])
                ax1.set_yticklabels([])
                ax1.set_zticklabels([])
        
            if i>=18 and i<58:
                ax1.set_color_cycle(['red', 'red','grey','purple','purple','grey','orange','orange','grey'])
                ax1.view_init(elev=10., azim=i)
                ax1.plot(x[i-15:i, 0], x[i-15:i, 1], x[i-15:i, 2])
                ax1.plot(x[i-18:i-15,0],x[i-18:i-15,1],x[i-18:i-15,2], ":")
                ax1.plot(x[0:i-18,0],x[0:i-18,1],x[0:i-18,2], ":")
                
                ax1.grid(False)
                ax1.set_xticklabels([])
                ax1.set_yticklabels([])
                ax1.set_zticklabels([])
                
            if i>=58:
                if i<360:
                    ax1.view_init(elev=10., azim=i)
                else:
                    Az=i-(int(i/360)*360)
                    ax1.view_init(elev=10., azim=Az)
                ax1.set_color_cycle(['red', 'red','grey','purple','purple','grey','orange','orange','grey'])
                ax1.plot(x[i-15:i, 0], x[i-15:i, 1], x[i-15:i, 2])
                ax1.plot(x[i-18:i-15,0],x[i-18:i-15,1],x[i-18:i-15,2], ":")
                ax1.plot(x[i-58:i-18,0],x[i-58:i-18,1],x[i-58:i-18,2], ":")
                
                ax1.grid(False)
                ax1.set_xticklabels([])
                ax1.set_yticklabels([])
                ax1.set_zticklabels([])

                
    a = np.zeros((smoothed[0].shape[1],len(smoothed)))
    
    #for idx,s in smoothed:
        #for n in range(0,s.shape[1]):
            #a[idx,0]=max(s[:,0])
            #a[idx,1]=max(s[:,1])
            #a[idx,2]=max(s[:,2])
            
            

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, projection='3d')
    ax1.axes.get_xaxis().set_visible(False)
    ax1.grid(True)
    ax1.set_xticklabels([])
    #ax1.auto_scale_xyz(100,100,100)

    #for ii in xrange(0,360,1):
        #ax.view_init(elev=10., azim=ii)
        #savefig("movie%d.png" % ii)
    
    anim=animation.FuncAnimation(fig1, animate2, interval=8, repeat=True)#frames=range(1, len(test_interp)), 
    
    plt.show()
