# Tridex
Algorithm consisting of multiple mid and long term strategies that shortlists the best companies to invest in on FTSE 350 index, on a given day.

The jupyter notebook `tridex/strategies.ipynb` contains the mock up of trading strategies. 

The `data/stocks` directory contains data for all FTSE 350 companies starting from 2014-01-01.


### Trading Strategies
See tridex/strategies.ipynb


### To do:
- Move data to BigQuery
- Move trading strategies from notebook to .py module
- Get data going back as early as possible for all stocks instead of 2014-01-01
- Implement more strategies (use zipline?)
- Backtest all strategies
- Write tests


### Research:
- How long does it take on average for long term (~200 days) and short term (50 days) moving averages to crossover. Find the average using all stocks in FTSE 350 over the entire history. 
