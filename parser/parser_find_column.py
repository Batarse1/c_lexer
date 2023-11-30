def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return str((token.lexpos - line_start) + 1)