#asks for password
passWord=input(str("Please enter the password: "))
#checks the length of the password
if len(passWord) != 8:
    print("Your password is not the correct length")
else:
    print("Your password is the right length.")
#list of symbols, needs one within password    
(symbol) = [ "$", "!", "£", "%", "^", "?", "&", "*", "#" ]
if any(sym in passWord for sym in symbol):
    print("Your password includes a correct symbol.")
else:
    print("Your password needs to include an acceptable symbol, e.g, £, $, !...")
