# %% Imports
import random
import numpy as np
from matplotlib import pyplot as plt


# %% Functions

# Function to generate a population with given parameter and size using the
# inverse transformation method.
def gen_inverse(k, M):
    pass


# Function to generate a population with given parameter and size using the
# rejection method.
def gen_rejection(k, M):
    pass


# Function to calculate the population mean using k.
def calc_population_mean(k):
    pass


# Function to calculate the population variance using k.
def calc_population_variance(k):
    pass


# Function to randomly take samples of size N from a population.
def random_sample(population, N):
    pass


# Function to calculate the sample mean.
def calc_sample_mean(sample):
    pass


# Function to calculate the sample variance (biased/unbiased).
def calc_sample_variance(sample, unbiased=True):
    pass


# Function to estimate the parameter k using method of moments
def estimate_k_mom(sample):
    pass


# Function to estimate the parameter k using maximum likelihood
def estimate_k_mle(sample):
    pass


# Function to calculate the confidence interval for population mean given the
# sample and the required confidence level. If population standard deviation is
# not provided, use sample standard deviation as its estimator. As confidence
# level, it should only accept 95, 96, 97, 98 and 99 for which the z values are
# hard-coded in the function.
def calc_conf_int_mean(sample, confidence_lvl, pop_std=0):
    pass


# %% Experiments

# Generate the two populations of size 1000000, calculate and print their means
# and variances and plot the population histograms.
M = 1000000
k_1 = 2.1
k_2 = 3.7
conf_lvl = 97

# YOUR CODE HERE

plt.figure()
# YOUR CODE HERE

# Collect 100000 random samples of size 25 from both populations, calculate
# sample means, biased and unbiased sample variances, MoM and MLE estimates of
# the parameter k and population mean intervals with 97% confidence with and
# without the population standard deviation for each sample of each population.
N = 25
R = 100000

# YOUR CODE HERE

# Calculate and print means of sample means, biased and unbiased sample
# variances, MoM and MLE estimates of parameter k and plot the histograms of
# sample means, k estimates using MoM and MLE for both populations.

# YOUR CODE HERE

plt.figure()
# YOUR CODE HERE

plt.figure()
# YOUR CODE HERE

plt.figure()
# YOUR CODE HERE

# Calculate and print the ratio of confidence intervals computed with and
# without using the population standard deviation that contains the population
# mean for both populations.

# YOUR CODE HERE

print('*'*50)
# Collect a sample of length 100000*25 from both populations, calculate and
# print their sample means, biased and unbiased sample variances, MoM and MLE
# estimates of parameter k and confidence intervals with and without using the
# population standard deviation.

# YOUR CODE HERE
