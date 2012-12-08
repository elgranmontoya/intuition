#!/usr/bin/python
# -*- coding: utf8 -*-

# Logger class (obviously...)
from Utilities import LogSubSystem
from Utilities import DatabaseSubSystem

# For mathematical stuff, data manipulation...
from pandas import Index, DataFrame
# Statsmodels has ols too, benchamark needed
from pandas import ols


'''---------------------------------------------------------------------------------------
Quant
---------------------------------------------------------------------------------------'''
class Quantitative:
  ''' Trade qunatitativ module 
  an instanciation work on a data set specified while initializing'''
  def __init__(self, quotes, logger=None):
    if logger == None:
      self._logger = LogSubSystem('Computer', "debug").getLog()
    else:
      self._logger = logger
    self._quotes = data
    #TODO: initialize database 

  def variation(self, period=0, start_date=0):
    ''' Day variation if nothing specified
    from startDate and for period otherwize '''
    if period + start_date == 0:  # Wants day variation
      self._logger.debug("Day variation")
      return ((self._data[self._data.shape[0]-1, 4] - self._data[0, 4]) / self._data[0, 4]) * 100
    elif period > 0 and start_date > 0:  # Variation between two dates
      self._logger.debug("Variation between two dates")
      return 1
    elif period > 0 and start_date == 0:  # Want variation from now to start_date
      self._logger.debug("Variation from now to date")
      return 2

    def returns(self, ts, period):
        ''' Compute returns on the given period '''
        #TODO: freq parameter etc...
        return ts / ts.shift(period) -1

    def HighLowSpread(self, df, offset):
        ''' Compute continue spread on given datafrme every offset period '''
        #TODO: handling the offset period with reindexing or resampling, sthg like:
        # subIndex = df.index[conditions]
        # df = df.reindex(subIndex)
        return df['high'] - df['close']

    def toMonthly(frame, how):
        #TODO: generic function ?
        offset = BMonthEnd()
        return frame.groupby(offset.rollforward).aggregate(how)

  #TODO: updateDB, every class has this method, factorisation ? shared memory map to synchronize

'''---------------------------------------------------------------------------------------
Usage Exemple
---------------------------------------------------------------------------------------'''
'''
if __name__ == '__main__':
'''

