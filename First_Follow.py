from collections import defaultdict

class Grammar:
    def __init__(self, rules):
        self.rules = rules
        self.first = defaultdict(set)
        self.follow = defaultdict(set)
        
    def compute_first(self):
        def first_of(symbol):
            if symbol not in self.rules:  
                return {symbol}
            if symbol in self.first: 
                return self.first[symbol]
            first_set = set()
            for production in self.rules[symbol]:
                for token in production:
                    token_first = first_of(token)
                    first_set.update(token_first - {"ε"})
                    if "ε" not in token_first:
                        break
                else:  
                    first_set.add("ε")
            self.first[symbol] = first_set
            return first_set

        for non_terminal in self.rules:
            
            first_of(non_terminal)

    def compute_follow(self):
        self.follow["program"].add("$")  
        while True:
            updated = False
            for non_terminal, productions in self.rules.items():
                for production in productions:
                    follow_temp = set(self.follow[non_terminal])
                    for i in reversed(range(len(production))):
                        token = production[i]
                        if token in self.rules:  
                            if follow_temp - self.follow[token]:
                                self.follow[token].update(follow_temp)
                                updated = True
                            if "ε" in self.first[production[i]]:
                                follow_temp.update(self.first[production[i]] - {"ε"})
                            else:
                                follow_temp = self.first[production[i]]
                        else:  
                            follow_temp = {token}
            if not updated:
                break
GRAMMAR = {
    "E": ["TA"],
    "A": ["+TA", "ε"],
    "T": ["FB"],
    "B": ["*FB", "ε"],
    "F":[["id"] , "(E)"]
}
GRAMMAR2 = {
    "program": [["expression"]],
    "expression": [["term", "+", "expression"], [ "term", "-", "expression"], [ "term"]],
    "term": [["factor", "*", "factor"], [ "factor", "/", "factor"] ,["factor"]],
    "factor": [["number"], [ "(", "expression", ")"]],
    "number": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}
GRAMMAR3 = {
    "program": [["statement"]],
    "statement": [["variable","=","expression"]],
    "expression": [[ "term", "-", "term"], [ "term", "+", "term"]],
    "term": [["variable"]],
    "variable": ["a" , "b" , "c", "d"],
}
grammar = Grammar(GRAMMAR3)
grammar.compute_first()
grammar.compute_follow()

print("FIRST sets:")
for non_terminal, first_set in grammar.first.items():
    print(f"{non_terminal}: {first_set}")

print("\nFOLLOW sets:")
for non_terminal, follow_set in grammar.follow.items():
    print(f"{non_terminal}: {follow_set}")