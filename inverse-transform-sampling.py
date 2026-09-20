# %% Imports
import random
import numpy as np
from matplotlib import pyplot as plt


# %% Functions

# Function to generate a population with given parameter and size using the
# inverse transformation method.
def gen_inverse(k, M):
    a1 = []
    for i in range(M):
        a1.append(random.random()**(1/(k+1)))
    return a1


# Function to generate a population with given parameter and size using the
# rejection method.
def gen_rejection(k, M):
    a1 = []
    while len(a1)<M:
        valx = random.random()
        valy = random.random()
        if valy<=valx**k:
            a1.append(valx)
    return a1


# Function to calculate the population mean using k.
def calc_population_mean(k):
    return ((k+1)/(k+2))


# Function to calculate the population variance using k.
def calc_population_variance(k):
    return (k+1)/((k+3)*((k+2)**2))


# Function to randomly take samples of size N from a population.
def random_sample(population, N):
    sample_array = []
    sample_array_loc = []
    while len(sample_array)<N:
        j = int(random.random()*len(population))
        if(j not in sample_array_loc):
            sample_array.append(population[j])
            sample_array_loc.append(j)
    return sample_array


# Function to calculate the sample mean.
def calc_sample_mean(sample):
    sum=0
    count = 0
    for i in sample:
        sum+=i
        count += 1
    return sum/count
        


# Function to calculate the sample variance (biased/unbiased).
def calc_sample_variance(sample, unbiased=True):
    sum = 0
    mean = calc_sample_mean(sample)
    for i in range(len(sample)):
        sum+= (sample[i] - mean)**2
    return sum/(len(sample)-(1-(int(unbiased))))


# Function to estimate the parameter k using method of moments
def estimate_k_mom(sample):
    mean_samp = calc_sample_mean(sample)
    return ((1-(mean_samp*2))/(mean_samp-1))


# Function to estimate the parameter k using maximum likelihood
def estimate_k_mle(sample):
    sample_ln = np.log(sample)
    sum = np.sum(sample_ln)
    return (-1*(len(sample)/sum))-1


# Function to calculate the confidence interval for population mean given the
# sample and the required confidence level. If population standard deviation is
# not provided, use sample standard deviation as its estimator. As confidence
# level, it should only accept 95, 96, 97, 98 and 99 for which the z values are
# hard-coded in the function.
def calc_conf_int_mean(sample, confidence_lvl, pop_std=0):
    conf_lvl_z = 0
    samp_mean = calc_sample_mean(sample)
    if confidence_lvl == 95:
        conf_lvl_z = 1.645
    elif confidence_lvl == 96:
        conf_lvl_z = 1.755
    elif confidence_lvl == 97:
        conf_lvl_z = 1.885
    elif confidence_lvl == 98:
        conf_lvl_z = 2.055
    elif confidence_lvl == 99:
        conf_lvl_z = 2.325
    if pop_std == 0:
        pop_std = calc_sample_variance(sample)**(1/2)
    return samp_mean-conf_lvl_z*(pop_std/(len(sample)**(1/2))),samp_mean+conf_lvl_z*(pop_std/(len(sample)**(1/2)))


# %% Experiments

# Generate the two populations of size 1000000, calculate and print their means
# and variances and plot the population histograms.
M = 1000000
k_1 = 2.1
k_2 = 3.7
conf_lvl = 97

p1 = gen_inverse(k_1,M)

p2 = gen_rejection(k_2,M)


plt.figure()
hp1 = plt.hist(p1,100,density=True,label = "population 1(p1) Histogram")
plt.legend()

plt.figure()
hp2 = plt.hist(p2,100,density=True,label = "population 2(p2) Histogram")
plt.legend()        



print("p1 mean :"+str(calc_population_mean(k_1)))
print("p2 mean :"+str(calc_population_mean(k_2)))
print("p1 variance :"+str(calc_population_variance(k_1)))
print("p2 variance :"+str(calc_population_variance(k_2)))
# YOUR CODE HERE

# Collect 100000 random samples of size 25 from both populations, calculate
# sample means, biased and unbiased sample variances, MoM and MLE estimates of
# the parameter k and population mean intervals with 97% confidence with and
# without the population standard deviation for each sample of each population.
N = 25
R = 100000

aS1 = []
aS2 = []
for i in range(R):
    aS1.append(random_sample(p1,N))
for i in range(R):
    aS2.append(random_sample(p2,N))
    
aSm1 = []
aSm2 = []


for i in range(R):
    aSm1.append(calc_sample_mean(aS1[i]))
for i in range(R):
    aSm2.append(calc_sample_mean(aS2[i]))
    

aS_ubv1 = []
aS_ubv2 = []

for i in range(R):
    aS_ubv1.append(calc_sample_variance(aS1[i]))
for i in range(R):
    aS_ubv2.append(calc_sample_variance(aS2[i]))
    
     
aS_bv1 = []
aS_bv2 = []

for i in range(R):
    aS_bv1.append(calc_sample_variance(aS1[i],False))
for i in range(R):
    aS_bv2.append(calc_sample_variance(aS2[i],False))
    
    
aS_mom1 = []
aS_mom2 = []

for i in range(R):
    aS_mom1.append(estimate_k_mom(aS1[i]))
for i in range(R):
    aS_mom2.append(estimate_k_mom(aS2[i]))
    
    
aS_mle1 = []
aS_mle2 = []

for i in range(R):
    aS_mle1.append(estimate_k_mle(aS1[i]))
for i in range(R):
    aS_mle2.append(estimate_k_mle(aS2[i]))
    

aS_pmean_ws1 = []
aS_pmean_ws2 = []

for i in range(R):
    aS_pmean_ws1.append([calc_conf_int_mean(aS1[i], 97, calc_population_variance(k_1)**(1/2))])
for i in range(R):
    aS_pmean_ws2.append([calc_conf_int_mean(aS2[i], 97, calc_population_variance(k_2)**(1/2))])
    

aS_pmean_wos1 = []
aS_pmean_wos2 = []

for i in range(R):
    aS_pmean_wos1.append(calc_conf_int_mean(aS1[i], 97))
for i in range(R):
    aS_pmean_wos2.append(calc_conf_int_mean(aS2[i], 97))

# Calculate and print means of sample means, biased and unbiased sample
# variances, MoM and MLE estimates of parameter k and plot the histograms of
# sample means, k estimates using MoM and MLE for both populations.

print("Mean of sample means of population 1:"+str(calc_sample_mean(aSm1)))
print("Mean of sample means of population 2:"+str(calc_sample_mean(aSm2)))

plt.figure()
hp1 = plt.hist(aSm1,100,density=True,label = "p1 mean Histogram")
plt.legend()

plt.figure()
hp1 = plt.hist(aSm2,100,density=True,label = "p2 mean Histogram")
plt.legend()


plt.figure()
hp1 = plt.hist(aS_ubv1,100,density=True,label = "p1 unbiased variance Histogram")
plt.legend()

plt.figure()
hp1 = plt.hist(aS_ubv2,100,density=True,label = "p2 unbiased variance Histogram")
plt.legend()

plt.figure()
hp1 = plt.hist(aS_bv1,100,density=True,label = "p1 biased variance Histogram")
plt.legend()

plt.figure()
hp1 = plt.hist(aS_bv2,100,density=True,label = "p2 biased variance Histogram")
plt.legend()


plt.figure()
hp1 = plt.hist(aS_mom1,100,density=True,label = "p1 k estimates using method of moments Histogram")
plt.legend()

plt.figure()
hp1 = plt.hist(aS_mom2,100,density=True,label = "p2 k estimates using method of moments Histogram")
plt.legend()


plt.figure()
hp1 = plt.hist(aS_mle1,100,density=True,label = "p1 k estimates using maximum likelihood Histogram")
plt.legend()

plt.figure()
hp1 = plt.hist(aS_mle2,100,density=True,label = "p2 k estimates using maximum likelihood Histogram")
plt.legend()



# Collect a sample of length 100000*25 from both populations, calculate and
# print their sample means, biased and unbiased sample variances, MoM and MLE
# estimates of parameter k and confidence intervals with and without using the
# population standard deviation.

p3 = gen_inverse(k_1,2500000)

p4 = gen_rejection(k_2,2500000)


aS3 = []
for i in range(R):
    aS3.extend(random_sample(p3,N))

aS4 = []
for i in range(R):
    aS4.extend(random_sample(p4,N))

print("sample 3 mean (sample 3 produced from p3) :"+str(calc_sample_mean(aS3)))
print("sample 4 mean (sample 4 produced from p4) :"+str(calc_sample_mean(aS4)))

print("sample 3 unbiased variance :"+str(calc_sample_variance(aS3)))
print("sample 4 unbiased variance :"+str(calc_sample_variance(aS4)))

print("sample 3 biased variance :"+str(calc_sample_variance(aS3,False)))
print("sample 4 biased variance :"+str(calc_sample_variance(aS4,False)))

print("sample 3 k estimation using method of moments :"+str(estimate_k_mom(aS3)))
print("sample 4 k estimation using method of moments :"+str(estimate_k_mom(aS4)))

print("sample 3 k estimation using method of maximum likelihood :"+str(estimate_k_mle(aS3)))
print("sample 4 k estimation using method of maximum likelihood :"+str(estimate_k_mle(aS4)))

print("sample 3 confidence interval for the mean value of population calculated while population variance is known :"+str(calc_conf_int_mean(aS3,97,(calc_population_variance(k_1)**(1/2)))))
print("sample 4 confidence interval for the mean value of population calculated while population variance is known :"+str(calc_conf_int_mean(aS4,97,(calc_population_variance(k_2)**(1/2)))))

print("sample 3 confidence interval for the mean value of population calculated while population variance is not known :"+str(calc_conf_int_mean(aS3,97)))
print("sample 4 confidence interval for the mean value of population calculated while population variance is not known :"+str(calc_conf_int_mean(aS4,97)))

# YOUR CODE HERE
plt.show()