import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    def derivative(f):
        temp=[]
        for i,v in enumerate(f):
            if i==0:
                pass
            temp.append(i*v)
        return temp
    def multiply(f,g):
        temp=[0]*(max(len(f),len(g))+1)
        for i in range(len(f)):
            for j in range(len(g)):
                temp[i+j]+=f[i]*g[j]
        return temp
    r1=multiply(f_coeffs,derivative(g_coeffs))
    r2=multiply(g_coeffs,derivative(f_coeffs))
    return [x + y for x, y in zip(r1, r2)][1:]

    