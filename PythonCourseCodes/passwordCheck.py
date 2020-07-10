import requests
from hashlib import sha1
import sys


def request_api_data(string):
    url = "https://api.pwnedpasswords.com/range/" + string
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching :{res.status_code}, check API and try again")
    return res


def get_password_leaks_count(hashes, password_hash):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, c in hashes:
        if h == password_hash:
            return c
    return 0


def pwned_api_check(password):
    query_string = sha1(password.encode('utf-8')).hexdigest().upper()
    head, tail = query_string[:5], query_string[5:]
    response = request_api_data(head)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        print(password)
        if count != 0:
            print(
                f"Your Password has been compromised. Your password was found {count} times.\n"
                f"Please Change your password 🤨 🤨\n")
        else:
            print('You\'re safe. Don\'t share your password with anyone')


if __name__ == '__main__':
    main(sys.argv[1:])
