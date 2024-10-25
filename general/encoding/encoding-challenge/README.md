### Analysis
This challenge is giving us the encoding script that runs on the server and we are asked to make a script, that decodes the server's message 100 times. The server's message is 1 of 5 possible encodings.

We are also given a sample python script that has the server communication function ready (send/receive messages).

* Note 1: In the server response JSON the encryption type is given to us so there is no need to make a function that identifies which encoding is used.
* Note 2: We have to make decryption methods for 5 types of encodings.

### Solution

1. For `base64`, `hex`, `utf-8` the decryption code is straight forward using functions we already used for previous challenges
2. For `rot-13` encodings we will use the `codeds.decode()` function from `codecs` library.
3. For `bigint` encodings there is a little more complex encoding happening:
    * The server is taking the number plaintext > converts it to bytes > the bytes are converted to a long number > hex encode. 
    * We can avoid converting the hex back to bytes because we can directly get the number from the hex. So we convert the hex to number (long) > convert the number to bytes > decode to ASCII
