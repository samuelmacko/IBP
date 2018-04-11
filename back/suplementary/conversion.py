

def to_MB(value):
    value = str(value)
    # if ' ' in value:
    split_value = value.split(' ')
    #todo zle
    if len(split_value) > 1 and \
            (split_value[1] != 'B' or split_value[1] != 'B/s'):
        return value

    return str(int(split_value[0]) / (1024 * 1024)) + ' MB'
    # else:
    #     return str(int(value) / (1024 * 1024)) + ' MB'
