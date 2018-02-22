from pwnedpasswords import haveibeenpwned
import binascii
import os
import unittest

class PwnedPasswordsTest(unittest.TestCase):

    def test_bad_password(self):
        result = haveibeenpwned("123456")
        self.assertGreater(result, 0)

    def test_good_password(self):
        result = haveibeenpwned(binascii.hexlify(os.urandom(32)).decode())
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
