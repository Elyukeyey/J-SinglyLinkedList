def print_str(fn):
    def wrapper(*a, **kwa):
        print(str(fn(*a, **kwa)))
        return fn(*a, **kwa)
    return wrapper