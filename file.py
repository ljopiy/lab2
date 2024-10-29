import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
brainFile = 'brainsize.txt'
brainFrame = pd.read_csv(brainFile, delimiter='\t')


menDf = brainFrame[brainFrame.Gender == 'Male']
womenDf = brainFrame[brainFrame.Gender == 'Female']
womenDf[['FSIQ', 'VIQ', 'PIQ', 'Weight', 'Height', 'MRI_Count']].corr(method='pearson')

mcorr = menDf[['FSIQ', 'VIQ', 'PIQ', 'Weight', 'Height', 'MRI_Count']].corr(method='pearson')

sns.heatmap(mcorr)
plt.show()