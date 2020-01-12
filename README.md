# Python Bitvavo Triangular Arbitrage Opportunity Monitor

A Simple Cryptocurrency Triangular Arbitrage Opportunities python application computes potential triangular arbitrage profits on Bitvavo exchange in real-time using REST and Websockets. It monitors 57 pairs (total of 114 opportunities) in real-time. Base currency is EUR. This is NOT an auto-trader.

Here are some examples of the strategy which the bot uses:
```
Buy BTC at X -> Buy ETH at X -> Sell ETH for X€ = profit
Buy ETH at X€ -> Sell ETH at X -> Sell BTC for X€ = profit
...
...
```

This project is using the python wrapper for the Bitvavo API.

Feel free to develop this project further for example making the bot excecute the strategy automatically by placing the orders for you. For more infos visit the official docs of Bitvavo [Bitvavo API documentation](https://docs.bitvavo.com/)

## Installation
```
pip install python-bitvavo-api
```

### Getting started

The API key and secret are required. Replace it in the file. [HERE](https://github.com/sinahastam/Python-Bitvavo-Triangular-Arbitrage-Opportunity-Monitor/blob/master/python_bitvavo_api/testApi.py#L368)
```python
from python_bitvavo_api.bitvavo import Bitvavo
bitvavo = Bitvavo({ 
  'APIKEY': "REPLACE_WITH_YOUR_APIKEY",
  'APISECRET': "REPLACE_WITH_YOUR_APISECRET",
  'ACCESSWINDOW': 10000,
  'DEBUGGING': True
})
```

## Additional Information
Minimum profit should be changed in the file. NOTE: Fees are not included in min_profit -> so real profit = min_profit - taker_fee\*3
Taker fee is 0.25% per trade on first tier. 
```
min_profit = 0.10
```

## Contact
If you feel you want to get in touch, then you can email me at j.doha999@gmail.com
