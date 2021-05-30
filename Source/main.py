import cProfile

from text_parser import text_parsing
from text_stats import get_text_measures
from file_nandler import file_reader, file_writer
from args_parser import args_parsing
from dict_displayer import display_dict


def main():

    results = ''
    args = args_parsing()

    if args.input_file:
        input_file_name = args.input_file
        raw_text = file_reader(input_file_name)
        parsed_text = text_parsing(raw_text)
        results = get_text_measures(parsed_text)

    if args.output_file:
        output_file = args.output_file
        file_writer(output_file, results)

    if args.console:
        display_dict(results)


if __name__ == '__main__':
    # pr = cProfile.Profile()
    # pr.enable()
    main()
    # pr.disable()
    # # after your program ends
    # pr.print_stats(sort="calls")
