from typing import Union, Dict
class Interpreter: 
    def __init__(self):
        self.env: Dict[str, Union[int, bool, str]] = {}
        self.lines = []
        self.current_line = 1
    
    def evaluate_expression(self,expr: str) -> Union[int, bool, str]:
      try:
          for variable in self.env: 
              expr = expr.replace(variable, str(self.env[var]))
            return eval(expr)
      except Exception as e: 
        print(f"Error evaluating expression '{expr}': {e}")
        return 
          
    def assign_variable(self,key,value):
        self.variables[key] = value
        print(self.variables)

    def print_stmt(self, statement: str):
        expr = statement.split("print", 1)
        value = self.evaluate_expression(expr)
        print(value) 

    def while_loop(self, statement:str):
        return null 

    def goto(self, statement:str):
        line_number = statement.split("goto")
        target = int(line_number)
        if target in self.lines:
            self.current_line = target 
        else: 
            print(f"Line {target} does not exist.")

    def run_statement(self, statement: str):
        return null

    def load_program(self):
        return null
            
    def execute_program(self):
        return null 

    def display_environment(self):
        print("\nCurrent Environment:")
        for z, v in self.env.items():
            print(f"{z} = {v}")

    def main_menu(self):
        while True:
            print("\nToy Language Interpreter")
            print("1. Load program")
            print("2. Run program")
            print("3. View environment")
            print("4. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                self.load_program()
            elif choice == '2':
                self.execute_program()
            elif choice == '3':
                self.display_environment()
            elif choice == '4':
                break
            else:
                print("Invalid option. Please select 1-4.")

if __name__ == "__main__":
    interpreter = Interpreter()
    interpreter.main_menu()
