import re

class HashTable:
    def __init__(self, hash_max):
        self.hash_max = hash_max
        self.table = {}
        self.data_types = {"int", "float", "double", "string", "char", "bool"}  

    def calculate_hash(self, identifier):
        identifier_length = len(identifier)
        first_char_ascii = ord(identifier[0])
        hash_value = (identifier_length + first_char_ascii) % self.hash_max
        return hash_value

    def process_code(self, code):
        self.table = {}
        processed_identifiers = set()  
        for line in code.splitlines():
            line = line.strip()
            if not line:
                continue

            identifiers = self.extract_identifiers(line)
            for identifier in identifiers:
                if identifier not in self.data_types and identifier not in processed_identifiers:
                    hash_value = self.calculate_hash(identifier)
                    processed_identifiers.add(identifier)  
                    
                    if hash_value in self.table:
                        if identifier not in self.table[hash_value]:
                            self.table[hash_value].append(identifier)  
                    else:
                        self.table[hash_value] = [identifier]
        
        self.print_hash_table()  

    def extract_identifiers(self, line):
        identifiers = []
        declaration_match = re.match(r"^(int|float|double|string|char|bool)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*;", line)
        if declaration_match:
            identifiers.append(declaration_match.group(2))

        assignment_match = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*)\s*=", line)
        if assignment_match:
            identifiers.append(assignment_match.group(1))

        expression_identifiers = re.findall(r"\b([a-zA-Z_][a-zA-Z0-9_]*)\b", line)
        identifiers.extend(expression_identifiers)

        return identifiers

    def get_table_data(self):
        return self.table

    def print_hash_table(self):
        print(f"{'Hash Value'}{'Identifiers'}")
        for hash_value in sorted(self.table.keys()):
            identifiers = " ".join(self.table[hash_value])
            print(f"{hash_value}{identifiers}")
