'''Code for simple math expressions lexer'''

from tokens import Token, TokenType

WHITESPACE = ' \n\t'
DIGITS = '0123456789'


class Lexer:
    '''Lexer class to analyze math expressions'''

    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        '''goes to the next char(?)'''
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        '''checks if token is valid and yield its value'''
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char == '.' or self.current_char in DIGITS:
                yield self.generate_number()
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            else:
                raise Exception(f"Illegal character '{self.current_char}'")

    def generate_number(self):
        '''generates the numbers used'''
        decimal_point_count = 0
        number_str = self.current_char
        self.advance()

        # is_dot_or_char = self.current_char == '.' or self.current_char in DIGITS
        while self.current_char is not None and (self.current_char == '.' or self.current_char in DIGITS):
            if self.current_char == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break

            number_str += self.current_char
            self.advance()

        def starts_with(str_number, initial_value):
            '''checks first element'''
            return str_number[0] == initial_value

        def ends_with(str_number, initial_value):
            '''checks first element'''
            return str_number[-1] == initial_value

        number_str = str(number_str)
        if starts_with(number_str, '.'):
            number_str = '0' + number_str
        if ends_with(number_str, '.'):
            number_str += '0'

        return Token(TokenType.NUMBER, float(number_str))
