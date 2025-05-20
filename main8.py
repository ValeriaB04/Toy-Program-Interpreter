# -*- coding: utf-8 -*-
"""
Created on Mon May 19 17:06:37 2025

@author: disha
"""

from typing import Union, Dict, Final
from dataclasses import dataclass 
#from enum import Enum

class Interpreter(): 
    #using declarative programming style here
    variables: dict = {}
    env: Dict[str, Union[int, bool, str]] = {}
    lines : dict = {}
    current_line = 0
    #current_line = 1 
    
    @classmethod    
    def evaluate_expression(self,expr: str) -> Union[int, bool, str]:
      try:
          for variable in self.env: 
              expr = expr.replace(variable, str(self.env[variable]))
          return eval(expr)
      except Exception as e: 
        print(f"Error evaluating expression '{expr}': {e}")
        return 
    @classmethod
    def assign_variable(self,value: str, key: int) -> dict:
        self.variables[key] = value
        print(self.variables)

    @classmethod
    def print_stmt(self, statement: str):
        expr = statement.split("print", 1)
        value = self.evaluate_expression(expr)
        print(value) 
    @classmethod
    def if_stmt(self):
        a_input = int(input("Please enter of value of a : "))
        b_input = int(input("Please enter the value of b: "))
        operator = input("Please enter the operator: ")
        new_value = operator 
        a = True
        if new_value == ">":
            print("Checking if a value is greater than b")
            if a_input > b_input:
                print(a)
            else:
                a = False
                print(a)
        elif new_value == ">=":
            print("Checking if a value is greater than b")
            if a_input >= b_input:
                print(a)
            else:
                a = False
                print(a)
        elif new_value == "<":
            print("Checking if a value is greater than b")
            if a_input < b_input:
                print(a)
            else:
                a = False
                print(a)
        elif new_value == "<=":
            print("Checking if a value is greater than b")
            if a_input <= b_input:
                print(a)
            else:
                a = False
                print(a)
        elif new_value == "==":
            print("Checking if a value is greater than b")
            if a_input == b_input:
                print(a)
            else:
                a = False
                print(a)

        
    @classmethod
    def while_or_for_loop(self, statement:str):
        user_input = input("Enter the operation you want to carry out: ")
        a_input = int(input("Enter the value of a: "))
        b_input = int(input("Enter the value of b: "))
        if user_input == "while loop":
            target = int(input("What's your target"))
            #while target < a_input
    @classmethod        
    def goto(self, statement:str):
        line_number = statement.split("goto")
        target = int(line_number)
        if target in self.lines:
            self.current_line = target 
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
            print(f"The statement is incorrect or invalid: {statement}")
    @classmethod        
    def load_program(cls):
        print("Enter your program line by line. Type 'END' to finish.")
        line_number = 1
        while True:
            line = input(f"Line {line_number}: ")
            if line.strip().upper() == "END":
                break
            else:
                cls.lines[line_number] = line
                line_number += 1
    @classmethod            
    def execute_program(self):
        self.current_line = 1
        while self.current_line in self.lines:
            statement = self.lines[self.current_line]
            self.run_statement(statement)
            self.current_line += 1
    @classmethod
    def display_environment(self):
        print("\nCurrent Environment:")
        for z, v in self.env.items():
            print(f"{z} = {v}")
    
    @classmethod
    def main_menu_choices(cls):
            print("\nToy Language Interpreter")
            print("1. Load program")
            print("2. Run program")
            print("3. View environment")
            print("4. Assign Variable")
            print("5. Exit")
            print("6. If statement")
            
    @classmethod
    def main_menu(cls):
        a = True
        while a:
            i = Interpreter()
            print(i.main_menu_choices())
            choice = input("Select an option: ")
            if choice == '1':
                i.load_program()
            elif choice == '2':
                i.execute_program()
            elif choice == '3':
                i.display_environment()
            elif choice == '4':
                return 
                #i.assign_variable(1, "hiiii")
            elif choice == '5':
                a = False
            elif choice == '6':
                i.if_stmt()
            else:
                print("Invalid option. Please select 1-5.")

if __name__ == "__main__":
    interpreter = Interpreter()
    interpreter.main_menu()
