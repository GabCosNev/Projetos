def replace_string_to_sequence(data, column):
    mapping = {
        'no': 1,
        'Sometimes': 2,
        'Frequently': 3,
        'Always': 4
    }
    data[column] = data[column].map(mapping)
    return data