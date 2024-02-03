#%%
import pandas as pd 

data = pd.read_csv('./data/2024-01-31_growth_curves_raw.csv', skiprows=19)
data = data[::5][1:]
data['time'] -= data['time'].min()

VESSELS = {1: {530: 0, 660: 300},
           2: {530: 25, 660:0},
           3: {530: 50, 660:0},
           4: {530: 75, 660:0},
           5: {530: 100, 660:0},
           6: {530: 150, 660:0},
           7: {530: 200, 660:0},
           8: {530:0, 660:0}}

df = pd.DataFrame([])
for v_id, v_inf in VESSELS.items():
    _df = data[['time', f'od-sensors-{v_id}.od-680 ']].copy()
    _df['vessel'] = v_id
    _df['strain'] = 'GC123'
    _df['carbon_source'] = 'acetate'
    _df['530nm_uE'] = v_inf[530]
    _df['660nm_uE'] = v_inf[660]
    _df.rename(columns={f'od-sensors-{v_id}.od-680 ':'od_680nm',
                        'time': 'elapsed_time_hr'},
                        inplace=True)
    df = pd.concat([df, _df], sort=False)
df.to_csv('./output/2024-01-31_processed_growth_curves.csv', index=False)

# %%
