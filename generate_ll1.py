# List of terminals and non-terminals
terminals = [
    "VOID", "INT", "CHAR", "FLOAT", "IF", "ELSE", "FUNCTION", "WHILE",
    "CONTINUE", "BREAK", "RETURN", "PREPROCESSOR", "MULT", "DIV", "ADD", "SUB",
    "AMPERSAND", "PIPE", "CIRCUMFLEX", "BITNOT", "LPAREN", "RPAREN", "LCURL",
    "RCURL", "SEMICOLON", "COMMA", "DOT", "ASSIGNMENT", "LANGLE", "RANGLE",
    "EQUALITY", "CONJUNCTION", "DISJUNCTION", "EXCLAMATION", "IDENTIFIER",
    "FLOAT_LITERAL", "INTEGER_LITERAL", "CHAR_LITERAL", "EOF"
]

len(terminals) # 39

non_terminals = [
    "S", "Type", "Values", "OperationAri", "OperationLogic", "Operationbit",
    "OperationbitNot", "Includes", "Globals", "GlobalsStartTypeId",
    "DeclarationsForm", "Declarator", "Function", "VoidFunction", "Params",
    "ParamMulti", "Expression", "InitialExpression", "MultpleExclamation",
    "ExpressionPrime", "BitsOperationExpression", "Statement",
    "StatementStartId", "StatementReturn", "Assignation", "CallFunction",
    "CallFunctionArg", "ArgumentsMulti", "While", "IfElse"
]

len(non_terminals) # 29 

# Generating the array for each non-terminal and terminal
arrays = []
for nt in non_terminals:
    for t in terminals:
        arrays.append([f"NT.{nt}.value", t, None])

result_strings = ["[NT." + nt + ".value, \"" + t + "\", None]," for nt in non_terminals for t in terminals]

sample_output = "\n".join(result_strings)  # Displaying the first 10 elements as a sample
print(sample_output)

