### Analysis
This challenge is giving us 2 images that we have to XOR together using their RGB values in order to find the flag.

A question that might occur as it did to me:
```
Why is XORing these 2 encoded images giving us the flag without knowing the key?
By XORing these 2 encoded images is equivalent to XORing the 2 plaintext images based on this formula:

`encoded_image_1 ^ encoded_image_2 = (plaintext_image_1 ^ key) ^ (plaintext_image_2 ^key) = plaintext_image_1 ^ plaintext_image_2`

So based on the images' contents, XORing the 2 plaintext images together
can result in an image that is somewhat the first image embedded inside the other one.
This happens in situations like this where the one of images is just a white background with black text in the middle.
```

### Solution

1. We will need the PIL library to work with images
2. We will also use numpy library which is widely used in ML because it has built-in easy to use functions to convert images or data into arrays and easily work with them.
3. We bitwise XOR each respective pixel and make a new array for the XORed pixels.
4. We construct the new image where the flag can be seen. The resulting image is the `xor_image.png` contained in this folder. I added it so you can see what I was talking about in the `Analysis` section. We can now see the flag inside the lemur's body.
