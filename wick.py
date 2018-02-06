import pandas as pd
import numpy as np

import tidyr


class TidyDF:
    def __init__(self, df, inplace):
        if inplace:
            self._df = df
        else:
            self._df = df.copy()

    def spread(self, key, value, fill=None, sep=None):
        return tidyr.spread(self, key, value, fill, sep)

    def gather(self):
        print('Not Implemented')

    def untidy(self):
        return self._df

    def __str__(self):
        n_head_rows = 5
        repstr = 'TidyDF\n------\n'+str(self._df.head(n_head_rows))
        if len(self._df) > n_head_rows:
            repstr += '\n + %i more rows'%(len(self._df)-n_head_rows)
        return repstr

    def __repr__(self):
        return self.__str__()
    

def tidy(df, inplace=False):
    return TidyDF(df, inplace=inplace)
