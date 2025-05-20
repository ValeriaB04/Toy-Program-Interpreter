from typing import Union, Dict

class Interpreter:
    def __init__(self):
        self.env: Dict[str, Union[int, bool, str]] = {}
        self.program_lines = {}
        self.current_line = 1

    def evaluate_expression(self, expr: str) -> Union[int, bool, str]:
        try:
            for variable in self.env:
                expr = expr.replace(variable, str(self.env[variable]))
            return eval(expr)
        except Exception as e:
            print(f"Error evaluating expression '{expr}': {e}")
            return None

    def assign_variable(self, statement: str):
        try:
            parts = statement.split("let", 1)
            rest = parts[1]  
            parts = rest.split("=", 1)
            var_name = parts[0].strip()
            expr = parts[1].strip()
            value = self.evaluate_expression(expr)
            if value is not None:
                self.env[var_name] = value
                print(var_name + " assigned value " + str(value))
        except Exception as e:
            print("Error in assignment: " + str(e))


    def print_stmt(self, statement: str):
        try:
            expr = statement.split("print", 1)[1].strip()
            value = self.evaluate_expression(expr)
            print(value)
        except Exception as e:
            print("Error in print statement:", e)

    def if_stmt(self, statement: str):
        condition = statement[2:].strip()
        result = self.evaluate_expression(condition)
        
        if result is True:
            print("Condition is True")
        elif result is False:
            print("Condition is False")
        else:
            print(f"Condition did not evaluate to True or False: {result}")

    def while_loop(self, statement: str):
        try:
            parts = statement.split(":", 1)
            condition_part = parts[0]
            cond = parts[1]
            condition = condition_part.replace("while", "", 1).strip()
            while self.evaluate_expression(condition):
                self.run_statement(cond.strip())
        except Exception as e:
            print("Error in while loop: " + str(e))


    def goto(self, statement: str):
        _, line_number = statement.split("goto")
        target = int(line_number.strip())
        if target in self.program_lines:
            self.current_line = target
        else:
            print(f"Line {target} does not exist.")

    def run_statement(self, statement: str):
        if statement.startswith("let"):
            self.assign_variable(statement)
        elif statement.startswith("print"):
            self.print_stmt(statement)
        elif statement.startswith("if"):
            self.if_stmt(statement)
        elif statement.startswith("while"):
            self.while_loop(statement)
        elif statement.startswith("goto"):
            self.goto(statement)
        else:
            print(f"Unknown statement: {statement}")

    def load_program(self):
        print("Enter your program line by line. Type 'END' to finish.")
        line_number = 1
        while True:
            line = input(f"Line {line_number}: ")
            if line.strip().upper() == "END":
                break
            self.program_lines[line_number] = line
            line_number += 1

    def run_program(self):
        self.current_line = 1
        while self.current_line in self.program_lines:
            statement = self.program_lines[self.current_line]
            self.run_statement(statement)
            self.current_line += 1

    def view_environment(self):
        print("\nCurrent Environment:")
        for k, v in self.env.items():
            print(f"{k} = {v}")

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
                self.run_program()
            elif choice == '3':
                self.view_environment()
            elif choice == '4':
                break
            else:
                print("Invalid option. Please select 1-4.")

if __name__ == "__main__":
    interpreter = Interpreter()
    interpreter.main_menu()
