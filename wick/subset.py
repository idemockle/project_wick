

def select():
    raise NotImplementedError


def filter():
    raise NotImplementedError


def distinct(df, *args, keep_all=False):
    if len(args) > 0:
        return df.drop_duplicates()
    else:
        out = df.drop_duplicates(subset=args)
        if keep_all:
            return out
        else:
            return out[args]


def sample_frac(df, size=1, replace=False, weight=None):
    raise NotImplementedError


def sample_n():
    raise NotImplementedError


def slice():
    raise NotImplementedError


def top_n():
    raise NotImplementedError