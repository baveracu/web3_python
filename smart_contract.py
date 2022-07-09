from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

print(web3.eth.block_number)

account_1 = "0xFeEaa23C5e54F4060A3CF482D108078bFec982bA"
account_2 = "0x5796f8fbfce1058Bdb83aC5B0f1E0D60BaF953EB"

private_key_1 = "ef8c2b2f02fa11ed988469e2b80c183d79b001dd97079b80d1feaa64429f897a"

# get the nonce
nonce = web3.eth.getTransactionCount(account_1)
# build a transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}
# sign a transaction
signed_tx = web3.eth.account.sign_transaction(tx, private_key_1)
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
# send a transaction
# get a transaction hash