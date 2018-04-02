from numpy import *
import sys
def run():
    print "The data file being trained on is:{0}".format(sys.argv[1])
    points=genfromtxt(sys.argv[1], delimiter=",")
    learning_rate=0.0001
    initial_m=0
    initial_b=0
    num_iterations=1000
    print "starting gradient at m={0},b={1} and error={2}".format(initial_m,initial_b,compute_error(initial_m,initial_b,points))
    print "running"
    [m,b]=optimize_error(initial_m,initial_b,points,num_iterations,learning_rate)
    print "After {0} iterations of gradient descent the m={0},b={1} and error={2}".format(num_iterations,m,b,compute_error(m,b,points))

def compute_error(m,b,points):
    totalError=0
    for i in range(0,len(points)):
        x=points[i,0]
        y=points[i,1]
        expectedvalue=m*x+b
        totalError=totalError+(y-expectedvalue)**2
    return totalError/float(len(points))

def optimize_error(m,b,points,num_iterations,learning_rate):
    N=float(len(points))
    m_gradient=0
    b_gradient=0
    for i in range(0,num_iterations):
        for j in range(0,len(points)):
            x=points[j,0]
            y=points[j,1]
            m_gradient += -(2/N)*x*(y-((m*x)+b))
            b_gradient += -(2/N)*(y-((m*x)+b))
        m=m-(learning_rate*m_gradient)
        b=b-(learning_rate*b_gradient)
    return [m,b]
if __name__=='__main__':
    run()
