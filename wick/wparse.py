def colselect(df, colstr):
    deselect = colstr.startswith('-')
    if deselect:
        colstr = colstr[1:]

    is_slice = ':' in colstr
    if is_slice:
        start_col, end_col = [s.replace(' ', '') for s in colstr.split(':')]
        start_idx = df.columns.get_loc(start_col)
        end_idx = df.columns.get_loc(end_col) + 1
        out_idx = list(range(start_idx, end_idx))
    else:
        out_idx = [df.columns.get_loc(colstr)]

    if deselect:
        return invert_idx(out_idx)
    else:
        return out_idx


def contains(df, *match, ignore_case=True):
    return NotImplementedError


def ends_with(df, match, ignore_case=True):
    return NotImplementedError


def everything():
    return slice(None)


def matches(df, match, ignore_case=True):
    return NotImplementedError


def num_range(df, prefix, range, width = None):
    return NotImplementedError


def one_of(df, *args):
    return NotImplementedError


def starts_with(df, match, ignore_case=True):
    return NotImplementedError












def invert_idx(df, idx):
    if type(idx) == int:
        idx = {idx}
    else:
        idx = set(idx)
    return list(set(range(df.shape[1])) - idx)