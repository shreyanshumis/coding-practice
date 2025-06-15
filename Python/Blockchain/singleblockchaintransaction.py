from web3 import Web3
from eth_account import Account

# Connect to an Ethereum node (e.g., using Infura)
infuraUrl = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(infuraUrl))

# Check if connected to the network
if web3.isConnected():
    print("Connected to Ethereum node")

# Sender's address and private key
senderAddress = "0xYourSenderAddress"
privateKey = "YourPrivateKey"

# Receiver's address
receiverAddress = "0xReceiverAddress"

# Create the transaction
transaction = {
    'to': receiverAddress,
    'value': web3.toWei(0.01, 'ether'),  # Sending 0.01 Ether
    'gas': 21000,
    'gasPrice': web3.toWei('50', 'gwei'),
    'nonce': web3.eth.getTransactionCount(senderAddress),
    'chainId': 1  # Ethereum Mainnet ID
}

# Sign the transaction
signedTxn = web3.eth.account.sign_transaction(transaction, privateKey)

# Send the transaction
txHash = web3.eth.sendRawTransaction(signedTxn.rawTransaction)

# Print the transaction hash
print(f"Transaction successful with hash: {web3.toHex(txHash)}")
