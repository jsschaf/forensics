#!/usr/bin/env python
from __future__ import print_function


import base64
import sys


PEM = ("""-----BEGIN RSA PRIVATE KEY-----
    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
    -----END RSA PRIVATE KEY-----""")


def via_cryptography(message):
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.backends import default_backend
    private_key = serialization.load_pem_private_key(PEM, password=None, backend=default_backend())
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import padding
    return private_key.sign(message, padding.PKCS1v15(), hashes.SHA1())

def via_openssl(message):
    import subprocess
    import tempfile
    with open("my-pem", "wb+") as f:
        f.write(PEM)
        f.flush()
        p = subprocess.Popen(
                             "openssl rsautl -sign -inkey " + f.name,
                             shell=True,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    stdout, stderr = p.communicate(input=message)
    if stderr or p.returncode != 0:
        print(stderr)
    return stdout


def via_pycrypto(message):
    from Crypto.PublicKey import RSA
    from Crypto.Hash import SHA
    from Crypto.Signature import PKCS1_PSS
    rsakey = RSA.importKey(PEM)
    return rsakey.encrypt(message, None)[0]


def via_pyopenssl(message, digest="sha1"):
    import OpenSSL
    key = OpenSSL.crypto.load_privatekey(OpenSSL.crypto.FILETYPE_PEM, PEM)
    return OpenSSL.crypto.sign(key, message, digest)


def via_rsa(message):
    import rsa
    privkey = rsa.PrivateKey.load_pkcs1(PEM)
    return rsa.sign(message, privkey, "SHA-1")


def via_ruby(message):
    import subprocess
    syntax = (
              "require 'openssl'; key = OpenSSL::PKey::RSA.new('%s'); "
              "print key.private_encrypt('asdf')"
              ) % PEM
    return subprocess.check_output('ruby -e "%s"' % syntax, shell=True)


if __name__ == "__main__":
    message = "collective"
    for each in (via_cryptography, via_openssl, via_pycrypto, via_pyopenssl,
                 via_rsa, via_ruby):
        print("Using %s:" % each.__name__)
        print(base64.b64encode(each(message)))
        print()
