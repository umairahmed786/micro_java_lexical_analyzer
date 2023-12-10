from transitionTable import *


bufferLength=10000
keywords=['if', 'else','while','read','print','return','void','final','new','program','class']


class lexicalsymbol():
    rowNum = None
    colNum = None
    lexeme = None
    tokenType = None


    def __init__(self,row,col,lexeme) -> None:
        self.rowNum = row
        self.colNum = col
        self.lexeme = lexeme
        if lexeme in keywords:
            self.tokenType="keyword"
        else:
            self.tokenType = get_token_type(str(lexeme))