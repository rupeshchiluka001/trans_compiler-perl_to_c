import enum

class Tag(enum.Enum):
    NUM = 256
    ID = 257

class Token:
    tag = 0

    def __init__ (self, t):
        self.tag = t

class Word (Token):
    lexeme = ""

    def __init__ (self, t, s):
        super(t)
        self.lexeme = s