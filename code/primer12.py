#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    with open("text.txt", "w", encoding="utf-8") as fileptr:
        print(
              "UTF-8 is variable-width character encodind used for electronic communicatication.",
              file=fileptr
              )
        print(
            "UTF-8 is capable of encoding all 1,112,064 valid character code points.",
            file=fileptr
        )
        print(
            "In Unicode using one to four one-byte (8-bit) code units.",
            file=fileptr
        )