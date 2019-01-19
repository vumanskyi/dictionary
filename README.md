# Simple dictionary on python

This is simple package on python for training coding on python.

## Getting Started

In current package there are available only two languages: English and German.

There are available two configuration:
 - en_to_de
 - de_to_en
 
This mean that we set word on english and get translation on german and rather.
 
### How to use

```python
from app.models.words import Words

#Set localization
word = Words('en_to_de')


word.set_word('famiar')

result = word.get_result()

print(result)

```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details