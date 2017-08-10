# ML
**Gradient_LinearModel.py**
* The above algorithm implements gradient descent for linear model(hypothesis space)
* This program takes the input file(comma separated) as input and learns on the same
* As a output you obtain slope and y-intercept for the straight line(m,b) which approximates the data
* The training set is trained for 1000 iterations

**Execution**
* python Gradient_LinearModel.py data.csv

**Output**
The data file being trained on is:data.csv
starting gradient at m=0,b=0 and error=5565.10783448
running
After 1000 iterations of gradient descent the m=1000,b=-0.037979888826 and error=15.3223965149

**Note**
* This works on single dimensional input and output.
* The data should be comma separated. 
* As you might already know this can be solved using linear regression using direct formula to find the weights.
