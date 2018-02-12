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
    idxset = set()
    for idxstr in args:
        idxlist = tidydf._parse_select(idxstr)
        idxset |= set(idxlist)
    idxcols = tidydf._invert_idx(list(idxset))
    idxcols = list(tidydf._df.columns.values[idxcols])
    tidydf._df.set_index(idxcols, inplace=True)
    tidydf._df.columns.rename(key, inplace=True)
    tidydf._df = tidydf._df.stack()
    tidydf._df.name = value
    if na_rm:
        tidydf._df.dropna(inplace=True)
    tidydf._df = tidydf._df.reset_index()
    return tidydf

