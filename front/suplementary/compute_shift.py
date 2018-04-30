

def compute_shift(col_flags, current_col):

    shift = -1
    for i, flag in enumerate(col_flags):
        if flag:
            shift += 1
        if shift == current_col:
            col_shift = i
            break
    return col_shift
