from tokens import tokens
from non_terminals import NT

symbols_table_id = 0
current_id = 0
non_terminals_symbols_table = {
}

symbols_table = {
}

def generate_symbols_table(token, lexer, current_stack):
    global current_id
    global non_terminals_symbols_table

    print("current_id")
    print(current_id)
    print(token)

    if current_stack == NT.D.value:
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
        if non_terminals_symbols_table[current_id]["start"] == NT.D.value and current_stack in tokens and current_stack == token.type:
            if token.type == "IDENTIFIER":
                symbols_table[token.value] = {
                    "id": symbols_table_id,
                    "state": False,
                    "type": non_terminals_symbols_table[current_id]["type"],
                    "body": [],
                    "line_number": lexer.lineno,
                    "position": lexer.column - len(token.value),
                    "level": lexer.level,
                }
            else:
                print(symbols_table)

    return non_terminals_symbols_table
    