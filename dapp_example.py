from web3 import Web3

# Fill in your infura API key here
infura_url = "https://mainnet.infura.io/v3/2a081d039e58489abbaa03afdf511710"
web3 = Web3(Web3.HTTPProvider(infura_url))

account = web3.eth.account.create()
print(account.address)
print(account.privateKey)
keystore = account.encrypt('foobar')
print(keystore)

print(web3.eth.account.decrypt(keystore, 'foobar'))
account.sign_transaction('{}')
