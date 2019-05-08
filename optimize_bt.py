import backtrader as bt
import extensions.strategies as st
import extensions.sizers as sz
import extensions.queries as qs
import datetime as dt


if __name__ == '__main__':

    # Instantiate a Cerebro class
    cerebro = bt.Cerebro(optreturn=False)

    # Add a strategy and its corresponding parameter(s) to optimize
    cerebro.optstrategy(
        st.SmaCrossoverStrategy,
        sma1_period=range(10, 21),
        opt_mode=True
    )

    # Query historical Brent Crude Oil data from Quandl for backtesting
    brent = qs.import_quandl_futures('CHRIS/ICE_B1')

    # Specify the backtest timeframe from '01/01/2018' to '01/01/2019'
    data = bt.feeds.PandasData(
        dataname=brent,
        fromdate=dt.datetime(2014, 1, 1),
        todate=dt.datetime(2019, 1, 1)
    )

    # Add the data feed to Cerebro
    cerebro.adddata(data)

    # Set starting cash as $10,000
    starting_cash = 10_000
    cerebro.broker.setcash(starting_cash)

    # Set broker commission to 0.1%
    cerebro.broker.setcommission(commission=0.001)

    # Add a custom Sizer class to Cerebro
    cerebro.addsizer(sz.ModifiyingSizer, size=100)

    # Iterate through all backtests and print the results
    print('')
    print('Backtest Optimization Results')
    print('-' * 50)
    opt_runs = cerebro.run()
