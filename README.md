# textReadability (WIP)
Software service with plug-in architecture for assessing the readability of text.

# Install
```commandline
pip install requirements.txt
python -m nltk.downloader punkt
```

## Command line usage
```commandline
python main.py --help
usage: main.py [-h] -i INPUT_FILE [-o OUTPUT_FILE] [-c]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input-file INPUT_FILE
                        specify path name for input file
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        specify path name for output file
  -c, --console         display readability results in console

```
