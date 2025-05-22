from typing import Dict, Union, Optional
import sys

class Interpreter:
    """A simple interpreter for a toy programming language."""
    # The interpreter uses a dictionary to represent the environment, where variable names are keys
    # and their values can be integers, booleans, or strings.
    # The interpreter also uses a dictionary to represent the lines of code, where line numbers are keys
    Env = Dict[str, Union[int, bool, str]]
    Lines = Dict[int, str]

     # evaluate_expression(expr: str, env: Env) -> Optional[Union[int, bool, str]]:
    #     Evaluates an expression using the given environment.
    @staticmethod
    def evaluate_expression(expr: str, env: Env) -> Optional[Union[int, bool, str]]:
        """Purely evaluates an expression using the given environment."""
        try:
            for variable in env:
                expr = expr.replace(variable, str(env[variable]))
            return eval(expr)
        except Exception as e:
            print(f"Error evaluating expression '{expr}': {e}")
            return None
        
    # assign_variable(statement: str, env: Env) -> Env:
    #     Parses and executes a variable assignment statement, returning an updated environment.
    @staticmethod
    def assign_variable(statement: str, env: Env) -> Env:
        try:
            parts = statement.split("let", 1)
            rest = parts[1]
            parts = rest.split("=", 1)
            var_name = parts[0].strip()
            expr = parts[1].strip()
            value = Interpreter.evaluate_expression(expr, env)
            if value is not None:
                # Create a new env dict with updated variable assignment (immutable update)
                new_env = {**env, var_name: value}
                print(var_name + " assigned value " + str(value))
                return new_env
            else:
                return env
        except Exception as e:
            print("Error in assignment: " + str(e))
            return env
        
    # print_stmt(statement: str, env: Env) -> None:
    #     Handles and evaluates a print statement, outputting the result.
    @staticmethod
    def print_stmt(statement: str, env: Env) -> None:
        """Handles the print statement."""
        keyword = "print"
        expr = statement[len(keyword):].strip() if statement.startswith(keyword) else None
        value = Interpreter.evaluate_expression(expr, env) if expr else None
        output = value if value is not None else f"Error evaluating expression: '{expr}'"
        print(output)

    # if_stmt(statement: str, env: Env) -> None:
    #     Evaluates an if statement and prints the result of the condition.
    @staticmethod
    def if_stmt(statement: str, env: Env) -> None:
        condition = statement[len("if"):].strip()
        result = Interpreter.evaluate_expression(condition, env)
        cond = {
            True: "Condition is True",
            False: "Condition is False",
        }
        print(cond.get(result, f"Condition did not evaluate to True or False: {result}"))

    # while_loop(statement: str, env: Env, lines: Lines) -> Env:
    #     Executes a while loop statement, repeatedly running the body while the condition is true.
    @staticmethod
    def while_loop(statement: str, env: Env, lines: Lines) -> Env:
        """Handles the while loop statement and returns updated environment."""
        if ":" not in statement:
            print("Missing ':' in while statement.")
            return env

        condition_part, body_part = statement.split(":", 1)
        condition = condition_part.replace("while", "", 1).strip()
        body = body_part.strip()
        
        current_env = env
        while Interpreter.evaluate_expression(condition, current_env):
            current_env = Interpreter.run_statement(body, current_env, lines)
        return current_env
    
    # goto(statement: str, lines: Lines) -> Optional[int]:
    #     Handles a goto statement, returning the target line number if valid.
    @staticmethod
    def goto(statement: str, lines: Lines) -> Optional[int]:
        """Handles the goto statement."""
        try:
            target = int(statement.split("goto")[1].strip())
            if target in lines:
                print(f"Jumping to line {target}")
                return target
            else:
                print(f"Line {target} does not exist.")
                return None
        except Exception as e:
            print(f"Error in goto: {e}")
            return None
        
    # run_statement(statement: str, env: Env, lines: Lines) -> Env:
    #     Executes a single statement and returns the updated environment.
    @staticmethod
    def run_statement(statement: str, env: Env, lines: Lines) -> Env:
        """Executes a single statement."""
        command = statement.strip().split()[0]
        if command == "let":
            return Interpreter.assign_variable(statement, env)
        elif command == "print":
            Interpreter.print_stmt(statement, env)
            return env
        elif command == "if":
            Interpreter.if_stmt(statement, env)
            return env
        elif command == "while":
            return Interpreter.while_loop(statement, env, lines)
        elif command == "goto":
            return env
        else:
            print(f"Unknown statement: {statement}")
            return env
        
    # execute_program(lines: Lines, env: Env) -> Env:
    #     Runs the entire program from the provided lines and environment.
    @staticmethod
    def execute_program(lines: Lines, env: Env) -> Env:
        """Executes the program in a declarative, pure style."""
        current_line = min(lines) if lines else 1
        current_env = env

        while current_line in lines:
            stmt = lines[current_line]
            if stmt.startswith("goto"):
                target = Interpreter.goto(stmt, lines)
                if target is not None:
                    current_line = target
                else:
                    break
            else:
                current_env = Interpreter.run_statement(stmt, current_env, lines)
                current_line += 1
        return current_env
    
    # load_program() -> Lines:
    #     Loads a program from user input, returning a dictionary of line numbers to statements.
    #     The program ends when the user types 'END'.
    #     The program is loaded into a dictionary with line numbers as keys.
    @staticmethod
    def load_program() -> Lines:
        print("Enter your program line by line. Type 'END' to finish.")
        lines = {}
        line_number = 1
        finished = False
        while not finished:
            line = input(f"Line {line_number}: ").strip()
            if line.upper() == "END":
                finished = True
            else:
                lines[line_number] = line
                line_number += 1
        return lines
    
    # view_environment(env: Env) -> None:
    #     Displays the current environment variables and their values.
    #     The environment is a dictionary mapping variable names to their values.
    @staticmethod
    def view_environment(env: Env) -> None:
        """Displays the current environment."""
        print("\nCurrent Environment:")
        for k, v in env.items():
            print(f"{k} = {v}")
        print()

    # main_menu() -> None:
    #     Provides a simple interactive menu for loading, running, and inspecting programs.
    #     The function uses a while loop to repeatedly display the menu options.
    #     The user can select an option by entering a number.
    #     The function handles user input and calls the appropriate methods to load, run, or view the program.
    @staticmethod
    def main_menu() -> None:
        lines: Interpreter.Lines = {}
        env: Interpreter.Env = {}

        while True:
            print("\nToy Language Interpreter")
            print("1. Load program")
            print("2. Run program")
            print("3. View environment")
            print("4. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                lines = Interpreter.load_program()
            elif choice == '2':
                env = Interpreter.execute_program(lines, env)
            elif choice == '3':
                Interpreter.view_environment(env)
            elif choice == '4':
                sys.exit()
            else:
                print("Invalid option. Please select 1-4.")

if __name__ == "__main__":
    Interpreter.main_menu()
