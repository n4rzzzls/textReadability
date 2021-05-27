
def display_dict(dictionary: dict) -> None:
    """
    Prints a dictionary line by line
    :param dictionary: dictionary to be displayed
    :return: None
    """
    if isinstance(dictionary, type(dictionary)):
        for k, v in dictionary.items():
            if k == 'Words frequency':
                print("10 most used words:")
                for x in v:
                    print(f"\t\"{x[0]} : {x[1]}")
            elif hasattr(v, '__iter__'):
                print("-" * 20, '\n', k, "\n", "-" * 20)
                display_dict(v)
            else:
                print('%s : %s' % (k, v))
