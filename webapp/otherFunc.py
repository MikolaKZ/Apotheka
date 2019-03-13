def str_to_bool(s):
    s = s.lower()
    if s == 'true':
        return True
    elif s == 'false':
        return False
    else:
        raise ValueError
