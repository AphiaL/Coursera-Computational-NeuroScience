"""
Created on Wed Apr 22 15:21:11 2015

Code to compute spike-triggered average.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def compute_sta(stim, rho, num_timesteps):
    """Compute the spike-triggered average from a stimulus and spike-train.

    Args:
        stim: stimulus time-series. 
        notive that The stimulus you have been provided with is the velocity of a random 
        bar pattern like this that moves back and forth on a screen in front of the fly. 
        The stimulus is created by choosing a random velocity (either positive or negative) every 2 milliseconds. 
        The screen then moves with that velocity for 2 ms. This is an example of a “white noise” stimulus. 
        
        rho: spike-train time-series
        num_timesteps: how many timesteps to use in STA

    Returns:
        spike-triggered average for num_timesteps timesteps before spike"""

    sta = np.zeros((num_timesteps,)) #np.array will return a new array of given shape and type, filled with zeros.

    # This command finds the indices of all of the spikes that occur
    # after 300 ms into the recording.
    spike_times = rho[num_timesteps:].nonzero()[0] + num_timesteps

    # Fill in this value. Note that you should not count spikes that occur
    # before 300 ms into the recording.
    num_spikes = len(spike_times) #calculating the number of spikes, which equals to the number of all the 300ms windows
    print(num_spikes)
    # Compute the spike-triggered average of the spikes found.
    # To do this, compute the average of all of the vectors
    # starting 300 ms (exclusive) before a spike and ending at the time of
    # the event (inclusive). Each of these vectors defines a list of
    # samples that is contained within a window of 300 ms before each
    # spike. The average of these vectors should be completed in an
    # element-wise manner.
    #
    # Your code goes here.
    for i in range(num_spikes):
        windows = stim[(spike_times[i] - num_timesteps):spike_times[i]]
        sta = sta+windows #sum up all the stimulus in the 300ms window preceidng a spike
    sta = sta/num_spikes #calculating average sta
    return sta
