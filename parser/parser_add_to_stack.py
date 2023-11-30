def add_to_stack(stack, production):
    for element in reversed(production):
        if element != 'empty': 
            stack.append(element)