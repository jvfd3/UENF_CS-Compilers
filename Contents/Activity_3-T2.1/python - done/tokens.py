'''Tokens for lexer'''
from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):
    '''has the type for each token'''
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    LPAREN = 5
    RPAREN = 6


@dataclass
class Token:
    '''Is a class for each token, having its type and respective value'''
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value is not None else "")
