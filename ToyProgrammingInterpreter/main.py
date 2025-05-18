
class Interpreter: 
    def __init__(self):
        self.variables = {}
        self.lines = []
        self.current_line = 0

    # Convert expression string into a value 
    def eval_expr(self,expr):
      try:
        return eval(expr, {}, self.variable)
      except Exception as e: 
        print(f"Error evaluating expression '{expr}': {e}")
        return 

    # Assign a variable in the environment 
    def assign_variable(self,key,value):
        self.variables[key] = value
        print(self.variables)

    # let print_stmt: str -> None
    def print_stmt(self, expr) -> None:
      value = self.eval_expr(expr)
      print(value) 

    # Execute a while loop given a condition and a start line to loop back to
    def while_loop(self, condition, start_line, current_line):
        if self.eval_expr(condition):
            return start_line  
        else:
            return current_line + 1
        
interpreter = Interpreter()
interpreter.assign_variable("hi",1)
