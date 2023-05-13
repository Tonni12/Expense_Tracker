# coding=utf-8
"""
    This project gives detailed explanation and implementation of data structures and algorithms in python
    :: parameters
    :: return
"""
import graphviz
import sympy
import math
import statistics
import numpy as np
import scipy.integrate
import scipy.optimize

class AdvancedEngineeringCalculator:

    def __init__(self):
        self.display = ""
        self.operator = ""
        self.numbers = []
        self.graph = graphviz.Digraph()

    def input(self, value):
        self.display += value

    def clear(self):
        self.display = ""
        self.operator = ""
        self.numbers = []
        self.graph = graphviz.Digraph()

    def calculate(self):
        global result, result
        if self.operator == "+":
            result = self.numbers[0] + self.numbers[1]
        elif self.operator == "-":
            result = self.numbers[0] - self.numbers[1]
        elif self.operator == "*":
            result = self.numbers[0] * self.numbers[1]
        elif self.operator == "/":
            result = self.numbers[0] / self.numbers[1]
        elif self.operator == "^":
            result = self.numbers[0] ** self.numbers[1]
        elif self.operator == "log":
            result = math.log(self.numbers[0], self.numbers[1])
        elif self.operator == "sin":
            result = math.sin(self.numbers[0])
        elif self.operator == "cos":
            result = math.cos(self.numbers[0])
        elif self.operator == "tan":
            result = math.tan(self.numbers[0])
        elif self.operator == "cosh":
            result = math.cosh(self.numbers[0])
        elif self.operator == "sinh":
            result = math.sinh(self.numbers[0])
        elif self.operator == "tanh":
            result = math.tanh(self.numbers[0])
        elif self.operator == "atan":
            result = math.atan(self.numbers[0])
        elif self.operator == "asin":
            result = math.asin(self.numbers[0])
        elif self.operator == "asinh":
            result = math.asinh(self.numbers[0])
        elif self.operator == "acosh":
            result = math.acosh(self.numbers[0])
        elif self.operator == "acos":
            result = math.acos(self.numbers[0])
        elif self.operator == "sqrt":
            result = math.sqrt(self.numbers[0])
        elif self.operator == "cbrt":
            result = math.cbrt(self.numbers[0])
        elif self.operator == "factorial":
            result = math.factorial(self.numbers[0])
        elif self.operator == "combination":
            result = math.comb(self.numbers[0], self.numbers[1])
        elif self.operator == "permutation":
            result = math.perm(self.numbers[0], self.numbers[1])
        elif self.operator == "variance":
            result = statistics.variance(self.numbers[0], self.numbers[1])
        elif self.operator == "graph":
            self.graph.node("A", self.numbers[0])
            self.graph.node("B", self.numbers[1])
            self.graph.edge("A", "B")
            self.graph.render("graph.png")
        else:
            result = None
        self.display = str(result)
        self.numbers = []
        self.operator = ""

    def get_display(self):
        return self.display
    def get_numbers(self):
        return self.numbers
    def get_operator(self):
        return self.operator
    def get_graph(self):
        return self.graph

    def solve_equation(self, equation):
        try:
            result = sympy.solve(equation)
        except:
            result = None
        return result

    def integrate(self, function, lower_bound, upper_bound):
        try:
            result = scipy.integrate.quad(function, lower_bound, upper_bound)
        except:
            result = None
        return result

    def differentiate(self, function, x):
        try:
            result = sympy.diff(function, x)
        except:
            result = None
        return result

    def optimize(self, function, x_0, method):
        try:
            result = scipy.optimize.minimize(function, x_0, method = method)
        except:
            result = None
        return result

if __name__ == "__main__":
    calculator = AdvancedEngineeringCalculator()

    while True:
        value = input("Enter a value: \n")
        if value == "clear":
            calculator.clear()
        elif value == "=":
            calculator.calculate()
        else:
            calculator.input(value)

        print(calculator.get_display())