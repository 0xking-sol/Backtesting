# Backtesting

Gets the OHLCV candles from Binance (Open, High, Low, Close, Volume)

Example:
binance.fetch_ohlcv(ticker, '1m', since=timestamp, limit=60)
- This will give 1 minute candles, since the timestamp (in seconds), for 60 candles (60 minutes)


candle[x][0] is timestamp
candle[x][1] is open
candle[x][2] is high
candle[x][3] is low
candle[x][4] is close
last is volume


Example output:
[[1502942400000, 301.13, 301.13, 301.13, 301.13, 0.42643], [1502942460000, 301.13, 301.13, 301.13, 301.13, 2.75787], [1502942520000, 300.0, 300.0, 300.0, 300.0, 0.0993], [1502942580000, 300.0, 300.0, 300.0, 300.0, 0.31389], [1502942640000, 301.13, 301.13, 301.13, 301.13, 0.23202], [1502942700000, 300.0, 301.13, 300.0, 301.13, 0.75705], [1502942760000, 300.1, 300.1, 300.1, 300.1, 0.90018], [1502942820000, 300.1, 300.1, 300.1, 300.1, 0.0], [1502942880000, 300.1, 300.1, 298.0, 298.0, 0.31493], [1502942940000, 298.0, 298.0, 298.0, 298.0, 0.0], [1502943000000, 298.0, 298.0, 298.0, 298.0, 0.0], [1502943060000, 298.0, 298.0, 298.0, 298.0, 0.0], [1502943120000, 298.0, 298.0, 298.0, 298.0, 0.0], [1502943180000, 298.0, 298.0, 298.0, 298.0, 0.0], [1502943240000, 298.0, 298.0, 298.0, 298.0, 0.0], [1502943300000, 298.0, 298.0, 298.0, 298.0, 9.59614], [1502943360000, 298.0, 298.0, 298.0, 298.0, 0.0], [1502943420000, 298.0, 298.0, 298.0, 298.0, 0.0], [1502943480000, 298.0, 298.0, 298.0, 298.0, 2.91114], [1502943540000, 299.05, 299.05, 299.05, 299.05, 0.37758], [1502943600000, 299.05, 299.05, 299.05, 299.05, 0.17585], [1502943660000, 299.05, 300.1, 299.05, 300.1, 6.40719], [1502943720000, 300.1, 300.1, 300.1, 300.1, 0.0], [1502943780000, 300.1, 300.1, 300.1, 300.1, 0.0], [1502943840000, 300.1, 300.1, 300.1, 300.1, 0.0], [1502943900000, 299.4, 299.4, 299.4, 299.4, 0.54316], [1502943960000, 299.4, 300.8, 299.4, 300.8, 4.77061], [1502944020000, 299.39, 299.39, 299.39, 299.39, 0.08994], [1502944080000, 299.39, 299.39, 299.39, 299.39, 0.05886], [1502944140000, 299.39, 299.39, 299.39, 299.39, 6.51018], [1502944200000, 299.39, 299.39, 299.39, 299.39, 0.486], [1502944260000, 299.39, 299.39, 299.39, 299.39, 0.0], [1502944320000, 299.39, 299.39, 299.39, 299.39, 17.93696], [1502944380000, 299.39, 299.39, 299.39, 299.39, 1.95841], [1502944440000, 299.39, 299.39, 299.39, 299.39, 0.4096], [1502944500000, 299.39, 299.39, 299.39, 299.39, 24.5542], [1502944560000, 300.79, 300.79, 300.79, 300.79, 0.86993], [1502944620000, 299.6, 299.6, 299.6, 299.6, 0.90661], [1502944680000, 299.6, 299.6, 299.6, 299.6, 0.0], [1502944740000, 299.6, 299.6, 299.6, 299.6, 1.26188], [1502944800000, 299.6, 299.6, 299.6, 299.6, 0.70683], [1502944860000, 299.6, 299.6, 299.6, 299.6, 2.53734], [1502944920000, 299.6, 299.6, 299.6, 299.6, 0.55225], [1502944980000, 299.6, 299.6, 299.6, 299.6, 0.0], [1502945040000, 299.6, 299.6, 299.6, 299.6, 0.75578], [1502945100000, 299.6, 299.6, 299.6, 299.6, 0.75878], [1502945160000, 300.8, 300.8, 300.8, 300.8, 0.23323], [1502945220000, 300.79, 300.79, 300.79, 300.79, 2.27645], [1502945280000, 300.79, 300.79, 300.79, 300.79, 0.82377], [1502945340000, 300.79, 300.79, 300.79, 300.79, 1.14426], [1502945400000, 300.79, 300.8, 300.79, 300.8, 1.45349], [1502945460000, 300.8, 300.8, 300.8, 300.8, 0.0], [1502945520000, 300.8, 301.13, 300.8, 300.8, 6.78247], [1502945580000, 301.13, 301.13, 301.13, 301.13, 0.39447], [1502945640000, 301.13, 301.13, 301.13, 301.13, 7.31345], [1502945700000, 301.13, 301.51, 301.13, 301.51, 3.04318], [1502945760000, 302.57, 302.57, 302.57, 302.57, 3.5576], [1502945820000, 302.57, 302.57, 302.57, 302.57, 0.0], [1502945880000, 301.61, 301.61, 301.61, 301.61, 7.70951], [1502945940000, 301.61, 301.61, 301.61, 301.61, 0.0]]
