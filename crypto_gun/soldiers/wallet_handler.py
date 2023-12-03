import secrets
from cryptography.fernet import Fernet
from django.conf import settings
from eth_account import Account
from eth_utils import is_address

class EncryptionHandler:

    @staticmethod
    def encryp_value(value: str) -> bytes | None:
        if value:
            return Fernet(settings.MY_ENCRYPTION_KEY).encrypt(value.encode())
        return None

    @staticmethod
    def decryp_value(enctypted_value: bytes) -> str | None:
        if enctypted_value:
            return Fernet(settings.MY_ENCRYPTION_KEY).decrypt(enctypted_value.encode()).decode()
        return None


class WalletHandler:

    @staticmethod
    def generate_private_key() -> str:
        priv = secrets.token_hex(32)
        private_key = "0x" + priv

        return private_key
    
    @staticmethod
    def generate_eth_account(private_key: str) -> Account:
        acct = Account.from_key(private_key)
        return acct

