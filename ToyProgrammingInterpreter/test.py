from main import Interpreter

# Test variable assignment using 'let' statements
def test_let_assignment():
    lines = {
        1: "let x = 10",
        2: "let y = x + 5"
    }
    env = {}
    env = Interpreter.execute_program(lines, env)  
    assert env["x"] == 10
    assert env["y"] == 15

# Test printing a variable value using 'print' statement
def test_print_stmt(capfd):
    lines = {
        1: "let x = 7",
        2: "print x"
    }
    env = {}
    env = Interpreter.execute_program(lines, env) 
    out, err = capfd.readouterr()
    assert "7" in out
    assert env["x"] == 7

# Test 'if' statement when the condition is true
def test_if_statement_true(capfd):
    lines = {
        1: "let x = 5",
        2: "if x == 5"
    }
    env = {}
    env = Interpreter.execute_program(lines, env) 
    out, err = capfd.readouterr()
    assert "Condition is True" in out
    assert env["x"] == 5

# Test 'if' statement when the condition is false
def test_if_statement_false(capfd):
    lines = {
        1: "let x = 3",
        2: "if x == 10"
    }
    env = {}
    env = Interpreter.execute_program(lines, env)  
    out, err = capfd.readouterr()
    assert "Condition is False" in out
    assert env["x"] == 3

# Test 'while' loop execution and variable increment
def test_while_loop():
    lines = {
        1: "let x = 0",
        2: "while x < 5: let x = x + 1"
    }
    env = {}
    env = Interpreter.execute_program(lines, env)  
    assert env["x"] == 5

# Test 'goto' statement to jump to a specific line
def test_goto_line():
    lines = {
        1: "let x = 5",
        2: "goto 4",
        3: "let x = 10",  
        4: "let y = x + 1"
    }
    env = {}
    env = Interpreter.execute_program(lines, env)  
    assert env["x"] == 5
    assert env["y"] == 6
    assert env.get("x") != 10
