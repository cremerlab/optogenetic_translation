#%%
import numpy as np 
import pandas as pd 
import scipy.stats
import matplotlib.pyplot as plt 
import size.viz  # Replace to opto
cor, pal = size.viz.matplotlib_style()

data = pd.read_csv('./output/2024-01-31_processed_growth_curves.csv')

# Clip the elapsed time to only after 15 hours of growth
data = data[data['elapsed_time_hr'] > 15]
data['elapsed_time_hr'] -= data['elapsed_time_hr'].min()


# Instantiate a storage datafram
growth_df = pd.DataFrame([])

# Define the time range over which to calculate the fit
time_range = np.linspace(0, 1.1 * data['elapsed_time_hr'].max(), 200)

# Make a plot of all of the growth curves and a linear regression
fig, ax = plt.subplots(2, 4, figsize=(6, 4), sharex=True, sharey=True)

# Set scales and labels
for a in ax.ravel():
    a.set_yscale('log')
for i in range(2):
    ax[i, 0].set_ylabel('OD$_{680nm}$ [a.u.]', fontsize=6)
for i in range(4):
    ax[1, i].set_xlabel('elapsed time [hr]', fontsize=6)
ax = ax.ravel()

# Iterate over each vessels, fit, and plot
for g, d in data.groupby(['vessel', '530nm_uE', '660nm_uE']):
    # Compute the fit of the growth rate
    popt = scipy.stats.linregress(d['elapsed_time_hr'], np.log(d['od_680nm'].values))
    fit = popt[1] + popt[0] * time_range
    _ax = ax[int(g[0] - 1)]
    _ax.plot(d['elapsed_time_hr'], d['od_680nm'].values, 'o', label='data', ms=3, 
             color=cor['primary_black'], markeredgewidth=0)
    _ax.plot(time_range, np.exp(fit), '-', color=cor['primary_red'], lw=1, 
             label=f'$\lambda$ = {popt[0]:0.3f}' + ' hr$^{-1}$')
    _ax.set_title(f'530nm: {g[1]} µE, 660nm: {g[2]} µE', fontsize=6)
    _ax.legend(fontsize=5)

    # Define the dataframe of growth rates and store
    _df  = pd.DataFrame([{'vessel':g[0], 
            '530nm_uE': g[1],
            '660nm_uE': g[2],
            'growth_rate_hr': popt[0],
            'od_680nm_init': np.exp(popt[1])}], index=[0])
    growth_df = pd.concat([growth_df, _df], sort=False)


# Save the figure and the growth rate table.
plt.subplots_adjust(hspace=0.08, wspace=0.1)
plt.savefig('./output/2024-01-31_growth_curves.png', bbox_inches='tight')
growth_df.to_csv('./output/2024-01-31_growth_rates.csv', index=False)
