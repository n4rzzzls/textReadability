from text_parser import text_parser
from text_stats import get_measures
from file_nandler import file_reader, file_writer
import argparse


# Prints a dictionary line by line
def display_dict(dictionary):
    """
    Prints a dictionary line by line
    :param dictionary:
    :param parsed:
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

    argsParser = argparse.ArgumentParser()
    argsParser.add_argument("--i", required=True, type=str)
    argsParser.add_argument("--o", required=False, type=str)
    argsParser.add_argument("--c", required=False, action='store_true')
    args = argsParser.parse_args()

    if args.i:
        input_file_name = args.i
        raw_text = file_reader(input_file_name)
        parsed_text = text_parser(raw_text)
        results = get_measures(parsed_text)

    if args.c:
        print(results)
        display_dict(results)

    if args.o:
        outputFile = args.o
        file_writer(outputFile, results)


if __name__ == '__main__':
    main()
