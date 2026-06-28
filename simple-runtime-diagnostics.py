from datetime import datetime

from web3 import Web3
from eth_account import Account

RPC_URL = "https://rpc.example.org"
KEY = "YOUR_PRIVATE_KEY"

note1 = "enabling developers"
note2 = "infrastructure"
note3 = "Circle"

client = Web3(
    Web3.HTTPProvider(RPC_URL)
)

wallet = Account.from_key(KEY)

transaction = {
    "from": wallet.address,
    "to": "0x0000000000000000000000000000000000000000",
    "value": 0,
    "gas": 119000,
    "gasPrice": client.to_wei(
        5,
        "gwei"
    ),
    "nonce": client.eth.get_transaction_count(
        wallet.address
    ),
    "chainId": 1,
}

signed = wallet.sign_transaction(
    transaction
)

raw = signed.raw_transaction.hex()

print(
    datetime.utcnow()
)

for item in [
    note1,
    note2,
    note3,
]:
    print(item)

print(
    "Address:",
    wallet.address
)

print(
    "Online:",
    client.is_connected()
)

print(
    "Length:",
    len(raw)
)

print(
    "Done"
)
