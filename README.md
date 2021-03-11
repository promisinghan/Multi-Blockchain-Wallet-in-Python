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
from [medium.com](https://medium.com/@harshagoli/hd-wallets-explained-from-high-level-to-nuts-and-bolts-9a41545f5b0))
- What does the HD wallet (Hierarchical Deterministic wallet) do?
: Hierarchical Deterministic wallet (HD wallet) is a new-age digital wallet that automatically generates a hierarchical tree-like structure of public/private addresses (or keys), to address the problem of the user having to generate them on their own. Simply put, the HD wallet is a public/private key tree all starting from a root node (master node).

- What the HD wallet is built with: HD wallets were introduced by BIP32 and later improved by BIP44. BIPs stand for Bitcoin Improvement Proposals. While HD wallets were introduced by Bitcoin community, it is a wallet structure that supports many coins. HD wallets can allow for an entire suite of crypto-wallets to be generated from a single seed phrase, although not a commonly used feature. HD wallet derives all the addresses from a single master seed (hence the name hierarchical). All HD wallets use a variant of the standard 12-word master seed key, and each time this seed is extended at the end by a counter value which makes it possible to automatically derive an unlimited number of new addresses.

- How to use HD wallet: HD wallets eliminate the need for the user to constantly generate and wait for the secure keys to be generated, so the users only need to worry about taking the backup.
HD wallet tree is represented by derivation paths to the first address node. For examples, the default for Ethereum is m/44'/60'/0'/0. Each number in that path represents a certain level in the tree such as  m/ proposal' / coin_type' / account' / chain / address_index.
To construct a transaction, the users use the private key of the address node to sign a transaction spending money from the address node's public key.


## Test transactions
Now, fund the wallets using testnet faucet. Open up a new terminal window (gitbash on windows) inside of the project folder/directory, then run *python*. Within the Python shell, run from wallet import *  - you can now access the functions in the wallet.py (your universal wallet script) interactively. You'll need to set the account with *priv_key_to_account* and use *send_tx* to send transactions.
- ### BTCTEST transaction
1. Fund a BTCTEST address using the [bitcoin testnet faucet](https://testnet-faucet.mempool.co/).

![funding BTCTEST to 1st wallet](https://github.com/promisinghan/


 ![screenshot1](https://github.com/promisinghan/Blockchain/blob/main/screenshot/screenshot1.PNG))



2. Use a [block explorer](https://tbtc.bitaps.com/) to watch transactions on the address.

3. Send a transaction to another testnet address (either one of your own, or the faucet).

4. Screenshot the confirmation of the transaction like so:








- ### Ethereum transaction











