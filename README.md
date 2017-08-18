# ML
**Gradient_LinearModel.py**
* The above algorithm implements gradient descent for linear model(hypothesis space)
* This program takes the input file(comma separated) as input and learns on the same
* As a output you obtain slope and y-intercept for the straight line(m,b) which approximates the data
* The training set is trained for 1000 iterations

   **Execution**
* python Gradient_LinearModel.py data.csv

   **Output**
* The data file being trained on is:data.csv
* starting gradient at m=0,b=0 and error=5565.10783448
* running
* After 1000 iterations of gradient descent the m=1000,b=-0.037979888826 and error=15.3223965149

   **Note**
* This works on single dimensional input and output.
* The data should be comma separated. 
* As you might already know this can be solved using linear regression using direct formula to find the weights.

**GradientNNewtonOpti_Illustration.py**
* The above algorithm implements gradient descent and newton optmization
* The newton optimization is implemented on derivative of function since the roots of derivate function are the points correspoding to the minimal of actual function
* The above is one of the second order optimization
* The above program is illustrated for quadratic and rosenbrock function
* The gradient descent does not work for rosenbrock function because of it's peculiar nature
* Rosenbrock function is a non convex function and it has a narrow curved valley
* But The newton optimization works well for both the functions.
* The important takeaway is the fact that the second order optimization is more powerful than gradient but it is costly due to complex operations.
* The second order optimization can be used for smaller training sets or when the error functions are like Rosenbrock functions or zigzag functions making the convergence of the gradient difficult.

   **Execution**
* python GradientNNewtonOpti_Illustration.py

    **Output**
* The output illustrates that the Gradient is not a solution for all.   
* The output is self explanatory
