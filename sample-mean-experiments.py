import numpy as np
import random
from matplotlib import pyplot as plt

# Experiment 1

ar_A = []
ar_B = []
ar_C = []
ar_X = []

av_A = []
av_B = []
av_C = []
av_X = []
vr_X = []

# Populate the given arrays.
### YOUR CODE HERE ###

# Inspect the following plots.
plt.figure()
plt.hist(ar_A,6,range=(1,7),align='left',density=True, rwidth=0.8)
plt.figure()
plt.hist(ar_B,4,range=(1,5),align='left',density=True, rwidth=0.8)
plt.figure()
plt.hist(ar_C,3,range=(-1,2),align='left',density=True, rwidth=0.8)
plt.figure()
plt.hist(ar_X,14,range=(-3,11),align='left',density=True, rwidth=0.8)

# Plot the average and variance values.
### YOUR CODE HERE ###

# Experiment 2

# Part a (Inverse Transform Method)
U = []
Xa = []
av_Xa = []
vr_Xa = []

# Populate the given arrays.
### YOUR CODE HERE ###

# Inspect the following plots.
plt.figure()
for i in range(len(Xa)):
    plt.plot([Xa[i],U[i]],[1,1.2])
plt.figure()
hU = plt.hist(U,100,alpha=0.5,normed=True)
hXa = plt.hist(Xa,100,alpha=0.5,normed=True)
plt.figure()
plt.plot(np.cumsum(hU[0]))
plt.plot(np.cumsum(hXa[0]))

# Plot the average and variance values.
### YOUR CODE HERE ###


# Part b (Rejection Method)
Xb = []
av_Xb = []
vr_Xb = []

# Populate the given arrays.
### YOUR CODE HERE ###

# Inspect the following plots.
plt.figure()
hXb = plt.hist(Xb,100,normed=True)
plt.figure()
plt.plot(np.cumsum(hXb[0]))

# Plot the average and variance values.
### YOUR CODE HERE ###
