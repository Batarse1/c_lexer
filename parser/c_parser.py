from tokens import tokens
from tokens import sync_tokens
from parsing_table import table_ll1

from .parser_find_rules import find_rules
from .parser_find_column import find_column
from .parser_add_to_stack import add_to_stack
from symbols_table.symbols_table import generate_symbols_table
from symbols_table.print_table import print_table

stack = ['EOF', 0]

def c_parser(lexer, file_path):
    symbols_table = {}
    lexer_tokens = []
    tok=lexer.token()
    panic_mode = False
    fail_input = False

    x=stack[-1]

    while True:
        if panic_mode and tok.type not in sync_tokens:
            # print("Token pass = " + str(x))
            tok=lexer.token()
            continue
        else: 
            panic_mode = False
        # print("tok.type = " + tok.type)
        # print("x = " + str(x))
        # print("Stack = " + str(stack))

        symbols_table = generate_symbols_table(tok, lexer, x)
        if x == tok.type and x == 'EOF':
            if (not fail_input):
                print("The code was recognized successfully")
                print_table(symbols_table, ["key", "type", "value", "line number", "position", "level"])
                # generate_symbols_table(lexer_tokens)
            return
        else:
            if x == tok.type and x != 'EOF': #terminal
                # print("Current stack = " + str(stack))
                stack.pop()
                # print("Poped stack = " + str(stack))
                x=stack[-1]
                # print("------------")
                lexer_tokens.append({
                    "type": tok.type,
                    "value": tok.value,
                    "line_number": tok.lineno,
                    "position": tok.lexpos,
                    "level": lexer.level,
                })
                tok=lexer.token()
                continue
            if x in tokens and x != tok.type:
                print("Compilation Failed")
                print(file_path + ":" + str(tok.lineno) + ":" + str(lexer.column) + " error: invalid suffix " + str(tok.value) + ", was expected '" + str(x) + "'")
                panic_mode = True
                fail_input = True
                if x == "EOF":
                    return
                stack.pop()
                x = stack[-1]
                # return 0;
            elif x not in tokens: #non-terminal
                # print("Entering to the table")
                cell=find_rules(table_ll1, x,tok.type)
                # print("Cell = " + str(cell))
                if cell is None:
                    print("Compilation Failed")
                    print(file_path + ":" + str(tok.lineno) + ":" + str(lexer.column) + " error: was not expected " + str(tok.type) + " in position " + str(lexer.column))
                    panic_mode = True
                    fail_input = True
                    if tok.type == "EOF":
                        return
                    tok = lexer.token()
                    # return 0;
                else:
                    # print("Current stack = " + str(stack))
                    stack.pop()
                    # print("Poped stack = " + str(stack))
                    add_to_stack(stack, cell)
                    # print("Added stack = " + str(stack))
                    # print("------------")
                    x=stack[-1]