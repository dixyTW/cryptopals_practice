"""
lesson: Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
"""
from base64 import b64encode, b64decode


hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

res = b64encode(bytes.fromhex(hex_str)).decode()

ans = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
assert res == ans
