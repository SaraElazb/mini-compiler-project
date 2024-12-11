import re

TOKENS = {
    "data-type": r"\b(?:int|float|double|string|char|bool)\b",
    "keyword": r"\bvoid\b",
    "identifier": r"\b[a-zA-Z_][a-zA-Z0-9_]*\b",
    "number": r"\b\d+(\.\d+)?\b",
    "comparisonOperator": r"[<>]=?|==|!=",
    "assignmentOperator": r"=",
    "arithmeticOperator": r"[\+\-\*/]",
    "logicalOperator": r"\b(and|or|&&|\|\|)\b",
    "delimiter": r"[;,\(\)\{\}]",
}

def tokenize(code):
    tokens = []
    position = 0  

    while position < len(code):
        match_found = False  
        for token_type, pattern in TOKENS.items():
            regex = re.compile(pattern)
            match = regex.match(code, position)  

            if match:
                tokens.append((token_type, match.group()))
                position = match.end()  
                match_found = True
                break  
            
        if not match_found:
            
            position += 1

    return tokens
