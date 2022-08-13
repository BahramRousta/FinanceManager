import hashlib
from typing import Optional, Any

import pyotp
from pyotp import TOTP


class Totp(TOTP):

    def __init__(self, s: str, digits: int = 6, digest: Any = hashlib.sha1, name: Optional[str] = None,
                 issuer: Optional[str] = None, interval: int = 300) -> None:
        self.interval = interval
        super().__init__(s, digits, digest, name, issuer, interval)


def generate_otp():
    totp = Totp('base32secret3232')
    code = totp.now()
    return code

