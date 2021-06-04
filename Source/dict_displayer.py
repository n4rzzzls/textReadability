
def display_dict(dictionary: dict) -> None:
    """
    Prints a dictionary line by line in console
    :param dictionary: dictionary to be displayed
    :return: None
    """

    if isinstance(dictionary, dict):

        for text_info_component_key, text_info_component_value in dictionary.items():

            if text_info_component_key == 'READABILITY GRADES':

                print("-" * 20, '\n', text_info_component_key, "\n", "-" * 20)

                for word in text_info_component_value.items():

                    readability_grade_name, readability_grade_values = word
                    readability_score, readability_level = readability_grade_values
                    print(f"{readability_grade_name}: {readability_score} ---> {readability_level}")

                continue

            if text_info_component_key == 'Words frequency':
                print("10 most used words:")

                for word in text_info_component_value:
                    print(f"\t\"{word[0]} : {word[1]}")

            elif hasattr(text_info_component_value, '__iter__') and not text_info_component_key == 'READABILITY GRADES':

                print("-" * 20, '\n', text_info_component_key, "\n", "-" * 20)
                display_dict(text_info_component_value)

            else:
                print('%s : %s' % (text_info_component_key, text_info_component_value))
