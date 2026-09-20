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
varXsum = 0

sumA = 0
sumB = 0
sumC = 0
sumX = 0

for i in range(30000):
    ar_A.append(1+int(random.random()*6))
    sumA+=ar_A[i]
    av_A.append(sumA/(i+1))
    
    ar_B.append(1+int(random.random()*4))
    sumB+=ar_B[i]
    av_B.append(sumB/(i+1))
    
    if int(2*random.random())==0:
        ar_C.append(-1)
    else:
        ar_C.append(1)     
    sumC+=ar_C[i]
    av_C.append(sumC/(i+1))
    
    ar_X.append(ar_A[i]+(ar_B[i]*ar_C[i]))
    sumX+=ar_X[i]
    av_X.append(sumX/(i+1))
    varXsum +=(ar_X[i]-av_X[i])**2
    if i != 0:
        vr_X.append(varXsum/(i))
    else:
         vr_X.append(0)
 
    

# Inspect the following plots.
plt.figure()
plt.hist(ar_A,6,range=(1,7),align='left',density=True, rwidth=0.8,label="A")
plt.legend()
plt.figure()
plt.hist(ar_B,4,range=(1,5),align='left',density=True, rwidth=0.8,label="B")
plt.legend()
plt.figure()
plt.hist(ar_C,3,range=(-1,2),align='left',density=True, rwidth=0.8,label="C")
plt.legend()
plt.figure()
plt.hist(ar_X,14,range=(-3,11),align='left',density=True, rwidth=0.8,label="X")
plt.legend()


# Plot the average and variance values.
plt.figure()
plt.plot(range(30000),av_A,label="Average value of A")
plt.ylim(0, 4)
plt.legend()
plt.figure()
plt.plot(range(30000),av_B,label="Average value of B")
plt.ylim(0, 3)
plt.legend()
plt.figure()
plt.plot(range(30000),av_C,label="Average value of C")
plt.ylim(-1, 1)
plt.legend()
plt.figure()
plt.plot(range(30000),av_X,label="Average value of X")
plt.ylim(0, 4)
plt.legend()
plt.figure()
plt.plot(range(30000),vr_X,label="Variance of X")
plt.ylim(0, 11)
plt.legend()


# Experiment 2

# Part a (Inverse Transform Method)
U = []
Xa = []
av_Xa = []
vr_Xa = []
varXasum = 0

# Populate the given arrays.
sum_Xa = 0
def inv_func(x):
    return x**(1/2)
for i in range(30000):
    U.append(random.random())
    Xa.append(inv_func(U[i]))
    sum_Xa+=Xa[i]
    av_Xa.append(sum_Xa/(i+1))
    
    varXasum +=(Xa[i]-av_Xa[i])**2
    if i != 0:
        vr_Xa.append(varXasum/(i))
    else:
         vr_Xa.append(0)
   

# Inspect the following plots.
plt.figure()
for i in range(len(Xa)):
    plt.plot([Xa[i],U[i]],[1,1.2])
plt.title("Xa")
plt.figure()
hU = plt.hist(U,100,alpha=0.5,density=True,label = "U Histogram")
hXa = plt.hist(Xa,100,alpha=0.5,density=True,label = "Xa Histogram")
plt.legend()
plt.figure()
plt.plot(np.cumsum(hU[0]),label = "U cumulative sum")
plt.plot(np.cumsum(hXa[0]),label = "Xa cumulative sum")
plt.legend()

# Plot the average and variance values.

plt.figure()
plt.plot(range(30000),av_Xa,label = "Average value of Xa")
plt.legend()
plt.figure()
plt.plot(range(30000),vr_Xa,label = "Variance of Xa")
plt.legend()



# Part b (Rejection Method)
Xb = []
av_Xb = []
vr_Xb = []

# Populate the given arrays.
xb_sum = 0
varXbsum = 0
for i in range(30000):
    xb = random.random()
    Xb1= random.random()
    Xb1= Xb1*2
    if xb<Xb1:
        continue
    else:
        Xb.append(xb)
        xb_sum+=xb
        av_Xb.append(xb_sum/len(Xb))
        varXbsum +=(Xb[len(Xb)-1]-av_Xb[len(av_Xb)-1])**2
        if i != 0:
            vr_Xb.append(varXbsum/(len(Xb)))
        else:
            vr_Xb.append(0)
        
# Inspect the following plots.
plt.figure()
hXb = plt.hist(Xb,100,density=True,label = "Xb Histogram")
plt.legend()
plt.figure()
plt.plot(np.cumsum(hXb[0]),label = "Xb cumulative sum")
plt.legend()


# Plot the average and variance values.
### YOUR CODE HERE ###

plt.figure()
plt.plot(range(len(av_Xb)),av_Xb,label = "Average value of Xb")
plt.legend()
plt.figure()
plt.plot(range(len(vr_Xb)),vr_Xb,label = "Variance of Xb")
plt.legend()

plt.show()