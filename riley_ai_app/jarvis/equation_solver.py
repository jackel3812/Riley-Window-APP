from sympy import symbols, Eq, solve

class EquationSolver:
    def __init__(self):
        self.variables = symbols('x y z')  # Define variables for equations

    def solve_equation(self, equation_str):
        try:
            # Parse the equation string into a sympy equation
            lhs, rhs = equation_str.split('=')
            equation = Eq(eval(lhs), eval(rhs))

            # Solve the equation
            solution = solve(equation, self.variables)
            return solution
        except Exception as e:
            return f"Error solving equation: {str(e)}"

    def solve_system_of_equations(self, equations):
        try:
            # Parse the list of equation strings into sympy equations
            sympy_equations = [Eq(eval(eq.split('=')[0]), eval(eq.split('=')[1])) for eq in equations]

            # Solve the system of equations
            solution = solve(sympy_equations, self.variables)
            return solution
        except Exception as e:
            return f"Error solving system of equations: {str(e)}"