input = 'amritmanash9@gmail.com'

def encrypt_email(input:str):
    initial = input.split('@')[0]
    domain = input.split('@')[1]
    return initial[0]+(len(initial)-2)*'*'+initial[-1]+'@'+domain

print(encrypt_email(input))

#output: 
a**********9@gmail.com
