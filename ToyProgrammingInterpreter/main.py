from typing import Union, Dict
import sys

class Interpreter:
    variables: dict = {}
    env: Dict[str, Union[int, bool, str]] = {}
    lines: Dict[int, str] = {}
    current_line: int = 1
    #current_line = 0 
    
    # Partially Declarative
    @classmethod
    def evaluate_expression(cls, expr: str) -> Union[int, bool, str]:
        try:
            for variable in cls.env:
                expr = expr.replace(variable, str(cls.env[variable]))
            return eval(expr)
        except Exception as e:
            print(f"Error evaluating expression '{expr}': {e}")
            return None
        
    # Partially Declarative
    @classmethod
    def assign_variable(cls, statement: str):
        try:
            parts = statement.split("let", 1)
            rest = parts[1]
            parts = rest.split("=", 1)
            var_name = parts[0].strip()
            expr = parts[1].strip()
            value = cls.evaluate_expression(expr)
            if value is not None:
                cls.env[var_name] = value
                print(var_name + " assigned value " + str(value))
        except Exception as e:
            print("Error in assignment: " + str(e))
            
    # DONE - declarative         
    @classmethod
    def print_stmt(cls, statement: str):
        keyword = "print"
        expr = statement[len(keyword):].strip() if statement.startswith(keyword) else None
        value = cls.evaluate_expression(expr) if expr else None
        output = value if value is not None else f"Error evaluating expression: '{expr}'"
        print(output)

    # DONE - declarative 
    @classmethod
    def if_stmt(cls, statement: str):
        condition = statement[len("if"):].strip()
        result = cls.evaluate_expression(condition)
        cond = {
            True: "Condition is True",
            False: "Condition is False",
        }
        print(cond.get(result, f"Condition did not evaluate to True or False: {result}"))
                      
    # DONE - Partially         
    @classmethod
    def while_loop(cls, statement: str):
        match ":" in statement:
            case True:
                condition_part, body_part = statement.split(":", 1)
                condition = condition_part.replace("while", "", 1).strip()
                body = body_part.strip()
                while cls.evaluate_expression(condition):
                    cls.run_statement(body)
            case False:
                print("Missing ':' in while statement")

    # DONE - declarative
    @classmethod
    def goto(cls, statement: str):
        line_number = statement.split("goto")[1]
        target = int(line_number.strip())
        target = [cls.current_line if target in cls.lines else print(f"Line {target} does not exist.")]

    # DONE - declarative
    @classmethod
    def run_statement(cls, statement: str):
        match statement.strip().split()[0]: 
            case "let":
                cls.assign_variable(statement)
            case "print":
                cls.print_stmt(statement)
            case "if":
                cls.if_stmt(statement)
            case "while":
                cls.while_loop(statement)
            case "goto":
                cls.goto(statement)
            case _:
                print(f"Unknown statement: {statement}")
            
     # DONE - declarative      
    @classmethod
    def load_program(cls):
        print("Enter your program line by line. Type 'END' to finish.")
        line_number = 1
        finished = False
        while not finished:
            line = input(f"Line {line_number}: ").strip()
            if line.upper() == "END":
                finished = True
            else:
                cls.lines[line_number] = line
                line_number += 1
    
    @classmethod
    def execute_program(cls):
        statements = [(num, cls.lines[num]) for num in sorted(cls.lines)]
        [cls.run_statement(stmt) for _, stmt in statements]

    # No change - just Print        
    @classmethod
    def view_environment(cls):
        print("\nCurrent Environment:")
        for k, v in cls.env.items():
            print(f"{k} = {v}")
    
    # DONE - declarative
    @classmethod
    def main_menu(cls):
        menu_actions = {
            '1': lambda: cls.load_program(),
            '2': lambda: cls.execute_program(),
            '3': lambda: cls.view_environment(),
            '4': lambda: sys.exit()
        }

        while True:
            print("\nToy Language Interpreter")
            print("1. Load program")
            print("2. Run program")
            print("3. View environment")
            print("4. Exit")
            choice = input("Select an option: ")
            action = menu_actions.get(choice)
            if action:
                action()
            else:
                print("Invalid option. Please select 1-4.")

if __name__ == "__main__":
    Interpreter.main_menu()
