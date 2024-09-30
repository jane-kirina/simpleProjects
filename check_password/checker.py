# The script checks how many times a password has been hacked using Pwned Password API
import requests
import hashlib

url = 'https://api.pwnedpasswords.com/range/'


def get_count_of_leaks(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_check(password):
    sha1pass = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5, tail = sha1pass[:5], sha1pass[5:]
    response = requests.get(url + first5)
    return get_count_of_leaks(response, tail)


def check(args):
    count = pwned_check(args)
    if count:
        print(f'"{args}" was detected {count} times in leaked databases')
    else:
        print(f'We didn’t find "{args}" password on any leaked databases')


flag = True
while flag:
    password = input('type "stop" to exit\n'
                     'password: ')

    if password == 'stop':
        flag = False
    else:
        check(password)
