import ply.lex as lex

from tokens import tokens
from keywords import keywords

def c_lexer():
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

    return lexer