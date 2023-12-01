from tokens import tokens
from non_terminals import NT

assign = False
current_key = ""
current_id = 0
non_terminals_symbols_table = {
}

symbols_table = {
}

def generate_symbols_table(token, lexer, current_stack):
    global assign
    global current_key
    global current_id
    global non_terminals_symbols_table

    if current_stack == NT.Globals.value:
        current_id+=1
        non_terminals_symbols_table[current_id] = {
            "id": current_id,
            "start": current_stack,
            "type": token.type,
            "line_number": lexer.lineno,
            "position": lexer.column,
            "level": lexer.level,
        }
    if current_id in non_terminals_symbols_table:
        if non_terminals_symbols_table[current_id]["start"] == NT.Globals.value and current_stack in tokens and current_stack == token.type:
            if token.type == "IDENTIFIER" and not assign:
                key = str(str(token.value)+str(lexer.level))
                current_key = key
                symbols_table[key] = {
                    "id": key,
                    "state": False,
                    "type": non_terminals_symbols_table[current_id]["type"],
                    "body": [],
                    "line_number": lexer.lineno,
                    "position": lexer.column - len(token.value),
                    "level": lexer.level,
                }
            if current_key in symbols_table:
                if token.type == "ASSIGNMENT":
                    symbols_table[current_key]["state"] = True
                    assign = True
                elif token.type == "COMMA" or token.type == "SEMICOLON":
                    symbols_table[current_key]["state"] = False
                    assign = False
                elif symbols_table[current_key]["state"]:
                    symbols_table[current_key]["body"].append(token.value)

    return symbols_table
    