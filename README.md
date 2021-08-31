# Morse Code Translator (Project #1 - Moorse)

This Morse Code translator is made with Python. It can translate from text to Morse or from Morse to text.

## Inspiration

A friend told me to practice my use of dictionaries and cleaning data so I decided to make a simple translator to utilize these concepts in real-world software.

## Usage

```python
import Moorse

# returns 'text'
print(Moorse.translate('Morse Code'))

# returns 'morse code'
print(Moorse.translate('text'))
```

## Keep in Mind
The `_` and `▬` simple is used for dashes and the `.` and `•` is used for dots.

Accented letters are not supported ex. `À`, `È`, `Ö`.
