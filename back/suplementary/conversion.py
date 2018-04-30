

def to_MB(value):
    value = str(value)
    split_value = value.split(' ')
    if len(split_value) > 1 and \
            (split_value[1] != 'B' or split_value[1] != 'B/s'):
        return value

    return str(int(split_value[0]) / (1024 * 1024)) + ' MB'
