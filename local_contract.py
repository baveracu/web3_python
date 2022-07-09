import json
from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.default_account = web3.eth.accounts[0]
abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
address = web3.toChecksumAddress("0xbd060a51398Fb2da69fb05d508189CCe8621f887")

contract = web3.eth.contract(address=address, abi=abi)
tx_hash = contract.functions.setGreeting('HEEEELLOOOO@').transact()
print(tx_hash)
web3.eth.wait_for_transaction_receipt(tx_hash)
print(contract.functions.greet().call())