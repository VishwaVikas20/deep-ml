import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    def derivative(f):
        n = len(f)
        deriv = []
        for i, coeff in enumerate(f):
            power = n - 1 - i
            if power > 0:
                deriv.append(coeff * power)
        return deriv
    # Your code here
    def compute(coeff, x):
        n = len(coeff)
        v = 0
        for i, l in enumerate(coeff):
            v += l * (x ** (n - 1 - i)) 
        return v
    g_derivative=derivative(g_coeffs)
    h_derivative=derivative(h_coeffs)
    numerator=compute(g_derivative,x)*compute(h_coeffs,x)-compute(g_coeffs,x)*compute(h_derivative,x)
    denominator=compute(h_coeffs,x)**2
    return numerator/denominator