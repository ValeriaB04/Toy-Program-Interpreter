from typing import Union, Dict
import sys

class Interpreter:
    variables: dict = {}
    env: Dict[str, Union[int, bool, str]] = {}
    lines: Dict[int, str] = {}
    current_line: int = 1
    #current_line = 0 

    @classmethod
    def evaluate_expression(cls, expr: str) -> Union[int, bool, str]:
        try:
            for variable in cls.env:
                expr = expr.replace(variable, str(cls.env[variable]))
            return eval(expr)
        except Exception as e:
            print(f"Error evaluating expression '{expr}': {e}")
            return None

    @classmethod
    def assign_variable1(cls, statement: str):
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
            
    # ? not sure if its ideal - input:
    # let x = 0 
    # while x < 5: let x = x + 1         
    @classmethod
    def while_loop(cls, statement: str):
        try:
            parts = statement.split(":", 1)
            condition_part = parts[0]
            cond = parts[1]
            condition = condition_part.replace("while", "", 1).strip()
            while cls.evaluate_expression(condition):
                cls.run_statement(cond.strip())
        except Exception as e:
            print("Error in while loop: " + str(e))

    @classmethod
    def goto(cls, statement: str):
        line_number = statement.split("goto")[1]
        target = int(line_number.strip())
        if target in cls.lines:
            cls.current_line = target
        else:
            print(f"Line {target} does not exist.")
            
    @classmethod
    def goto1(cls, statement: str):
        keyword = "goto"
        if statement.startswith(keyword):
            target_str = statement[len(keyword):].strip()
            target = int(target_str)
            
            if target in cls.lines:
                cls.current_line = target
            else:
                print(f"Line {target} does not exist.")

    # DONE - declarative
    @classmethod
    def run_statement(cls, statement: str):
        commands = {
            "let": cls.assign_variable,
            "print": cls.print_stmt,
            "if": cls.if_stmt,
            "while": cls.while_loop,
            "goto": cls.goto
        }
    
        matched = False
        for keyword, function_to_call in commands.items():
            if statement.strip().startswith(keyword):
                function_to_call(statement)
                matched = True
                break
   
        if not matched:
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
        cls.current_line = 1
        while cls.current_line in cls.lines:
            statement = cls.lines[cls.current_line]
            cls.run_statement(statement)
            cls.current_line += 1
            
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
