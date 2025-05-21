from toyProgram import Interpreter

def setup_function():
    Interpreter.env = {}
    Interpreter.lines = {}
    Interpreter.current_line = 1

# Test variable assignment (let)
def test_let_assignment():
    Interpreter.lines = {
        1: "let x = 10",
        2: "let y = x + 5"
    }
    Interpreter.execute_program()
    assert Interpreter.env["x"] == 10
    assert Interpreter.env["y"] == 15

# Test print statement
def test_print_stmt():
    Interpreter.lines = {
        1: "let x = 7",
        2: "print x"
    }
    Interpreter.execute_program()
    assert Interpreter.env["x"] == 7  

# Test if statement
def test_if_statement_true():
    Interpreter.lines = {
        1: "let x = 5",
        2: "if x == 5"
    }
    Interpreter.execute_program()
    assert Interpreter.env["x"] == 5  

def test_if_statement_false():
    Interpreter.lines = {
        1: "let x = 3",
        2: "if x == 10"
    }
    Interpreter.execute_program()
    assert Interpreter.env["x"] == 3  

# Test while loop
def test_while_loop():
    Interpreter.lines = {
        1: "let x = 0",
        2: "while x < 5: let x = x + 1"
    }
    Interpreter.execute_program()
    assert Interpreter.env["x"] == 3  # Loop runs until x == 3

# Test goto skips a line
def test_goto_line():
    Interpreter.lines = {
        1: "let x = 5",
        2: "goto 4",
        3: "let x = 10",  # Should be skipped
        4: "let y = x + 1"
    }
    Interpreter.execute_program()
    assert Interpreter.env["x"] == 5
    assert Interpreter.env["y"] == 6
    assert Interpreter.env.get("x") != 10