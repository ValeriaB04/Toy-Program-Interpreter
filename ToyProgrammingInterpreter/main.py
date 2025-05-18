
class Interpreter: 
    def __init__(self):
        self.variables = {}
        self.lines = []
        self.current_line = 0
    
    def evaluate_expression(self,expr):
      try:
        return eval(expr, {}, self.variable)
      except Exception as e: 
        print(f"Error evaluating expression '{expr}': {e}")
        return 
    def assign_variable(self,key,value):
        self.variables[key] = value
        print(self.variables)
interpreter = Interpreter()
interpreter.assign_variable("hi",1)
