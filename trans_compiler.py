import lexical_analyzer.lexer as lx;

if __name__ == "__main__":
    try:
        f = open("input.pl", encoding='utf-8')
        lx.Lexer.scan( f )
    finally:
        f.close()