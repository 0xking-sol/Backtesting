import pandas as pd

data = pd.read_csv('Final Analysis.csv')

initial_investment = 100

stop_loss_levels = ['Pct Increases 0.001', 'Pct Increases 0.005', 'Pct Increases 0.01', 'Pct Increases 0.02', 'Pct Increases 0.03', 'Pct Increases 0.05', 'Pct Increases 0.1']

for stop_loss_pct in stop_loss_levels:
    data[stop_loss_pct + '_multiplier'] = 1 + data[stop_loss_pct] / 100
    final_investment = data[stop_loss_pct + '_multiplier'].cumprod() * initial_investment
    print(f"Final investment value for {stop_loss_pct}: $", final_investment.iloc[-1])
