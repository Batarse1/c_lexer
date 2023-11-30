from tokens import tokens
from tokens import sync_tokens
from parsing_table import table_ll1

from prettytable import PrettyTable

stack = ['EOF', 0]

def c_parser(lexer, file_path):
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
        if x == tok.type and x == 'EOF':
            if (not fail_input):
                print("The code was recognized successfully")
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
                # print("Compilation Failed")
                print(file_path + ":" + str(lexer.lineno) + ":" + find_column(file_path,tok) + " error: invalid suffix " + str(tok.value) + ", was expected '" + str(x) + "'")
                panic_mode = True
                fail_input = True
                if x == "EOF":
                    return
                stack.pop()
                x = stack[-1]
                # return 0;
            if x not in tokens: #non-terminal
                # print("Entering to the table")
                cell=find_rules(x,tok.type)
                # print("Cell = " + str(cell))
                if cell is None:
                    # print("Compilation Failed")
                    print(file_path + ":" + str(lexer.lineno) + ":" + find_column(file_path,tok) + " error: was not expected " + str(tok.type) + " in position " + find_column(file_path,tok))
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
                    add_to_stack(cell)
                    # print("Added stack = " + str(stack))
                    # print("------------")
                    x=stack[-1]            

def find_rules(non_terminal, terminal):
    for i in range(len(table_ll1)):
        if(table_ll1[i][0] == non_terminal and table_ll1[i][1] == terminal):
            return table_ll1[i][2]

def add_to_stack(production):
    for element in reversed(production):
        if element != 'empty': 
            stack.append(element)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return str((token.lexpos - line_start) + 1)

# def generate_symbols_table(tokens):
#     symbols_map = {}
#     i = 0

#     while i < len(token_array):
#         current_token = token_array[i]
        
#         if current_token['type'] == "INT":
#             i+=1
#             if i < len(token_array) and token_array[i]['type'] == "IDENTIFIER":
#                 i+=1
#                 if i < len(token_array) and
