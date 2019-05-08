import backtrader as bt
import extensions.strategies as st
import extensions.sizers as sz
import extensions.queries as qs
import datetime as dt


if __name__ == '__main__':
    # Instantiate a Cerebro class
    cerebro = bt.Cerebro()

    # Add a strategy to Cerebro from the strategies module
    cerebro.addstrategy(st.RSIMeanReversionSystem)

    # Query historical Brent Crude Oil data from Quandl for backtesting
    brent = qs.import_quandl_futures('CHRIS/ICE_B1')

    # Specify the backtest timeframe from '01/01/2018' to '01/01/2019'
    data = bt.feeds.PandasData(
        dataname=brent,
        fromdate=dt.datetime(2016, 1, 1),
        todate=dt.datetime(2019, 1, 1)
    )

    # Add the data feed to Cerebro
    cerebro.adddata(data)

    # Set starting cash as $10,000
    starting_cash = 10_000
    cerebro.broker.setcash(starting_cash)
    print(f'Starting Portfolio Value: ${round(cerebro.broker.getvalue(), 2)}')

    # Set broker commission to 0.1%
    cerebro.broker.setcommission(commission=0.001)

    # Add a custom Sizer class to Cerebro
    cerebro.addsizer(sz.ModifiyingSizer, size=100)

    # Run the backtest
    cerebro.run()

    # Print the results of the backtest
    print(f'Ending Portfolio Value: ${round(cerebro.broker.getvalue(), 2)}')
    print(f'Total P&L: ${round(cerebro.broker.getvalue() - starting_cash, 2)}')

    # Plot the results of the backtest
    cerebro.plot(style='candlestick')
