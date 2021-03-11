from wallet import *

# sending some coins from the first(index 0) account to second(index 1) account
coin = ETH
account = privateKeyToAccount(ETH, coins[ETH][0]['privkey'])
to = '0xebcceDE0B93d33E975afAc529b7306a9403D4Ee8'
amount = 3333333333333333333

send_tx(coin, account, to, amount)


