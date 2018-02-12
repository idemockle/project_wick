import pandas as pd

from wick import reshape
from wick import wparse


class TidyDF:
    def __init__(self, df, inplace):
        if inplace:
            self._df = df
        else:
            self._df = df.copy()

    def spread(self, key, value, fill=None, sep=None):
        return reshape.spread(self, key, value, fill, sep)

    def gather(self, key, value, *args, na_rm=False):
        return reshape.gather(self, key, value, *args, na_rm=na_rm)

    def untidy(self):
        return self._df

    def _parse_select(self, colstr):
        return wparse.colselect(self._df, colstr)

    def _invert_idx(self, idx):
        return wparse.invert_idx(self._df, idx)

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


if __name__ == '__main__':
    a = pd.DataFrame(dict(a=[1, 1, 2, 2, 3, 3], b=['a', 'b'] * 3, c=pd.np.random.rand(6)))
    a = tidy(a).spread('b', 'c', sep='_').gather('b', 'c', '-a')
