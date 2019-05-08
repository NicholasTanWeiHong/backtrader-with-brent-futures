import backtrader as bt


class ModifiyingSizer(bt.Sizer):
    params = (
        ('size', 1),
    )

    def _getsizing(self, comminfo, cash, data, isbuy):
        return self.p.size
