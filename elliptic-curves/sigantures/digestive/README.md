## Analysis
In this challenge the ECDSA algorithm seems to be well-implemented. Although the developers forgot to uncomment the use of the hash function applied to each message before it gets signed. That means the raw message is getting signed every time isntead of its hash. How can we get advantage of that?

The ECDSA algorithm signs only the `Ln` Leftmost bits of the message where `Ln` is equals to the group order of the base point `G`.

This works fine when using hashes because of the avalanche effect in hash methods: one small change generates a whole different hash.

But in our case that the raw message is being signed, the same signature that was used to sing a message `m`
can also be used to verify `m + *` (if `m` is long enough).

So we take advantage of the JSON property that duplicate values overwrite the previous ones to verify:
`{"admin": false, "username": "test", "admin": true}` 

by using the signature from  `{"admin": false, "username": "test"}`

ECDSA Algorithm: https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm