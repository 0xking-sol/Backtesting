import pandas as pd

# Read the CSV file
data = pd.read_csv('Final Analysis.csv')

# Calculate the win rate for each stop loss level
win_rates = {}
for col in data.columns[5:12]:
    win_count = data[data[col] > 0].shape[0]
    total_count = data.shape[0]
    win_rate = (win_count / total_count) * 100
    win_rates[col] = win_rate

# Print the win rates
for key, value in win_rates.items():
    print(f'{key}: {value:.2f}%')
