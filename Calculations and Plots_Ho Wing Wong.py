#==============================================================================
# Lists of stock index values
#
# By Johnny Lin
#
# There are three lists defined here:
# * nasdaq:  Close of index at the end of each trading day in trading_days.
# * sp500:  Close of index at the end of each trading day in trading_days.
# * djia:  Close of index at the end of each trading day in trading_days.
# * trading_days:  Number of trading days since Jun 1, 2016.  Jun 1 is
#   trading day 0.
#
# Values downloaded from http://finance.yahoo.com.  Values of all lists are
# daily trading day closings from Jun 1-Aug 31, 2016, inclusive.
#==============================================================================


nasdaq = [4952.25,
4971.359863,
4942.52002,
4968.709961,
4961.75,
4974.640137,
4958.620117,
4894.549805,
4848.439941,
4843.549805,
4834.930176,
4844.919922,
4800.339844,
4837.209961,
4843.759766,
4833.319824,
4910.040039,
4707.97998,
4594.439941,
4691.870117,
4779.25,
4842.669922,
4862.569824,
4822.899902,
4859.160156,
4876.810059,
4956.759766,
4988.640137,
5022.819824,
5005.72998,
5034.060059,
5029.589844,
5055.779785,
5036.370117,
5089.930176,
5073.899902,
5100.160156,
5097.629883,
5110.049805,
5139.810059,
5154.97998,
5162.129883,
5184.200195,
5137.72998,
5159.740234,
5166.25,
5221.120117,
5213.140137,
5225.47998,
5204.580078,
5228.399902,
5232.890137,
5262.02002,
5227.109863,
5228.660156,
5240.149902,
5238.379883,
5244.600098,
5260.080078,
5217.689941,
5212.200195,
5218.919922,
5232.330078,
5222.990234,
5213.220215]

sp500 = [2099.330078,
2105.26001,
2099.129883,
2109.409912,
2112.129883,
2119.120117,
2115.47998,
2096.070068,
2079.060059,
2075.320068,
2071.5,
2077.98999,
2071.219971,
2083.25,
2088.899902,
2085.449951,
2113.320068,
2037.410034,
2000.540039,
2036.089966,
2070.77002,
2098.860107,
2102.949951,
2088.550049,
2099.72998,
2097.899902,
2129.899902,
2137.159912,
2152.139893,
2152.429932,
2163.75,
2161.73999,
2166.889893,
2163.780029,
2173.02002,
2165.169922,
2175.030029,
2168.47998,
2169.179932,
2166.580078,
2170.060059,
2173.600098,
2170.840088,
2157.030029,
2163.790039,
2164.25,
2182.870117,
2180.889893,
2181.73999,
2175.48999,
2185.790039,
2184.050049,
2190.149902,
2178.149902,
2182.219971,
2187.02002,
2183.870117,
2182.639893,
2186.899902,
2175.439941,
2172.469971,
2169.040039,
2180.379883,
2176.120117,
2170.949951]

djia = [17789.669922,
17838.560547,
17807.060547,
17920.330078,
17938.279297,
18005.050781,
17985.189453,
17865.339844,
17732.480469,
17674.820312,
17640.169922,
17733.099609,
17675.160156,
17804.869141,
17829.730469,
17780.830078,
18011.070312,
17400.75,
17140.240234,
17409.720703,
17694.679688,
17929.990234,
17949.369141,
17840.619141,
17918.619141,
17895.880859,
18146.740234,
18226.929688,
18347.669922,
18372.119141,
18506.410156,
18516.550781,
18533.050781,
18559.009766,
18595.029297,
18517.230469,
18570.849609,
18493.060547,
18473.75,
18472.169922,
18456.349609,
18432.240234,
18404.509766,
18313.769531,
18355,
18352.050781,
18543.529297,
18529.289062,
18533.050781,
18495.660156,
18613.519531,
18576.470703,
18636.050781,
18552.019531,
18573.939453,
18597.699219,
18552.570312,
18529.419922,
18547.300781,
18481.480469,
18448.410156,
18395.400391,
18502.990234,
18454.300781,
18400.880859]

trading_days = range(len(nasdaq))

#- Check lengths of all lists are the same: if (len(nasdaq) != len(sp500)) or (len(sp500) != len(djia)):
#    raise ValueError, "bad data"

import scipy as sci
import matplotlib.pyplot as plt

#1
naMean = sci.mean(nasdaq)
naStd = sci.std(nasdaq)

spMean = sci.mean(sp500)
spStd = sci.std(sp500)

djMean = sci.mean(djia)
djStd = sci.std(djia)

print('Nasdaq mean= ', naMean)
print('Nasdaq s.d.= ', naStd)
print('Nasdaq s.d./mean=', naStd/naMean)
print('Sp500 mean= ', spMean)
print('spStd= ', spStd)
print('sp500 s.d./mean=', spStd/spMean)
print('djia mean= ', djMean)
print('djia Std= ', djStd)
print('djia s.d./mean=', djStd/djMean)

#2
plt.figure(1)
plt.plot(trading_days, nasdaq, 'r*--')
plt.ylabel('Index')
plt.xlabel('Time')
plt.title('NASDAQ', size = 24.0)
plt.show()

plt.figure(2)
plt.plot(trading_days, sp500, 'b*--')
plt.ylabel('Index')
plt.xlabel('Time')
plt.title('S&P 500 Index', size = 24.0)
plt.show()

plt.figure(3)
plt.plot(trading_days, djia,  'k*--')
plt.ylabel('Index')
plt.xlabel('Time')
plt.title('Dow Jones Industrial Index', size = 24.0)
plt.show()

#3
plt.figure(4)
#plt.plot(trading_days, nasdaq, 'r*-.',label="NASDAQ", trading_days, sp500, 'b*--',label= "S&P 500", trading_days, djia, 'k*-',label= "Dow Jones")
plt.plot(trading_days, nasdaq, 'r*--',label="NASDAQ")
plt.plot(trading_days, sp500, 'b*--',label= "S&P 500")
plt.plot(trading_days, djia,  'k*--',label= "Dow Jones")
plt.axis([0,100, 0, 20000])
plt.ylabel('Index')
plt.xlabel('Time')
plt.title('DJIA, SP500, NASDAQ Combined', size = 20.0)
plt.legend()
plt.show()
#===== end file =====
