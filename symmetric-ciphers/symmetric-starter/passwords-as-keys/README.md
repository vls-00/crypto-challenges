## Solution
By reading the server source code we notice that the key is made from a random word picked from a wordlist that it is also provided (https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words).

This can be used to bruteforce the key by trying every word as the key on the ciphertext.