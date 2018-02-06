import pandas as pd


def spread(tidydf, key, value, fill=None, sep=None):
    index_cols = [col for col in tidydf._df.columns if col not in [key, value]]
    index_cols = index_cols + [key]
    tidydf._df.set_index(index_cols, inplace=True)
    tidydf._df = tidydf._df.unstack(fill_value=fill)
    tidydf._df.columns = tidydf._df.columns.droplevel().rename(None)
    if sep is not None:
        tidydf._df.rename(columns={col: sep.join((key, col)) for col in tidydf._df.columns}, inplace=True)
    tidydf._df.reset_index(inplace=True)
    return tidydf


def gather(tidydf, key, value, *args, na_rm=False):
    print('Not Implemented')