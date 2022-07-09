from web3 import Web3

# Fill in your infura API key here
infura_url = "https://mainnet.infura.io/v3/2a081d039e58489abbaa03afdf511710"
web3 = Web3(Web3.HTTPProvider(infura_url))

latest = web3.eth.block_number

print(web3.eth.get_block(latest))

tx_hash = '0x17691fb3d16e7d41b2f41a953533fd80cbf6d3ee46efc98e44e489c744e0bba6'
print(web3.eth.getTransactionByBlock(tx_hash,2))