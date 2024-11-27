## Analysis
In this challenge a custom CTR mode is supposed to be implemented but with a closer look at the code we can notice that this is not happening because of 3 things:
1) `self.stup` is always False
2) In the increment function, the same calculation `self.newIV = hex(int(self.value, 16) - self.stup)` is done every time because `self.stup` is always False.
3) The result of the above is always `hex(int(self.value, 16))` because `self.stup` is always False (0).

Conclusion: the same bytes are used into the block cipher encryption for every block.

The encryption here is downgraded from a CTR mode stream cipher to an XOR encryption with the same key for each block of the image.

By knowing 1 block of plaintext value is enough to find the key. We can use the PNG image header for this which is exactly 16 bytes.

## Solution
1) Copy the PNG image header that is common for all PNG images from: https://en.wikipedia.org/wiki/PNG
2) Find the key by calculating `plaintext ^ ciphertext => header ^ first block`
3) XOR every image block with the key and concatenate them to create the flag image.