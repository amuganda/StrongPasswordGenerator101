import random

chars = 'abcdefghijklmnopqrstuvwxyz@!$&£_%1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'

length = input('Password Length Required (Minimum 8 characters): ')
length = int(length)

generate = input('Passwords Required (1-10): ')
generate = int(generate)

for outputnum in range(generate):
  password = ''
  for chosenlength in range(length):
    password += random.choice(chars)
  print(password)
