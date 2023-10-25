#!/usr/bin/python3
"""
a method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you
    only need to handle the 8 least significant bits of each integer

    """
    # bytes in the current utf-8 charcter.
    utf_8_1 = 0
    # check for most significant bit
    check_bit_1 = 1 << 7
    check_bit_2 = 1 << 6

    # looping through each byte in the data.
    for bytes in data:
        check = 1 << 7
        if utf_8_1 == 0:
            while check & bytes:
                utf_8_1 += 1
                check = check >> 1

                # for byte characters.
                if utf_8_1 == 0:
                    continue

                if utf_8_1 == 1 or utf_8_1 > 4:
                    return False

        else:
            if not (bytes & check_bit_1 and not (bytes & check_bit_2)):
                return False
        utf_8_1 -= 1
        return utf_8_1 == 0
