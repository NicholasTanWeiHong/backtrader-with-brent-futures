import backtrader as bt


class SmaCrossoverStrategy(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=30)
        crossover_signal = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(sigtype=bt.signal.SIGNAL_LONG, signal=crossover_signal)


class RSIMeanReversionSystem(bt.Strategy):
    def __init__(self):
        self.rsi = bt.ind.RSI_SMA(self.data.close, period=14)

    def next(self):
        if not self.position:
            if self.rsi < 30:
                self.buy()
        else:
            if self.rsi > 70:
                self.sell()
