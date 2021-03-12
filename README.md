> # Multi-Blockchain Wallet in Python 
# Unit 19 | Blockchain-Python: multi-blockchain wallet using HD wallet

## Background

Your new startup is focusing on building a portfolio management system that supports not only traditional assets
like gold, silver, stocks, etc, but crypto-assets as well! The problem is, there are so many coins out there! 
It's a good thing you understand how HD wallets work, since you'll need to build out a system that can create them.
You're in a race to get to the market. There aren't as many tools available in Python for this sort of thing, yet.
Thankfully, you've found a command line tool, hd-wallet-derive that supports not only BIP32, BIP39, and BIP44, but also supports non-standard derivation paths for the most popular wallets out there today! 
However, you need to integrate the script into your backend with your dear old friend, Python. Once you've integrated this "universal" wallet, you can begin to manage billions of addresses across 300+ coins, giving you a serious edge against the competition.
In this assignment, however, you will only need to get 2 coins working: Ethereum and Bitcoin Testnet.
*Ethereum keys are the same format on any network, so the Ethereum keys should work with your custom networks or testnets.*
<br>
<br>

>Let's do it!
![free will is not free](https://collider.com/wp-content/uploads/2020/02/westworld-season-3-poster.jpeg "Free will is not Free.")

*Photo from [COLLIDER](https://collider.com/westworld-season-3-poster-free-will-is-not-free/)*


## Short desciprtion about the wallet
(from [investopedia.com](https://www.investopedia.com/terms/h/hd-wallet-hierarchical-deterministic-wallet.asp ) and
 [medium.com](https://medium.com/@harshagoli/hd-wallets-explained-from-high-level-to-nuts-and-bolts-9a41545f5b0))
- What does the HD wallet (Hierarchical Deterministic wallet) do?
: Hierarchical Deterministic wallet (HD wallet) is a new-age digital wallet that automatically generates a hierarchical tree-like structure of public/private addresses (or keys), to address the problem of the user having to generate them on their own. Simply put, the HD wallet is a public/private key tree all starting from a root node (master node).

- What the HD wallet is built with: HD wallets were introduced by BIP32 and later improved by BIP44. BIPs stand for Bitcoin Improvement Proposals. While HD wallets were introduced by Bitcoin community, it is a wallet structure that supports many coins. HD wallets can allow for an entire suite of crypto-wallets to be generated from a single seed phrase, although not a commonly used feature. HD wallet derives all the addresses from a single master seed (hence the name hierarchical). All HD wallets use a variant of the standard 12-word master seed key, and each time this seed is extended at the end by a counter value which makes it possible to automatically derive an unlimited number of new addresses.

- How to use HD wallet: HD wallets eliminate the need for the user to constantly generate and wait for the secure keys to be generated, so the users only need to worry about taking the backup.
HD wallet tree is represented by derivation paths to the first address node. For examples, the default for Ethereum is m/44'/60'/0'/0. Each number in that path represents a certain level in the tree such as  m/ proposal' / coin_type' / account' / chain / address_index.
To construct a transaction, the users use the private key of the address node to sign a transaction spending money from the address node's public key.


## Send some transactions!
Now, fund the wallets using testnet faucet. Open up a new terminal window (gitbash on windows) inside of the project folder/directory, then run *python*. Within the Python shell, run from wallet import *  - you can now access the functions in the wallet.py (your universal wallet script) interactively. You'll need to set the account with *priv_key_to_account* and use *send_tx* to send transactions.
- ### BTCTEST transaction (Bitcoin Testnet transaction)
1. Fund a BTCTEST address using the [bitcoin testnet faucet](https://testnet-faucet.mempool.co/).

![funding BTCTEST to 1st wallet](https://github.com/promisinghan/multi_blockchain_wallet_in_python/blob/main/screenshot/funding_btctest.png "Funding BTCTEST to my 1st BTCTEST wallet")


2. Use a [block explorer](https://tbtc.bitaps.com/) to watch transactions on the address.

![successful funding BTCTEST to 1st wallet](https://github.com/promisinghan/multi_blockchain_wallet_in_python/blob/main/screenshot/funding_1stwallet_btctest.png "Succesfully funded BTCTEST to my 1st wallet")

![successful funding transaction to 1st wallet](https://github.com/promisinghan/multi_blockchain_wallet_in_python/blob/main/screenshot/funding_btctest_transaction.png "Displaying the successful funding transaction to my 1st BTCTEST wallet")

3. Send a transaction to another testnet address (either one of your own, or the faucet).

I ran *python test_BTCTEST.py* on Gitbash after running *python wallet.py*, instead of using Python shell on Gitbash.
After that, I went to the block explorer to watch transactions and then screenshotted them as below.

![transacting BTCTEST to 2nd wallet](https://github.com/promisinghan/multi_blockchain_wallet_in_python/blob/main/screenshot/transaction_to_2ndwallet_btctest.png "Sending BTCTEST from my 1st wallet to 2nd wallet")

4. Screenshot the confirmation of the transaction like so:


![successful Bitcoin testnet transaction](https://github.com/promisinghan/multi_blockchain_wallet_in_python/blob/main/screenshot/transaction_to_2ndwallet_btctest_transaction.png "Successful BTCTEST transaction from my 1st wallet to 2nd wallet")


- ### Local PoA ETH(Ethereum) transaction

1. Fund one of the ETH addresses by adding it to the pre-allocated accounts in your networkname.json 
In my case, I added the first ETH address (index 0) to melon.json as shown in the below screenshot.

![Adding one of the ETH addresses to the pre-allocated accounts in melon.json](https://github.com/promisinghan/multi_blockchain_wallet_in_python/blob/main/screenshot/adding%20mneumonic-derived%20wallet%20to%20custom%20network%20json%20file%20to%20prefund.png "I added the first ETH addresses to the pre-allocated accounts in melon.json to pre-fund it")


2. Delete the geth folder in each node, then re-initialize using geth --datadir nodeX init networkname.json. This will create a new chain, and will pre-fund the new account.
In my case, I ran

 ./geth --datadir node1 --unlock 0xa1cE03EB9453d9D68902a6CD7d53B653b142BA9D --mine --rpc --allow-insecure-unlock

 for node1, and I ran 

 ./geth --datadir node2 --unlock 0x38333aE5426B5900E536A72D538ce8D266D8f601 --mine --port 30304 --bootnodes "enode://aefd693c5555dd40cbd4e92bc09798813f056b767b8aa79c7a737b965f2976179a0e41fa7eb18fc6a48ada6485e465b6ba6445fe8cf723d1c2747ebc131d08bd@127.0.0.1:30303" --ipcdisable --allow-insecure-unlock

 for node2 on Gitbash inside the Blockchain-Tools folder.

 3. Add the following middleware to wallet.py to support the PoA algorithm:

 from web3.middleware import geth_poa_middleware
 
 w3.middleware_onion.inject(geth_poa_middleware, layer=0)

 4. Due to a bug in web3.py, you will need to send a transaction or two with MyCrypto first, since the w3.eth.generateGasPrice() function does not work with an empty chain. You can use one of the ETH address privkey, or one of the node keystore files. 
I sent a transaction on MyCrypto from my node 1 account to my first ETH address.

5. I made sure Ganache is open to make my local host (RPC SERVER HTTP://127.0.0.1:8545) available.

On Gitbash, I activated ethereum2 environment where I installed web3 libary by 

conda activate ethereum2

Then inside my project folder, I ran 

python wallet.py

and then I ran 

python test_ETH.py

I could get the transaction hash or transaction id as a result as shown below, such as 

0xff9e574e7764fc3d93a5c117f9230b1265fa75e74fa740e088237c097248ca9d

![Getting transaction id after transaction](https://github.com/promisinghan/multi_blockchain_wallet_in_python/blob/main/screenshot/running%20wallet%20file%20on%20Gitbash%20in%20ethereum2%20enviroment.png "I obtained the transaction id after I transacted ETH from the 1st wallet address to 2nd wallet address")


I copied and pasted this transaction id into MyCrypto's TX Status and screenshot the succssful transaction as shown below:

![Checking transaction status using the transaction id](https://github.com/promisinghan/multi_blockchain_wallet_in_python/blob/main/screenshot/checking%20transaction%20with%20txhash%20on%20Mycrypto.png "I copied and pasted the transaction id obtained into MyCrypto's TX status and screenshotted the successful transaction")


Celebrate the fact that I now have an incredibly powerful wallet that I can expand to hundreds of coins!
![Let's celebrate](https://cdn.pixabay.com/photo/2017/01/04/21/00/new-years-eve-1953253_1280.jpg "Let's celebrate!")

*Photo from [pixabay.com](https://pixabay.com/photos/new-year-s-eve-fireworks-beacon-1953253/) by [nck_gsl](https://pixabay.com/users/nck_gsl-3554748/)*


