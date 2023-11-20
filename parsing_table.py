from non_terminals import NT

table_ll1 = [[NT.S.value, 'IDENTIFIER', None ],
         [NT.S.value, 'INT', [NT.TT.value,'IDENTIFIER',NT.D.value] ],
         [NT.S.value, 'FLOAT', [NT.TT.value,'IDENTIFIER',NT.D.value] ],
         [NT.S.value, 'COMMA', None],
         [NT.S.value, 'SEMICOLON', None],
         [NT.TT.value, 'IDENTIFIER', None ],
         [NT.TT.value, 'INT', ['INT'] ],
         [NT.TT.value, 'FLOAT', ['FLOAT'] ],
         [NT.TT.value, 'COMMA', None],
         [NT.TT.value, 'SEMICOLON', None],
         [NT.D.value, 'IDENTIFIER', None ],
         [NT.D.value, 'INT', None ],
         [NT.D.value, 'FLOAT', None ],
         [NT.D.value, 'COMMA', ['COMMA','IDENTIFIER',NT.D.value]],
         [NT.D.value, 'SEMICOLON', ['SEMICOLON']],
         ]
 
