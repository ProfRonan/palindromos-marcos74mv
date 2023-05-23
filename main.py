"""Main functions"""


def is_palindrome(string: str) -> bool:
    
    string = ''.join(c.lower() for c in string if c.isalnum())

    return string == string[::-1]

testes_1 = ["", "a", "arara", "ola", "ovo", "mundo", "ame o poema", "Ame o poema!", "Hello, world!", "ola mundo", "Anotaram a data da maratona!"]

for teste_2 in testes_1:
    print(f">>> is_palindrome(\"{teste_2}\")")
    print(is_palindrome(teste_2))
    print()


