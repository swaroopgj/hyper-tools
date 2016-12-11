#!/usr/bin/env python

from __future__ import division
import numpy as np
from scipy.spatial.distance import pdist
from scipy.spatial.distance import cdist
from .align import *
from .helpers import reduceD, reduceD_list
import scipy.spatial.distance as sd

import seaborn as sns
sns.set(style="darkgrid")

def describe(x, include=[None]):

    ##SUB FUNCTIONS##

    def align_summary(x):

        if type(x) is not list:
            print('Must pass a list of arrays.')

        def compute_a(x):
            dists= []
            for xidx,xi in enumerate(x):
                x_cov = 1 - pdist(xi,'correlation')
                y_cov = 1 - pdist(np.mean(np.array([yi for yidx,yi in enumerate(x) if yidx!=xidx]),0),'correlation')
                dists.append(sd.cdist(sd.squareform(x_cov), sd.squareform(y_cov), 'cosine'))
            return np.mean(dists)

        before = compute_a(x)
        x_aligned = align(x)
        after = compute_a(x_aligned)

        return 1 - np.exp(-((before / after) - 1))

    def PCA_summary(x):
        if type(x) is list:
            x = np.vstack(x)
        cov_alldims = pdist(x,'correlation')
        cov_PCA =  [(pdist(reduceD(x,num),'correlation')) for num in range(2,x.shape[1]+1)]
        return [np.corrcoef(cov_alldims, cov_PCA_i)[0][1] for cov_PCA_i in cov_PCA]

    if type(x) is list:
        pass
    else:
        x = [x]

    attrs = {}

    if 'PCA' in include or include==[None]:
        attrs['PCA_summary'] = {}
        attrs['PCA_summary']['average'] = PCA_summary(x)
        attrs['PCA_summary']['individual'] = [PCA_summary(x_i) for x_i in x]

    if 'align' in include or include==[None]:
        attrs['Align_summary'] = [align_summary([reduceD(i,num) for i in x]) for num in range(2,10)]

    return attrs
