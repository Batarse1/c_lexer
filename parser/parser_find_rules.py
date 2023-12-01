def find_rules(table, non_terminal, terminal):
    for i in range(len(table)):
        if(table[i][0] == non_terminal and table[i][1] == terminal):
            return table[i][2]