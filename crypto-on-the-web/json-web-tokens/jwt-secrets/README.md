## Analysis
This challenge is teaching the improtance of a strong key. If we take a look at the source code of the page we can see a comment saying `# TODO: PyJWT readme key, change later` which might be a hint of where to find the key and craft our own JWT impersonating someone else.

## Solution
1. By visiting `https://github.com/jpadilla/pyjwt/blob/master/README.rst` we can see in the example code the secret key used is the string `secret`, so this might be the key we want.
2. Generate a JWT for the user `admin` from the website.
3. If we try to decode it without by also verifying the signature it works, so this conmfirms that is our key.
4. We change the `admin` value to `True` and we now encode out modifed JWT with the same key.
5. We send the key to the server to receive the flag.
6. The JWT used to get the flag is: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiYWRtaW4iOiJUcnVlIn0.M_0DWlPMYO1M1UckS4aXtEXG29JlkIhDih5PqeY7r58`
