## Analysis
This challenge is giving us an RSA key public key and is asking us to find a certificate that uses the key's parameters which are the modulus and the exponent. The challenge is also teaching about certificate trasparency and we can use the website `https://crt.sh/` to search for transparent certificates.
* Note: We do not have to take the exponent into consideration as almost all certificates have the same exponent (65537). The modulus is sufficient in order to find the certificate.

## Solution

1. We extract the modulus from the key.
2. We convert it to hex and remove the first 2 characters which are `0x`.
3. After taking a look at the transparent certificates I noticed every certificate starts with `00`
and I read online that is used to ensure the number is treated as positive so I also added `00` at the start of the hex modulus we extracted.
4. Now we can search for `cryptohack.org` in `https://crt.sh/` and fetch the whole HTML page using `BeautifulSoup`.
5. By looking at the page's source code we can see that the certificate IDs are in the second `<TABLE>` HTML tag inside the `<TR>` and `<TD>` tags so we use `BeautifulSoup` to extract all the tags and keep the certificate IDs for the domain `cryptohack.org`. We need those for later.
6. Now that we have the certificate IDs we can iterate through all of them in their respective page (e.g `https://crt.sh/?id=id`) and fetch the HTML page for each ID we extracted.
7. By looking at the HTML code again we can notice that the RSA modulus in the HTML is splited in each line containing 30 characters of the modulus and every 2 characters there is a delimiter `:`
8. I constructed only the first line of the modulus in the same format which are the first 30 hexabytes of the modulus (including `00`) and added `:` every 2 characters.
9. I thought that the certificates might not be that many so it will be sufficient if I only construct the first line of the modulus and search each certificate page by it. In the worst case we will find a false positive and we are gonna construct the second line too.
10. Now we iterate all certificate IDs and their respective page and we try to find the one matching our first hexabyte line of the modulus using `BeautifulSoup` to extract the whole text from the HTML page and search inside the text.

Note: the line we contructed is `00:b9:88:f4:ea:6e:6a:e0:cf:12:b0:44:30:29:7f:` and if you visit `https://crt.sh/?id=3347792120` you can see the certificate that has this exact line is it's RSA modulus. This is the certificate we want. 
This certificates was issued for the subdomain `thetransparencyflagishere.cryptohack.org`. If we visit that, we get the flag.