import requests
from bs4 import BeautifulSoup
import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from Crypto.PublicKey import RSA
from Crypto.Util.number import *
    
def get_certificates_ids(domain):
    url = f"https://crt.sh/?q={domain}"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error with status code: {response.status_code}")
        return None
    
    html = BeautifulSoup(response.text, 'html.parser')
    
    # The certificates are in the the third <TABLE> HTML tag
    cert_table = html.find_all('table')[2]
    
    certificates = []
    
    # Extract all the <TR> HTML tags which contain the certificates
    for row in cert_table.find_all('tr')[1:]:
        # The id is in the first <TD> tag
        columns = row.find_all('td')
        cert_id = columns[0].text.strip()
        certificates.append(cert_id)
    
    return certificates

def pub_key_modulus_matches_cert_id(cert_id, modulus_hex_line):
    url = f"https://crt.sh/?id={cert_id}"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error with status code: {response.status_code}")
        return None
    
    html = BeautifulSoup(response.text, 'html.parser')
    text = html.get_text()
    
    if modulus_hex_line in text:
        return True
    return False

def construct_first_line(modulus_hex):
    result = ""
    i=0
    while i < 30:
        result = result + f'{modulus_hex[i]}{modulus_hex[i+1]}:'
        i+=2
    return result

URL = "cryptohack.org"
pem_data = open("transparency.pem", 'rb').read()

certificate_ids = get_certificates_ids(URL)

key = RSA.importKey(pem_data)
modulus = key.n

# Throw away the first 2 characters which are 0x
modulus_hex = hex(modulus)[2:]

# Prepend with 00 (read analysis)
modified_hex = "00" + modulus_hex

first_line_of_hex = construct_first_line(modified_hex)
print(f'Modulus: {modulus}')

for id in certificate_ids:
    result = pub_key_modulus_matches_cert_id(id, first_line_of_hex)
    print(f'Searching certificate with ID: {id}')
    if result:
        print(f'FOUND IT: visit https://crt.sh/?id={id} to see the certificate')
        exit(0)
        