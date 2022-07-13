1. String can be encoded differently (ASCII or Unicode)
   1. ASCII
      1. 128 chars in total
      2. covers only basic european characters
      3. some are not printable
      4. a subset of unicode
   2. Unicode
      1. ~2^17 chars
      2. covers all chars in the world including Chinese
      3. use ord() to convert char to unicode index `ord('a')`
      4. use chr() to convert unicode index to char `chr(97)`
2. string can be sorted like number because they are encoded and represented by number behind the scene
3. 