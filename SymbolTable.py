import re


class SymbolTable:
    def __init__(self):
        self.table = []
        self.current_address = 0
        self.counter = 0

    def generate_table(self, code):
        self.table = [] 
        line_number = 1  
        
        for line in code.splitlines():
            
            match = re.match(r"^\s*(?P<data_type>\w+)\s+(?P<variable_name>\w+)\s*=\s*(?P<value>.+);$", line)
            if match:
                data_type = match.group("data_type")
                variable_name = match.group("variable_name")
                
                self.table.append({
                    "Counter": self.counter,
                    "Variable Name": variable_name,
                    "Address": self.current_address,
                    "Data Type": data_type,
                    "No. of Dimensions": 0, 
                    "Line Declaration": line_number,
                    "Reference Line": set(),  
                })

                self.counter += 1
                if data_type == "char":
                    self.current_address += 1
                elif data_type == "int":
                    self.current_address += 2  
                elif data_type == "float":
                    self.current_address += 4
                elif data_type == "double":
                    self.current_address += 8
                
            for variable in re.findall(r"\b\w+\b", line):
                for entry in self.table:
                    if entry["Variable Name"] == variable:
                        
                        if line_number != entry["Line Declaration"]:
                            entry["Reference Line"].add(line_number)
                        break

            line_number += 1

    def get_table_data(self):
        
        formatted_table = []
        for entry in self.table:
            formatted_table.append([
                entry["Counter"],
                entry["Variable Name"],
                entry["Address"],
                entry["Data Type"],
                entry["No. of Dimensions"],
                entry["Line Declaration"],
                ", ".join(map(str, entry["Reference Line"])),   
            ])
            
        return formatted_table
