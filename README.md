# BookBot

BookBot is a Python command-line application that analyzes text files and provides statistics about word count and character frequency.

## Features

- Counts total number of words in a text file
- Counts frequency of each alphabetical character (case-insensitive)
- Displays results in a formatted report
- Sorts character frequencies from most frequent to least frequent

## Requirements

- Python 3.x

## Installation

1. Clone this repository or download the source code
```bash
git clone <repository-url>
cd bookbot
```

## Usage

Run the program from the command line by providing the path to your text file:

```bash
python3 main.py <path_to_book>
```

Example:
```bash
python3 main.py books/frankenstein.txt
```

### Sample Output
```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
...
============= END ===============
```

## Project Structure

- `main.py`: Entry point of the application
- `stats.py`: Contains core functionality for text analysis
- `books/`: Directory containing text files to analyze

## Error Handling

The program includes error handling for:
- Missing command line arguments
- File not found
- File reading errors

If you run the program without specifying a file path, you'll see:
```bash
Usage: python3 main.py <path_to_book>
```

## Contributing

Feel free to submit issues and enhancement requests!

## License
lol
