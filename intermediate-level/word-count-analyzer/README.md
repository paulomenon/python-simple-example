# Word Count Analyzer

Analyzes a block of text and reports statistics: character count, word count, sentence count, unique words, average word length, and the top 5 most common words.

## How to Run

```bash
python word_count_analyzer.py
```

Enter your text, then press Enter on an empty line to finish.

## Example

```
Word Count Analyzer
------------------------------
Enter your text (press Enter twice to finish):

The quick brown fox jumps over the lazy dog. The dog barked at the fox.

===== Text Analysis =====
Characters (with spaces):    71
Characters (without spaces): 58
Words:                       14
Sentences:                   2
Unique words:                10
Average word length:         3.4 characters

Top 5 most common words:
  'the' — 3 time(s)
  'dog' — 2 time(s)
  'fox' — 2 time(s)
  'quick' — 1 time(s)
  'brown' — 1 time(s)
```

## What You'll Learn

- String methods (`split()`, `lower()`, `strip()`, `count()`)
- Dictionaries for counting word frequency
- Sorting with `sorted()` and lambda functions
- Functions that return dictionaries
