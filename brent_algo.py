import backtrader as bt
import extensions.strategies as st
import extensions.sizers as sz

import datetime as dt
import quandl

my_quandl_key = open("quandlapikey.txt", "r").read()
quandl.ApiConfig.api_key = my_quandl_key


def import_quandl_futures(quandl_code):

    # Query continuous futures data from the Quandl API
    df = quandl.get(quandl_code)

    # Preprocess the pandas DataFrame to accommodate backtrader PandasData feed
    df.rename(columns={
        'Settle': 'Close',
        'Prev. Day Open Interest': 'OpenInterest'},
        inplace=True)
    df = df[['Open', 'High', 'Low', 'Close', 'Volume', 'OpenInterest']]

    return df


if __name__ == '__main__':

    # Instantiate a Cerebro class
    cerebro = bt.Cerebro()

    # Add a strategy to Cerebro
    cerebro.addstrategy(st.RSIMeanReversionSystem)

    # Query historical Brent Crude Oil data from Quandl for backtesting
    brent = import_quandl_futures('CHRIS/ICE_B1')
    data = bt.feeds.PandasData(
        dataname=brent,
        fromdate=dt.datetime(2018, 1, 1),
        todate=dt.datetime.now())

    # Add the data feed to Cerebro
    cerebro.adddata(data)

    # Set starting cash as $100,000
    starting_cash = 100_000
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
    cerebro.plot()
