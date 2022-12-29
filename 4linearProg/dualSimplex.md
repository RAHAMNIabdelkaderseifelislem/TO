# Dual Simplex

is a method for solving linear programming problems. It is a widely used and efficient algorithm for solving linear programming problems. The dual simplex method is a special case of the more general method of linear programming. The dual simplex method is a direct search method that is used to solve linear programming problems. The dual simplex method is a method for solving linear programming problems. It is a widely used and efficient algorithm for solving linear programming problems. The dual simplex method is a special case of the more general method of linear programming. The dual simplex method is a direct search method that is used to solve linear programming problems.

## Example

### Problem

Maximize $Z = 3x_1 + 5x_2$

Subject to:

$x_1 + x_2 \leq 4$

$2x_1 + x_2 \leq 12$

$x_1, x_2 \geq 0$

### Solution

we will get the dual problem:

Minimize $Z = 4y_1 + 12y_2$

Subject to:

$y_1 + 2y_2 \leq 3$

$y_1 + y_2 \leq 5$

$y_1, y_2 \geq 0$

we will use the simplex method to solve this problem.

First we will change the problem to the standard form:

Minimize $Z = 4y_1 + 12y_2$

Subject to:

$y_1 + 2y_2 - y_3 = 3$

$y_1 + y_2 - y_4 = 5$

$y_1, y_2, y_3, y_4 \geq 0$

$y_3, y_4$ are slack variables.

We will use the tableau method to solve this problem.

We will start with the initial tableau:

|     | $y_1$ | $y_2$ | $y_3$ | $y_4$ | RHS |
| --- | ----- | ----- | ----- | ----- | --- |
| $Z$ | 4     | 12    | 0     | 0     | 0   |
| $1$ | 1     | 2     | 1     | 0     | 3   |
| $2$ | 1     | 1     | 0     | 1     | 5   |

We will choose the pivot column $y_1$ because it has the smallest value.

We will choose the pivot row $1$ because it has the smallest ratio.

We will get the new tableau:

|     | $y_1$ | $y_2$ | $y_3$ | $y_4$ | RHS |
| --- | ----- | ----- | ----- | ----- | --- |
| $Z$ | 0     | 4     | 1     | 0     | 3   |
| $1$ | 0     | 0     | 1     | 0     | 1   |
| $2$ | 1     | 1     | 0     | 1     | 5   |

We will choose the pivot column $y_2$ because it has the smallest value.

We will choose the pivot row $2$ because it has the smallest ratio.

We will get the new tableau:

|     | $y_1$ | $y_2$ | $y_3$ | $y_4$ | RHS |
| --- | ----- | ----- | ----- | ----- | --- |
| $Z$ | 0     | 0     | 1     | 0     | 1   |
| $1$ | 0     | 0     | 1     | 0     | 1   |
| $2$ | 1     | 0     | 0     | 1     | 4   |

the optimal solution is $y_1 = 1, y_2 = 0, y_3 = 1, y_4 = 4$ and $Z = 4$
