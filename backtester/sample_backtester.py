import matplotlib.pyplot as plt
from datetime import datetime
import pytz

from zipline.algorithm import TradingAlgorithm
from zipline.utils.factory import load_from_yahoo


class BuyApple(TradingAlgorithm):  # inherit from TradingAlgorithm
    """This is the simplest possible algorithm that does nothing but
    buy 1 apple share on each event.
    """
    def handle_data(self, data):  # overload handle_data() method
        self.order('AAPL', 1)  # order SID (=0) and amount (=1 shares)


start = datetime(2008, 1, 1, 0, 0, 0, 0, pytz.utc)
end = datetime(2010, 1, 1, 0, 0, 0, 0, pytz.utc)
data = load_from_yahoo(stocks=['AAPL'], indexes={}, start=start,
                       end=end)
simple_algo = BuyApple()
results = simple_algo.run(data)

print "RESULTS: ", results.portfolio_value

# print "VALUES: ",
# print results.values

print "COLUMNS: ", results.columns
# ax1 = plt.subplot(211)
# results.portfolio_value.plot(ax=ax1)
# ax2 = plt.subplot(212, sharex=ax1)
# data.AAPL.plot(ax=ax2)
# plt.gcf().set_size_inches(18, 8)

print "error: ", err
          print "self.url: ", self.url