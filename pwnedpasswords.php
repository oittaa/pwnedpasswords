<?php
/*
This script uses the pwnedpasswords.com v2 API to check your password in a secure way.
https://en.wikipedia.org/wiki/K-anonymity
The full hash is never transmitted over the wire, only the first 5 characters. The comparison
happens offline. Special thanks to Troy Hunt (@troyhunt) for making this script possible.
*/
namespace PwnedPasswords;

define("API_URL", "https://api.pwnedpasswords.com/range/");
define("USERAGENT", "Pwnage-Checker");

/**
 * This function takes a password string as an input and returns the number of times the password
 * appears in PwnedPasswords. Any number greater than zero means that the password has been pwned.
 * @param string $password The password to be tested
 * @return int The number of times the password appears in PwnedPasswords
 */
function haveibeenpwned($password) {
    $passhash = strtoupper(sha1($password));
    $ph_short = substr($passhash, 0, 5);

    $url = API_URL.$ph_short;
    $options = array(
      'http' => array(
        'header'  => "User-Agent: ".USERAGENT."\r\n",
        'method'  => 'GET',
      ),
    );
    $context  = stream_context_create($options);
    $passlist = file_get_contents($url, false, $context);

    $lines = explode("\n", $passlist);
    foreach($lines as $line) {
        $larr = explode(":", $line);
        if ($ph_short . $larr[0] === $passhash) {
            return (int) trim($larr[1]);
        }
    }
    return 0;
}
