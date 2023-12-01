from tokens import tokens
from non_terminals import NT

condition = False
assign = False
current_key = ""
current_id = 0
type_table = {
}

symbols_table = {
}

def generate_symbols_table(token, lexer, current_stack):
    global assign, condition, current_key, current_id, type_table

    if (current_stack == NT.Globals.value or current_stack == NT.Statement.value) and token.type != "IDENTIFIER":
        current_id+=1
        type_table[current_id] = {
            "id": current_id,
            "start": current_stack,
            "type": token.type,
            "line_number": lexer.lineno,
            "position": lexer.column,
            "level": lexer.level,
        }
    if current_id in type_table:
        if (type_table[current_id]["start"] == NT.Globals.value or type_table[current_id]["start"] == NT.Statement.value) and current_stack in tokens and current_stack == token.type:
            if token.type == "IDENTIFIER" and not assign and not condition:
                key = str(str(token.value)+str(lexer.level))
                current_key = key
                symbols_table[key] = {
                    "id": key,
                    "state": False,
                    "type": type_table[current_id]["type"],
                    "body": [],
                    "line_number": lexer.lineno,
                    "position": lexer.column - len(token.value),
                    "level": lexer.level,
                }
            if current_key in symbols_table:
                if token.type == "LPAREN":
                    condition = True
                elif token.type == "RPAREN":
                    condition = False
                elif token.type == "ASSIGNMENT":
                    symbols_table[current_key]["state"] = True
                    assign = True
                elif token.type == "COMMA" or token.type == "SEMICOLON":
                    symbols_table[current_key]["state"] = False
                    assign = False
                elif symbols_table[current_key]["state"]:
                    symbols_table[current_key]["body"].append(token.value)

    return symbols_table
    