import numpy as np
<<<<<<< HEAD
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy
from scipy.interpolate import PchipInterpolator as pchip
from mpl_toolkits.mplot3d import Axes3D
import hyperalign as hyp
=======
>>>>>>> 71f5a3da4751783d9d54923142580348108437ee
from sklearn.decomposition import PCA
import csv
import time


def stream(raw_file, pca_file, seconds, rate):

    ##VARIABLES##
<<<<<<< HEAD

    required_lines=seconds*rate #required lines before computing PCA
    sleep_secs=1/rate #seconds to sleep before checking for new data
    head=6 #number of header rows
    chan=1 #number of leading channel-info cols
=======
    
    required_lines = np.ceil(seconds*rate) #required lines before computing PCA

    sleep_secs = 1.0 / rate #seconds to sleep before checking for new data
    head = 3 #number of header rows
    chan = 1 #number of leading channel-info cols
>>>>>>> 71f5a3da4751783d9d54923142580348108437ee

    #session_secs=600
    #set this parameter and change commenting in last while loop for predefined session length


####################################


    num_lines=open(raw_file).read().count('\n')

    while num_lines==0:
        time.sleep(sleep_secs)
        num_lines=open(raw_file).read().count('\n')
        #if no data, rest

    while num_lines != required_lines:
        time.sleep(sleep_secs)
        num_lines=open(raw_file).read().count('\n')
        #while there is data, but not enough for PCA, rest


    csv1 = np.genfromtxt(raw_file, delimiter=",")
    x1=csv1[head:,chan:] #x1 is raw data minus header and channel info
    m=PCA(n_components=3, whiten=True)
    m.fit(x1)
    #compute PCA


    out= m.transform(x1[-1,:])
    out = [int(x) for x in out]
    w = csv.writer(open(pca_file,'a'),dialect='excel')
    w.writerows(out)
    #write out the last PCA interval datapoint as first plot point


    num_lines2=open(pca_file).read().count('\n')
    #while num_lines2 < session_secs*rate :
    while True:
        csv_stream = np.genfromtxt(raw_file, delimiter=",")
        csv_pca = np.genfromtxt(pca_file, delimiter=",")


        p=m.transform(csv_stream[-1,:])
        w = csv.writer(open(pca_file,'a'),dialect='excel')
        w.writerows(p)
        time.sleep(sleep_secs)
    #num_lines2=open(pca_file).read().count('\n')
