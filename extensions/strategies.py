import backtrader as bt


class SmaCrossoverStrategy(bt.SignalStrategy):
    """
    Simple Moving Average Crossover Strategy.

    Description
    -----------
    This strategy generates a signal when the short SMA crosses the long SMA.
    A Buy trade is made when the short SMA crosses above the long SMA,
    and a Sell trade is made when the short SMA crosses below the long SMA.
    """

    params = (
        ('sma1_period', 10),
        ('sma2_period', 30),
        ('opt_mode', False)
    )

    def __init__(self):
        sma1 = bt.ind.SMA(period=self.params.sma1_period)
        sma2 = bt.ind.SMA(period=self.params.sma2_period)
        crossover_signal = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(sigtype=bt.signal.SIGNAL_LONG, signal=crossover_signal)

    def stop(self):
        if self.params.opt_mode is True:
            param_1 = self.params.sma1_period
            param_2 = self.params.sma2_period
            port_value = round(self.broker.getvalue(), 2)
            print(
                'MA1 Period: %d, MA2 Period: %d, Final Portfolio Value: $%.2f'
                % (param_1, param_2, port_value))


class RSIMeanReversionSystem(bt.Strategy):
    """
    RSI Mean Reversion Strategy.

    Description
    -----------
    This strategy generates an 'RSI Index' based on the Close of the asset.
    When the RSI Index enters 'oversold' territory (i.e. < 30),
    a Buy trade is initiated.
    Conversely, when the RSI Index enters 'overbought' territory (i.e. > 70),
    a Sell trade is initiated.
    """

    params = (
        ('rsi_period', 14),
        ('opt_mode', False)
    )

    def __init__(self):
        self.rsi = bt.ind.RSI_SMA(
            self.data.close, period=self.params.rsi_period
        )

    def next(self):
        if not self.position:
            if self.rsi < 30:
                self.buy()
        else:
            if self.rsi > 70:
                self.sell()

    def stop(self):
        if self.params.opt_mode is True:
            param = self.params.rsi_period
            port_value = round(self.broker.getvalue(), 2)
            print('RSI Period: %d, Final Portfolio Value: $%.2f'
                  % (param, port_value))


class ThreeSoldiersAndCrows(bt.Strategy):
    """
    Three Solders and Crows Strategy.

    Description
    -----------
    This strategy analyzes the number of consecutively bullish/bearish candles.
    If it encounters three consecutively bearish candles,
    a Buy trade is initiated.
    If it encounters three consecutively bullish candles,
    a Sell trade is initiated.
    """

    def __init__(self):
        self.dataclose = self.data.close

    def next(self):
        if not self.position:
            if self.dataclose[0] < self.dataclose[-1]:
                if self.dataclose[-1] < self.dataclose[-2]:
                    if self.dataclose[-2] < self.dataclose[-3]:
                        self.buy()
        else:
            if self.dataclose[0] > self.dataclose[-1]:
                if self.dataclose[-1] > self.dataclose[-2]:
                    if self.dataclose[-2] > self.dataclose[-3]:
                        self.sell()
