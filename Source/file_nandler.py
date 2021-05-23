import textract
import PyPDF2


def read_pdf(file_name):
    """
    Reader for .pdf files
    :param file_name: file name
    :return: text from a file
    """
    pdf_reader = PyPDF2.PdfFileReader(file_name)
    page_obj = pdf_reader.getPage(0)
    raw_text = page_obj.extractText()
    return raw_text


def read_default(file_name):
    """
    Default file reader
    :param file_name: file name
    :return: text from a file
    """
    raw_text = textract.process(file_name).decode('utf-8')
    return raw_text


READER_FUNCTIONS = {
    'pdf': read_pdf
}


# Reads .txt/.odt/.pdf/.docx and transforms it into raw text.
# Returns raw text in string type.
def file_reader(file_name: str = '') -> str:
    """
    Reads a file
    :param file_name: file name
    :return: text from file
    """
    name, extension = file_name.rsplit('.', 1)
    reader_function = READER_FUNCTIONS.get(extension, read_default)
    return reader_function(file_name)


# Writes results into the specified file
def file_writer(file_name, readability_results):
    """
    Writes the results into the file
    :param file_name: file name
    :param readability_results: text readability calculation results
    :return: None
    """
    with open(file_name, 'w') as reader:
        reader.write(readability_results)
        reader.flush()
