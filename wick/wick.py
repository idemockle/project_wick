import pandas as pd

from wick import tidyr


class TidyDF:
    def __init__(self, df, inplace):
        if inplace:
            self._df = df
        else:
            self._df = df.copy()

    def spread(self, key, value, fill=None, sep=None):
        return tidyr.spread(self, key, value, fill, sep)

    def gather(self, key, value, *args, na_rm=False):
        return tidyr.gather(self, key, value, *args, na_rm=na_rm)

    def untidy(self):
        return self._df

    def _parse_idx_str(self, colstr):
        deselect = colstr.startswith('-')
        if deselect:
            colstr = colstr[1:]

        is_slice = ':' in colstr
        if is_slice:
            start_col, end_col = colstr.split(':')
            start_idx = self._df.columns.get_loc(start_col)
            end_idx = self._df.columns.get_loc(end_col) + 1
            out_idx = list(range(start_idx, end_idx))
        else:
            out_idx = [self._df.columns.get_loc(colstr)]

        if deselect:
            return self._invert_idx(out_idx)
        else:
            return out_idx

    def _invert_idx(self, idx):
        if type(idx) == int:
            idx = {idx}
        else:
            idx = set(idx)
        return list(set(range(self._df.shape[1])) - idx)

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
