from lexer.c_lexer import c_lexer
from parser.c_parser import c_parser

def main():
    file_path = "main.c"

    lexer = c_lexer()
    
    file = open(file_path, "r")
    lexer.input(file.read() + "$")

    c_parser(lexer, file_path)

main();