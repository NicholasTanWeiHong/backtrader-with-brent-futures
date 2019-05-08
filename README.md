# Backtrader Framework for Quandl Futures

The following is a simple backtesting framework for Quandl Continuous Futures written with the [backtrader](https://github.com/backtrader/backtrader) library.

![App Screenshot](https://github.com/NicholasTanWeiHong/eda-quandl-futures/blob/master/images/calendar-spreads.png "App Screenshot")

## Description

The current implementation of this project is separated into two main functionalities: ` ` ` visualize_bt.py ` `  ` and `  ` ` optimize_bt.py ` ` `.

### Backtest Visualization

To run a simple analysis of a strategy, simply run:
` ` ` python visualize_bt.py ` ` `
This returns a terminal output of P & L generated over the stipulated timeframe alongside the packaged backtrader plot.

### Backtest Optimization

To optimize parameters within an existing strategy, run:
` ` ` python optimize_bt.py ` ` `
This prints a series of simulation over multiple values for the parameters and their corresponding portfolio values.

## Future Plans

* Add to set of strategies based on new ideas from fundamental research
* Tinker with 'sizers' to execute based on various risk portfolios
* Tinker with 'queries' to experiment with more unconvential commodity datasets
* Include a plotting functionality for optimizations runs

