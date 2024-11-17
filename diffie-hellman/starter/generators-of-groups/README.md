## Analysis
In this challenge we have the finite field `F` which contains all numbers from 1 until `p`.

We are asked to find the smallest number `g` for which every element from `F` can be written `as g^n mod p`.

In simpler words, `g` must generate `p-1`(we exclude zero) unique numbers. In order to brute force this, 
we can generate the first `p-1` numbers from 1 until `p-1` of the formula `g^n mod p`.

So we will calculate `g^1 mod p`, `g^2 mod p`, .... , `g^(p-1) mod p`. This will give us `p-1` numbers.

If these are all distinct then it means we have generated the whole `F` excluding the zero.

## Solution
1. We iterate for possible `g` from 2 until `p`.
2. We generate the whole field H = {`g^1 mod p`, `g^2 mod p`, .... , `g^(p-1) mod p`}
3. We add all those elements in a set because we need uniqueness.
4. For the first `g` that the set H has `p-1` unique elements we stop the execution
because the first `g` we find will also be the smallest one.

