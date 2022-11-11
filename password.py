import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+ query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError (f"Hashing error {res.status_code}")
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def passwordChecking(args):
    count = pwned_api_check(args)
    if count:
        result = {"api_response": f"{args} was found {count} times. You should probably consider a change."}
        return result["api_response"]
    else:
        result = {"api_response": f"{args} was not found! Carry on."}
        return result["api_response"]

def test():
    return 'this is a test'