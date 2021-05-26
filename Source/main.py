from text_parser import text_parser
from text_stats import get_text_measures
from file_nandler import file_reader, file_writer
import argparse


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
                    print('\t\"%s\" : %s' % (x[0], x[1]))
            elif hasattr(v, '__iter__'):
                print("-" * 20, '\n', k, "\n", "-" * 20)
                display_dict(v)
            else:
                print('%s : %s' % (k, v))


def main():

    results = ''

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("-i", "--input-file", required=True, type=str, help='specify path name for input file')
    args_parser.add_argument("-o", "--output-file", required=False, type=str, help='specify path name for output file')
    args_parser.add_argument("-c", "--console", required=False, action='store_true', help='display readability '
                                                                                          'results in console')
    args = args_parser.parse_args()

    if args.input_file:
        input_file_name = args.input_file
        raw_text = file_reader(input_file_name)
        parsed_text = text_parser(raw_text)
        results = get_text_measures(parsed_text)

    if args.output_file:
        output_file = args.output_file
        file_writer(output_file, results)

    if args.console:
        display_dict(results)


if __name__ == '__main__':
    main()
