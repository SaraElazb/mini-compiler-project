import re

token_specification = [
    ('NUMBER',   r'\d+'),                          
    ('ID',       r'[a-zA-Z_][a-zA-Z0-9_]*'),       
    ('ASSIGN',   r'='),                            
    ('END',      r';'),                            
    ('OP',       r'[+\-*/]'),                      
    ('LPAREN',   r'\('),                          
    ('RPAREN',   r'\)'),                          
    ('LBRACE',   r'\{'),                          
    ('RBRACE',   r'\}'),                           
    ('COMPARISON', r'[<>]=?|==|!='),               
    ('KEYWORD',  r'\bint\b|\bfloat\b|\bstring\b|\bchar\b|\bbool\b|\bif\b|\belse\b|\bwhile\b'), 
    ('WHITESPACE', r'[ \t]+'),                    
    ('NEWLINE',  r'\n'),                           
    ('MISMATCH', r'.'),                            
]


token_re = re.compile('|'.join('(?P<%s>%s)' % pair for pair in token_specification))

def tokenize(code):
    line_num = 1
    line_start = 0
    tokens = []
    for mo in re.finditer(token_re, code):
        kind = mo.lastgroup
        value = mo.group(kind)
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = int(value)
        elif kind == 'ID' and value in ['int', 'float', 'if', 'else', 'while']:
            kind = 'KEYWORD'
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        tokens.append((kind, value, line_num, column))
    return tokens

with open(r'C:\\Users\workstation\Desktop\\Compilers Project\\code.txt', 'r') as f:
    code = f.read()


tokens = tokenize(code)
for token in tokens:
    print(token)