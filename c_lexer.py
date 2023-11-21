import ply.lex as lex

from prettytable import PrettyTable

from keywords import keywords
from tokens import tokens
from parsing_table import table_ll1

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

ply_table = PrettyTable()
ply_table.field_names = ["Type", "Value", "Line Number", "Position", "level"]
stack = [0,'EOF']

# for tok in lexer:
#     ply_table.add_row([tok.type, tok.value, tok.lineno, tok.lexpos, lexer.level])

def parser():
    file = open("minimal_example.c", "r")
    lexer.input(file.read() + "$")
    tok=lexer.token()
    x=stack[0]

    while True:
        print("tok.type = " + tok.type)
        print("x = " + str(x))
        if x == tok.type and x == 'EOF':
            print("The code was recognized successfully")
            print("\nLexemas Table")
            print(ply_table)
            return
        else:
            if x == tok.type and x != 'EOF': #terminal
                print("Current stack = " + str(stack))
                stack.pop(0)
                print("Poped stack = " + str(stack))
                x=stack[0]
                print("------------")
                ply_table.add_row([tok.type, tok.value, tok.lineno, tok.lexpos, lexer.level])
                tok=lexer.token()                
                continue
            if x in tokens and x != tok.type:
                print("Error: " + str(tok.type) + " was expected instead of " + str(x))
                return 0;
            if x not in tokens: #non-terminal
                print("Entering to the table")
                cell=find_rules(x,tok.type)
                print("Cell = " + str(cell))
                if  cell is None:
                    print("Error: " + str(tok.type) + " was not expected")
                    print("In position:", tok.lexpos)
                    return 0;
                else:
                    print("Current stack = " + str(stack))
                    stack.pop(0)
                    print("Poped stack = " + str(stack))
                    add_to_stack(cell)
                    print("Added stack = " + str(stack))
                    print("------------")
                    x=stack[0]            

def find_rules(non_terminal, terminal):
    for i in range(len(table_ll1)):
        if(table_ll1[i][0] == non_terminal and table_ll1[i][1] == terminal):
            return table_ll1[i][2]

def add_to_stack(production):
    for element in reversed(production):
        if element != 'empty': 
            stack.insert(0,element)

parser()
# This is only for the executable file
input("Press anything to exit.")
