#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import size.viz 
cor, pal = size.viz.matplotlib_style()
fluo_data = pd.read_csv('./output/2024-01-31_processed_plate_reader.csv')

fig, ax = plt.subplots(1,2, figsize=(4, 2))
for g, d in fluo_data.groupby('660nm_uE'):
    d.sort_values(by='530nm_uE', inplace=True)
    if g > 0:
        color = cor['primary_red']
    else:
        color = cor['primary_blue']
    ax[0].plot(d['530nm_uE'], d['535nm_per_od'], '-o', color=color, label=f'660nm: {g} µE')
    ax[1].plot(d['530nm_uE'], d['fold-change'], '-o', color=color, label=f'660nm: {g} µE')

for a in ax:
    a.set_xlabel('530nm illumination [µE]', fontsize=6)
    a.legend(fontsize=5)
ax[0].set_ylabel('GFP fluorescence per OD$_{600nm}$ [a.u.]', fontsize=6)
ax[1].set_ylabel('fold-change in GFP [a.u.]', fontsize=6)
plt.savefig('./output/2024-01-31_foldchange_analysis.png', bbox_inches='tight')