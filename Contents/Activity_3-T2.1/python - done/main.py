'''https://youtu.be/88lmIMHhYNs'''
from lexer import Lexer

while True:
    text = input("calc > ")
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    print(list(tokens))
