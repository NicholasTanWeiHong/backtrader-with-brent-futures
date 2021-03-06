# Backtrader Framework for Brent Crude Oil Futures

The following is a simple backtesting framework for Brent Crude Oil Futures written with the [backtrader](https://github.com/backtrader/backtrader) library.

![App Screenshot](https://github.com/NicholasTanWeiHong/backtrader-with-brent-futures/blob/master/images/three_solders_and_crows.png "App Screenshot")

## Description

This project queries historical data for Brent Crude Oil futures from [Quandl](https://www.quandl.com/data/CHRIS-Wiki-Continuous-Futures) and backtests several algorithmic trading strategies using the backtrader library. It currently ships with three strategies: ``SmaCrossoverStrategy``, ``RSIMeanReversionSystem`` and ``ThreeSoldiersAndCrows``, which were variously inspired by examples from the [backtrader documentation series](https://www.backtrader.com/), [backtest-rookies.com](https://backtest-rookies.com/), as well as my own experiences in technical analysis.

The current implementation of this project is separated into two main functionalities: ``visualize_bt.py`` and ``optimize_bt.py``.

### Backtest Visualization

To perform a simple analysis using one of the pre-packaged strategies, simply edit in ``visualize_bt.py``:

```python
import extensions.strategies as st

cerebro.addstrategy(st.RSIMeanReversionSystem)
```

Then, in Terminal, run:

```python
python visualize_bt.py
```

This returns a terminal output of P&L generated over a stipulated timeframe alongside the packaged backtrader plot.

### Backtest Optimization

To optimize parameters within an existing strategy, first edit in ``optimize_bt.py``:

```python
cerebro.optstrategy(
        st.SmaCrossoverStrategy,
        sma1_period=range(10, 21),
        opt_mode=True
    )
```

Then run the following in Terminal:

```python
python optimize_bt.py
```

This prints a series of simulations for the parameter(s) under analysis alongside their corresponding final portfolio values.

## Future Plans (Ordered By Priority)

* Add to the set of strategies based on new ideas from fundamental research
* Include a plotting functionality for optimizations runs (i.e. Plotting Parameter Values against P&L)
* Analyze the potential of implementing the framework for live trading with OANDA or Interactive Brokers
* Tinker with 'extensions.sizers' to execute based on various risk portfolios
* Tinker with 'extensions.queries' to experiment with more unconvential commodity datasets
