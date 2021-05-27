import argparse


def args_parsing():
    """

    :return:
    """
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("-i", "--input-file", required=True, type=str, help='specify path name for input file')
    args_parser.add_argument("-o", "--output-file", required=False, type=str, help='specify path name for output file')
    args_parser.add_argument("-c", "--console", required=False, action='store_true', help='display readability '
                                                                                          'results in console')
    args = args_parser.parse_args()

    return args
