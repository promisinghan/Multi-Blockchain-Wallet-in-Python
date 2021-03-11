from wallet import *

# sending some coins from the first(index 0) account to second(index 1) account
coin = BTCTEST
account = privateKeyToAccount(BTCTEST, coins[BTCTEST][0]['privkey'])
to = 'n2nrtRREqL1QpgjM8iZY8CURxUkehcHSCV'
amount = 0.0022

send_tx(coin, account, to, amount)



