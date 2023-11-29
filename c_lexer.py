import ply.lex as lex

from prettytable import PrettyTable

from keywords import keywords
from tokens import tokens
from tokens import sync_tokens
from parsing_table import table_ll1
# import parsing_table 

# Arithmetic Operators
t_MULT = r"\*"
t_DIV = r"/"
t_ADD = r"\+"
t_SUB = r"-"

# Parentheses
t_LPAREN = r"\("
t_RPAREN = r"\)"

# Braces
def t_LCURL(t):
    r"\{"
    t.lexer.level += 1
    return t

def t_RCURL(t):
    r"\}"
    t.lexer.level -= 1
    return t

# Punctuation
t_SEMICOLON = r"\;"
t_COMMA = r"\,"

# Assignment Operator
t_ASSIGNMENT = r"="

# Comparison Operators
t_LANGLE = r"\<"
t_RANGLE = r"\>"
t_EQUALITY = r"=="

# Logical Operators
t_CONJUNCTION = r"&&"
t_DISJUNCTION = r"\|\|"
t_EXCLAMATION = r"\!"

# Literals
def t_FLOAT_LITERAL(t):
    r"-\d+\.\d+ | \d+\.\d+"
    t.value = float(t.value)
    return t

def t_INTEGER_LITERAL(t):
    r"-\d+ | \d+"
    t.value = int(t.value)
    return t

def t_CHAR_LITERAL(t):
    r"\'[a-zA-Z0-9]\'"
    t.value = str(t.value)
    return t

# Identifiers
def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = keywords.get(t.value, "IDENTIFIER")
    return t

# Comments
def t_LINE_COMMENT(t):
    r"\/\/.*"
    pass

def t_DELIMITED_COMMENT(t):
    r"\/\*(.|\n)*\*\/"
    pass

# Newline
def t_NEWLINE(t):
    r"\r?\n"
    t.lexer.lineno += len(t.value)

# Whitespace
t_ignore = " \t"

# End of line
t_EOF= r'\$'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
lexer.level = 0
lexer_tokens = []


stack = ['EOF', 0]

# for tok in lexer:
#     ply_table.add_row([tok.type, tok.value, tok.lineno, tok.lexpos, lexer.level])

def parser():
    file_path = "main.c"
    file = open(file_path, "r")
    lexer.input(file.read() + "$")
    tok=lexer.token()
    panic_mode = False 
    fail_input = False
    x=stack[-1]

    while True:
        if panic_mode and tok.type not in sync_tokens:
            tok=lexer.token()
            continue
        else: 
            panic_mode = False
        
        # print("tok.type = " + tok.type)
        # print("x = " + str(x))
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
                print("Compilation Failed")
                print(file_path + ":" + str(lexer.lineno) + ":" + find_column(file_path,tok) + " error: invalid suffix " + str(tok.value) + ", was expected '" + str(x) + "'")
                # return 0;
            if x not in tokens: #non-terminal
                # print("Entering to the table")
                cell=find_rules(x,tok.type)
                # print("Cell = " + str(cell))
                if  cell is None:
                    print("Compilation Failed")
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

parser()
