#!/usr/bin/env python3
"""
This script uses the pwnedpasswords.com v2 API to check your password in a secure way.
https://en.wikipedia.org/wiki/K-anonymity
The full hash is never transmitted over the wire, only the first 5 characters. The comparison
happens offline. Special thanks to Troy Hunt (@troyhunt) for making this script possible.
"""
from hashlib import sha1
from urllib.request import urlopen, Request

API_URL = "https://api.pwnedpasswords.com/range/{0}"
HEADERS = {"User-Agent" : "Pwnage-Checker"}

def haveibeenpwned(password: str) -> int:
    """
    This function takes a password string as an input and returns the number of times the password
    appears in PwnedPasswords. Any number greater than zero means that the password has been pwned.

    :param password: The password to be tested
    :type password: string

    :return: The number of times the password appears in PwnedPasswords
    :rtype: integer
    """
    passhash = sha1(password.encode("utf-8")).hexdigest().upper()
    ph_short = passhash[:5]
    url = API_URL.format(ph_short)
    req = Request(url=url, headers=HEADERS)
    passlist = urlopen(req).read().decode("utf-8")
    for line in passlist.split("\n"):
        larr = line.split(":")
        if ph_short + larr[0] == passhash:
            return int(larr[1].strip())
    return 0

def main():
    """Ask user for their password and check its hash against PwnedPasswords"""
    from getpass import getpass
    print("Welcome to PwnedPasswords")
    print("Your password will not be transmitted over the network!")

    result = haveibeenpwned(getpass("Password to check: "))
    if result != 0:
        print("Found your password {} times.".format(result))
    else:
        print("Your password did not appear in PwnedPasswords yet.")

if __name__ == "__main__":
    main()
