import numpy as np
from sympy import *
from sympy.parsing import sympy_parser as spp

weights_matrix = Matrix(symbols('w1 w2'))
#Tolerable Error while approximating function
error = 0.3
#Start weigts
weights_start=np.array([-4.0, 6.0])
#If a quadratic function is being used as an error function whose roots are known
weights_result= np.array([0.0,0.0])

#Computing the value of (nx1) Matrix at any given point 
def computexprmatrix(exprmatrix,x):
    return [float(exprmatrix[i].subs(weights_matrix[0],x[0]).subs(weights_matrix[1],x[1])) for i in range(len(exprmatrix))]

#Compute the error function at a particular value of weights.This can be extended to compute the value based on training set given 
#Currently it just substitutues the weights and returns the same
def computeerror(obj,x):
    return float(obj.subs(weights_matrix[0],x[0]).subs(weights_matrix[1],x[1]))

#Computes the values of weights by gradient descent
def steepestdescent(alpha=0.05):
    gradient=[diff(obj,weights_matrix[i]) for i in range(len(weights_matrix))]
    weights=weights_start
#Here we are trying to minimize the distance between the known root of function and weights vector
#Instead the below compute error can also be choosen for actual problems
    while np.linalg.norm(weights-weights_result)>error:
    #while computeerror(obj,weights)>error:
        gradient_value=computexprmatrix(gradient,weights)
        weights=weights-np.dot(alpha,gradient_value)
    print weights
    print "The value of error function for above weights is{0}".format(computeerror(obj,weights))
    print "The value of distance between two weight vectors is{0}".format(np.linalg.norm(weights-weights_result))

#Computes the values of weights by newton method of optimization
#second order optimization
def newtonoptimization():
    gradient=Matrix([diff(obj,weights_matrix[i]) for i in range(len(weights_matrix))])
    hessian=Matrix([[diff(gradient[i],weights_matrix[j]) for j in range(len(weights_matrix))] for i in range(len(gradient))])
    hessian_inv=hessian.inv() 
    weights=weights_start
#Here we are trying to minimize the distance between the known root of function and weights vector
#Instead the below compute error can also be choosen for actual problems
    while np.linalg.norm(weights-weights_result)>error:
    #while computeerror(obj,weights)>error:
        gradient_value=Matrix(computexprmatrix(gradient,weights))
        newton=hessian_inv*gradient
        newton_value=computexprmatrix(newton,weights)
        weights=weights-newton_value
    print weights
    print "The value of error function for above weights is{0}".format(computeerror(obj,weights))
    print "The value of distance between two weight vectors is{0}".format(np.linalg.norm(weights-weights_result))
    
    
if __name__=='__main__':
    #Below is the Error function which is quadratic
    obj=spp.parse_expr('w1**2 - 2 * w1 * w2 + 4 * w2**2')
    #Call for Steepest descent or in other words gradient(first order optimization)
    steepestdescent()
    #Call for Newton Optimization(second order optimization)
    newtonoptimization()
