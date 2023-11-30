from keywords import keywords

tokens = [
    # Arithmetic Operators
    "MULT",  # Multiplication *
    "DIV",  # Division /
    "ADD",  # Addition +
    "SUB",  # Subtraction -
    # Parentheses
    "LPAREN",  # Left parenthesis (
    "RPAREN",  # Right parenthesis )
    # Braces
    "LCURL",  # Left curly brace {
    "RCURL",  # Right curly brace }
    # Punctuation
    "SEMICOLON",  # Semicolon ;
    "COMMA",  # Comma ,
    # Assignment Operator
    "ASSIGNMENT",  # Assignment =
    # Comparison Operators
    "LANGLE",  # Less than <
    "RANGLE",  # Greater than >
    "EQUALITY",  # Equality ==
    # Logical Operators
    "CONJUNCTION",  # Conjunction &&
    "DISJUNCTION",  # Disjunction ||
    "EXCLAMATION",  # Exclamation mark !
    # Identifiers
    "IDENTIFIER",  # Identifier (e.g. main)
    # Literals
    "FLOAT_LITERAL",  # Float (e.g. 1.0)
    "INTEGER_LITERAL",  # Integer (e.g. 1)
    "CHAR_LITERAL",  # Boolean (e.g. true)
    # Helpers
    "EOF",
    "IGNORE"
    # Keywords
] + list(keywords.values())

sync_tokens = [
    "LCURL",  # Left curly brace {
    "RCURL",  # Right curly brace }
    "SEMICOLON",  # Semicolon ;
    "COMMA",
]
