import random
import string

def generated_code():
    characters = string.digits
    cod = ''.join(random.choice(characters) for i in range(6))
    return cod