def categorizar_performance(media):
    if 0 <= media <= 5:
        return 1
    elif 6 <= media <= 10:
        return 2
    elif 11 <= media <= 15:
        return 3
    else:
        return 4