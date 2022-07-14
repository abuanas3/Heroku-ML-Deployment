
#-------------- Python 3.7 ------------------#
# Lets import loadmat required to import .mat files
from scipy.io import loadmat
# Of course we also need signal from Scipy too
from scipy import signal
# Importing numpy to make it possible to perform vector operations
import numpy as np
# These two libraries are for visualization
import matplotlib.pyplot as plt
from pandas import Series
import pandas as pd
import os
import seaborn as sns
from numpy import asarray
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from csv import writer
import csv
from pandas import read_csv
from pandas import DataFrame


def BandPassECG(Path,Fs):
    '''
    This function takes in a "path" and imports the ECG signal in .mat format
    '''
    # Import the signal
    #ECG    = loadmat(Path)['EKG5']
    ECG    = pd.read_csv(Path)
    # Implementing the Butterworth BP filter
    W1     = 5*2/Fs                                    # --> 5 Hz cutt-off (high-pass) and Normalize by Sample Rate
    W2     = 15*2/Fs                                   # --> 15 Hz cutt-off (low-pass) and Normalize by Sample Rate
    b, a   = signal.butter(4, [W1,W2], 'bandpass')     # --> create b,a coefficients , since this is IIR we need both b and a coefficients
    ECG    = np.asarray(ECG)                           # --> let's convert the ECG to a numpy array, this makes it possible to perform vector operations 
    ECG    = np.squeeze(ECG)                           # --> squeeze
    ECG_BP = signal.filtfilt(b,a,ECG)    # --> filtering: note we use a filtfilt that compensates for the delay
    return ECG_BP,ECG

def Differentiate(ECG):
    '''
    Compute single difference of the signal ECG
    '''
    ECG_df  = np.diff(ECG)
    ECG_sq  = np.power(ECG_df,2)
    return np.insert(ECG_sq,0, ECG_sq[0])

def MovingAverage(ECG,N=30):
    '''
    Compute moving average of signal ECG with a rectangular window of N
    '''
    window  = np.ones((1,N))/N
    ECG_ma  = np.convolve(np.squeeze(ECG),np.squeeze(window))
    return ECG_ma

def QRSpeaks(ECG,Fs):
    '''
    Finds peaks in a smoothed signal ECG and sampling freq Fs.
    '''
    peaks, _  = signal.find_peaks(ECG, height=np.mean(ECG), distance=round(Fs*0.200))
  
    return peaks

# Load and BP the Signal
ECG    = pd.read_csv("myfile1.csv")
#Fs =(len(ECG)//10)+1
Fs=250
print (Fs)
#Fs =300
#Path ='F:\\MATLAB\\bin\\ecg digitization\\myfile1.csv'
#====================================scaling================================================
path1 = read_csv('myfile1.csv', header=None)


trans = MinMaxScaler()
data = trans.fit_transform(path1)
#===============================remove zero from data=================
l=list(filter(lambda num: num != 0, data))
data2 = DataFrame(l)
data2.to_csv('myfile11.csv',header=False, index=False)
#=============================================================================================
Path ='myfile11.csv'
# BP Filter
ECG_BP,ECG_raw = BandPassECG(Path,Fs)


# Difference Filter
ECG_df = Differentiate(ECG_BP)

# Moving Average
ECG_ma = MovingAverage(ECG_df)

# QRS peaks
QRS = QRSpeaks(ECG_ma,Fs)


#==========================Plot figure======================
fig = plt.figure(frameon="False") 
plt.title("Detected peaks in signal")
plt.plot(np.arange(ECG_raw.shape[0])/Fs,ECG_raw,color='blue',label='ECG')
#=======================remove figure if exist===========
if os.path.exists('static\\QRS_pks.png'):
    os.remove('static\\QRS_pks.png')
#======================================================
plt.vlines(x=(QRS-15)/Fs,ymin=np.min(ECG_raw),ymax=np.max(ECG_raw),linestyles='dashed',color='r', label='QRS',linewidth=2.0)
plt.ylabel('Amp'); plt.xlabel('Time[S]'); plt.legend()
plt.tight_layout(); plt.show()
fig.savefig('static\\QRS_pks.png', transparent=True)
#=======================get 187 rows from dataframe==========
df = pd.read_csv("myfile11.csv")
data=df.head(187)
list=data[data.columns[0]]

list.to_csv("myfile2.csv", index=False)


#===================================END CODE FLAG================ 
df = pd.read_csv("myfile2.csv")

list1=df[df.columns[0]]

 
with open('myfile4.csv', 'w',newline='') as ff:
    # create the csv writer
    writer = csv.writer(ff)
    
    writer.writerow(list1)
    # write a row to the csv file
    writer.writerow(list1)
   
    ff.close()
#=================================================================
#=======================Compute heart rate====================
RR_list = []
cnt = 0
while (cnt < (len(QRS)-1)):
    RR_interval = (QRS[cnt+1] - QRS[cnt]) #Calculate distance between beats in # of samples
    ms_dist = ((RR_interval / Fs) * 1000.0) #Convert sample distances to ms distances
    RR_list.append(ms_dist) #Append to list
    cnt += 1

bpm =int( 60000 / np.mean(RR_list)) #60000 ms (1 minute) / average R-R interval of signal
print("\n\n\nAverage Heart Beat is: %.01f\n" %(bpm)) #Round off to 1 decimal and print
print("No of peaks in sample are {0}".format(len(QRS)))
#=======================================================================
