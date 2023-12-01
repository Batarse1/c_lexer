from prettytable import PrettyTable

def print_table(table, field_names):
    prettyTable = PrettyTable()
    prettyTable.field_names = field_names
    for key, element in table.items():
        elements = []
        
        for name, item in element.items():
            if name == "id":
                elements.append(item[:-1])
            elif name == "body":
                if len(item) > 0:
                    elements.append(' '.join(str(elem) for elem in item))
                else:
                    elements.append("Undefined")
            elif name != "state":
                elements.append(item)

        prettyTable.add_row(elements)
    
    print(prettyTable)
    
