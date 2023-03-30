import pandas as pd

df = pd.read_csv('YourFileHere')

final_Df = df.filter(['Date', 'User', 'Tickers', 'Price after 5 seconds'])

stop_loss_percentages = [0.001, 0.005, 0.01, 0.02, 0.03, 0.05, 0.1]

for index, row in df.iterrows():
    if isinstance(row['Tickers'], str):
        price = row['Price after 5 seconds']
        stop_loss_prices = [price * (1 - percentage) for percentage in stop_loss_percentages]

        for stop_loss_price, percentage in zip(stop_loss_prices, stop_loss_percentages):
            current_stop_loss_price = stop_loss_price
            pct_increase = None
            low_price = row['Low 1']
            high_price = row['High 1']

            for i in range(1, 51):
                if low_price <= stop_loss_price:
                    pct_increase = ((stop_loss_price - row['Price after 5 seconds']) / row['Price after 5 seconds']) * 100
                    break
                elif high_price > price:
                    price = high_price
                    stop_loss_price = price * (1 - percentage)
                low_price = row[f'Low {i+1}'] if i < 50 else low_price
                high_price = row[f'High {i+1}'] if i < 50 else high_price
            if pct_increase is None:
                pct_increase = ((price - row['Price after 5 seconds']) / row['Price after 5 seconds']) * 100

            final_Df.loc[index, f'Pct Increases {percentage}'] = pct_increase

final_Df.to_csv('Final Analysis.csv')
