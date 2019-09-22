"""
Implement a bit map for storing given number of bits

Approach:
    We'll keep number of character array (8 bits each) for storing bits
    For Setting a bit:
        We'll find out how many elements to skip and which bit to set
        After we find the element, we can generate a mask and perform an OR operation with current element

        For setting a bit 22
        We need to skip 22/8 , i.e 2 elements and set 22%8 i.e 6th bit of 3rd element

        In order to generate a mask with 6th bit set, 0000 0100 We'll left shift 1 2 times (8-6 times)
        After we have a mask we'll just perform a bitwise OR with element 3

    For Getting a bit:
        We'll find out how many elements to skip and which bit to get
        After we find the element, we can generate a mask and perform an AND operation with current element

        For getting a bit 22
        We need to skip 22/8 , i.e 2 elements and set 22%8 i.e 6th bit of 3rd element
        In order to generate a mask with 6th bit set, 0000 0100 We'll left shift 1 2 times (8-6 times)
        After we have a mask we'll just perform a bitwise AND with element 3
        We're ANDing here because we need to see what's set at bit 22nd. ANDing with 1 will give us the correct value


    For Unsetting a bit:
        We'll find out how many elements to skip and which bit to get
        After we find the element, we can generate a mask and perform an AND operation with 0 for a given bit

        For un-setting a bit 22
        We need to skip 22/8 , i.e 2 elements and set 22%8 i.e 6th bit of 3rd element

        In order to generate a mask with only 6th bit unset, i.e 1111 1011
        We'll left shift 1 2 times (8-6 times) and get 0000 0100 and perform a bitwise NOT operation to flip the bits
        So we'll get 1111 1011, once we have the mask, we'll AND it with current element so that only bit 22nd un-sets
"""


class Bitmap:
    def __init__(self, num_of_bits=10):

        if num_of_bits % 8 == 0:
            size = num_of_bits / 8
        else:
            size = (num_of_bits / 8) + 1

        # we're going to keep array of characters (8 bits each) as array of bits
        self.bitarr = [0] * size
        self.min_allowed_bit = 1
        self.max_allowed_bit = (size * 8) - 1

    def set(self, idx):
        if idx < self.min_allowed_bit or idx > self.max_allowed_bit:
            raise Exception("invalid bit, allowed range: [%d, %d]" % (self.min_allowed_bit, self.max_allowed_bit))

        # for setting a bit at idx we need to skip to the bitarr until we reach idx
        # for example if we want to store 22nd bit then we need to skip 2 (8 + 8 i.e idx/8)
        # elements and need to set the 6th bit i.e idx%8
        if idx % 8 == 0:
            skip = (idx / 8) - 1
            bit = 8
            or_with = 1
        else:
            skip = idx / 8
            bit = idx % 8
            # left shift 1 8-bit_idx time
            or_with = 1 << 8 - bit

        self.bitarr[skip] |= or_with

    def unset(self, idx):
        """
        unsets the bit at given index
        """
        if idx < self.min_allowed_bit or idx > self.max_allowed_bit:
            raise Exception("invalid bit, allowed range: [%d, %d]" % (self.min_allowed_bit, self.max_allowed_bit))

        if idx % 8 == 0:
            skip = (idx / 8) - 1
            bit = 8
            and_with = ~1
        else:
            skip = idx / 8
            bit = idx % 8
            # left shift 1 8-bit_idx time and then invert it
            # so we can have
            and_with = ~(1 << 8 - bit)
        self.bitarr[skip] &= and_with

    def get(self, idx):
        """
        gets the bit at given index
        """
        if idx < self.min_allowed_bit or idx > self.max_allowed_bit:
            raise Exception("invalid bit, allowed range: [%d, %d]" % (self.min_allowed_bit, self.max_allowed_bit))

        if idx % 8 == 0:
            skip = (idx / 8) - 1
            bit = 8
            and_with = 1
        else:
            skip = idx / 8
            bit = idx % 8
            # left shift 1 8-bit_idx time
            and_with = 1 << 8 - bit
        return True if self.bitarr[skip] & and_with else False

    def __str__(self):
        return "%s" % self.bitarr


def main():
    bitmap = Bitmap(105)
    for i in range(1, 9):
        bitmap.set(i)
    assert 255 == bitmap.bitarr[0]

    assert True is bitmap.get(1)
    assert False is bitmap.get(9)
    bitmap.set(9)
    assert True is bitmap.get(9)
    bitmap.unset(9)
    assert False is bitmap.get(9)

    bitmap.set(32)
    assert 1 == bitmap.bitarr[3]


if __name__ == '__main__':
    main()
