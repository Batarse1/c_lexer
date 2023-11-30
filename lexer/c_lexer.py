import ply.lex as lex

from tokens import tokens
from keywords import keywords

def c_lexer():
    # Arithmetic Operators
    def t_MULT(t):
        r"\*"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        return t
    def t_DIV(t):
        r"/"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        return t
    def t_ADD(t):
        r"\+"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        return t
    def t_SUB(t):
        r"-"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        return t

    # Parentheses
    def t_LPAREN(t):
        r"\("
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        return t
    def t_RPAREN(t):
        r"\)"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        return t

    # Braces
    def t_LCURL(t):
        r"\{"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        t.lexer.level += 1
        return t

    def t_RCURL(t):
        r"\}"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        t.lexer.level -= 1
        return t

    # Punctuation
    def t_SEMICOLON(t):
        r"\;"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        return t
    def t_COMMA(t):
        r"\,"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        return t

    # Assignment Operator
    def t_ASSIGNMENT(t):
        r"="
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        return t

    # Comparison Operators
    def t_LANGLE(t):
        r"\<"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        return t
    def t_RANGLE(t):
        r"\>"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        return t
    def t_EQUALITY(t):
        r"=="
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        return t

    # Logical Operators
    def t_CONJUNCTION(t):
        r"&&"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        return t
    def t_DISJUNCTION(t):
        r"\|\|"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        return t
    def t_EXCLAMATION(t):
        r"\!"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        return t

    # Literals
    def t_FLOAT_LITERAL(t):
        r"-\d+\.\d+ | \d+\.\d+"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        t.value = float(t.value)
        return t

    def t_INTEGER_LITERAL(t):
        r"-\d+ | \d+"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        t.value = int(t.value)
        return t

    def t_CHAR_LITERAL(t):
        r"\'[a-zA-Z0-9]\'"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        t.value = str(t.value)
        return t

    # Identifiers
    def t_IDENTIFIER(t):
        r"[a-zA-Z_][a-zA-Z0-9_]*"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        t.type = keywords.get(t.value, "IDENTIFIER")
        return t

    # Comments
    def t_LINE_COMMENT(t):
        r"\/\/.*"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        pass

    def t_DELIMITED_COMMENT(t):
        r"\/\*(.|\n)*\*\/"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        pass

    # Newline
    def t_NEWLINE(t):
        r"\r?\n"
        t.lexer.column = 0 # Reset column count, since we're on a new line. lexer.column = 0
        t.lexer.lineno += len(t.value)

    # Whitespace
    def t_IGNORE(t):
        r"\s+"
        t.column = t.lexer.column
        t.lexer.column += len(t.value)
        pass

    # End of line
    t_EOF= r'\$'

    # Error handling rule
    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    lexer = lex.lex()
    lexer.level = 0
    lexer.column = 0

    return lexer