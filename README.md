# PwnedPasswords

This script uses the pwnedpasswords.com v2 API to check your password in a secure way.

https://en.wikipedia.org/wiki/K-anonymity

The full hash is never transmitted over the wire, only the first 5 characters. The comparison
happens offline. Special thanks to Troy Hunt (@troyhunt) for making this script possible.

## Usage

```sh
./pwnedpasswords.py
```

The output will either be:

```
Password to check: 
Your password did not appear in PwnedPasswords yet.
```

or in case your password is not secure

```
Password to check: 
Found your password 5728 times.
```

## Integrate to your own programs

### Python

```python
from pwnedpasswords import haveibeenpwned

password = 'P@ssword'

result = haveibeenpwned(password)
if result > 0:
	# Password FOUND from PwnedPasswords, ABORT!
	print("ABORT!")
else:
	# Password not found from PwnedPasswords, continue...
	print("continue...")
```

### PHP

```php
<?php

require_once('pwnedpasswords.php');

$password = 'P@ssword';

$result = PwnedPasswords\haveibeenpwned($password);
if ($result > 0) {
  // Password FOUND from PwnedPasswords, ABORT!
  echo "ABORT!\n";
} else {
  // Password not found from PwnedPasswords, continue...
  echo "continue...\n";
}
```