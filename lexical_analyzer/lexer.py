import re

class Lexer :

    __delim_str = ' |\n|\t|\r|\+|-|\)|\(|\*|&|%|/|=|;'

    def get_delim_str (self):
        return self.__delim_str

    @classmethod
    def scan(self, file_pointer) :

        for line in file_pointer:
            if len(line) < 2:
                continue

            token_array = re.split( self.get_delim_str(self), line )
            token_array = list( filter(None, token_array) )
            print(token_array)