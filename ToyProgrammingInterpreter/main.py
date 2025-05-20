from typing import Union, Dict

class Interpreter:
    env: Dict[str, Union[int, bool, str]] = {}
    lines: Dict[int, str] = {}
    current_line: int = 1

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

    @classmethod
    def print_stmt(cls, statement: str):
        try:
            expr = statement.split("print", 1)[1].strip()
            value = cls.evaluate_expression(expr)
            print(value)
        except Exception as e:
            print("Error in print statement:", e)

    @classmethod
    def if_stmt(cls, statement: str):
        condition = statement[2:].strip()
        result = cls.evaluate_expression(condition)

        if result is True:
            print("Condition is True")
        elif result is False:
            print("Condition is False")
        else:
            print(f"Condition did not evaluate to True or False: {result}")

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
        line_number = statement.split("goto")
        target = int(line_number.strip())
        if target in cls.lines:
            cls.current_line = target
        else:
            print(f"Line {target} does not exist.")

    @classmethod
    def run_statement(cls, statement: str):
        if statement.startswith("let"):
            cls.assign_variable(statement)
        elif statement.startswith("print"):
            cls.print_stmt(statement)
        elif statement.startswith("if"):
            cls.if_stmt(statement)
        elif statement.startswith("while"):
            cls.while_loop(statement)
        elif statement.startswith("goto"):
            cls.goto(statement)
        else:
            print(f"Unknown statement: {statement}")

    @classmethod
    def load_program(cls):
        print("Enter your program line by line. Type 'END' to finish.")
        line_number = 1
        while True:
            line = input(f"Line {line_number}: ")
            if line.strip().upper() == "END":
                break
            cls.lines[line_number] = line
            line_number += 1

    @classmethod
    def run_program(cls):
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

    @classmethod
    def main_menu(cls):
        while True:
            print("\nToy Language Interpreter")
            print("1. Load program")
            print("2. Run program")
            print("3. View environment")
            print("4. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                cls.load_program()
            elif choice == '2':
                cls.run_program()
            elif choice == '3':
                cls.view_environment()
            elif choice == '4':
                break
            else:
                print("Invalid option. Please select 1-4.")

if __name__ == "__main__":
    Interpreter.main_menu()
