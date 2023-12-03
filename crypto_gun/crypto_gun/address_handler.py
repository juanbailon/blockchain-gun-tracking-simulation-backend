from eth_account import Account
import secrets
priv = secrets.token_hex(32)
private_key = "0x" + priv
print ("SAVE BUT DO NOT SHARE THIS:", private_key)
print(priv)
acct = Account.from_key(private_key)
print("Address:", acct.address)



from eth_utils import is_address

# Check if the address is valid
valid = is_address(acct.address)

print(f"Address is valid: {valid}")