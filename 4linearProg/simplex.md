# Simplex Method

## Introduction

Linear programming is a method to achieve the best outcome (maximum or minimum) in a mathematical model whose requirements are represented by linear relationships. Linear programming is a special case of mathematical programming (also known as mathematical optimization). In general, mathematical programming is the selection of a best element (with regard to some criterion) from some set of available alternatives. In mathematical programming, the alternatives are represented by mathematical models, and the selection criterion is represented by an objective function. The objective function is usually represented by a mathematical equation that defines an optimization problem to be solved. The optimization problem is solved subject to a set of constraints, which are usually represented by a system of linear equations or inequalities.

## Simplex Method

The simplex method is a method for solving linear programming problems. It is a widely used and efficient algorithm for solving linear programming problems. The simplex method is a special case of the more general method of linear programming. The simplex method is a direct search method that is used to solve linear programming problems. The simplex method is a method for solving linear programming problems. It is a widely used and efficient algorithm for solving linear programming problems. The simplex method is a special case of the more general method of linear programming. The simplex method is a direct search method that is used to solve linear programming problems.

## Example

### Problem

Maximize $Z = 3x_1 + 5x_2$

Subject to:

$x_1 + x_2 \leq 4$

$2x_1 + x_2 \leq 12$

$x_1, x_2 \geq 0$

### Solution

We will use the simplex method to solve this problem.

First we will change the problem to the standard form:

Maximize $Z = 3x_1 + 5x_2$

Subject to:

$x_1 + x_2 - x_3 = 4$

$2x_1 + x_2 - x_4 = 12$

$x_1, x_2, x_3, x_4 \geq 0$

$x_3, x_4$ are slack variables.

We will use the tableau method to solve this problem.

We will start with the initial tableau:

|     | $x_1$ | $x_2$ | $x_3$ | $x_4$ | RHS |
| --- | ----- | ----- | ----- | ----- | --- |
| $Z$ | 3     | 5     | 0     | 0     | 0   |
| $1$ | 1     | 1     | 1     | 0     | 4   |
| $2$ | 2     | 1     | 0     | 1     | 12  |

We will choose the pivot column. The pivot column is the column with the smallest negative value. In this case, the pivot column is $x_1$.

We will choose the pivot row. The pivot row is the row with the smallest ratio of the RHS to the pivot column. In this case, the pivot row is $1$.

We will divide the pivot row by the pivot element. In this case, the pivot element is $1$.

We will subtract the pivot row from all other rows.

the new tableau is:

|     | $x_1$ | $x_2$ | $x_3$ | $x_4$ | RHS |
| --- | ----- | ----- | ----- | ----- | --- |
| $Z$ | 0     | 1     | 1     | 0     | 4   |
| $1$ | 1     | 0     | 0     | 0     | 1   |
| $2$ | 0     | 1     | 0     | 1     | 8   |

We will choose the pivot column. The pivot column is the column with the smallest negative value. In this case, the pivot column is $x_2$.

We will choose the pivot row. The pivot row is the row with the smallest ratio of the RHS to the pivot column. In this case, the pivot row is $2$.

We will divide the pivot row by the pivot element. In this case, the pivot element is $2$.

We will subtract the pivot row from all other rows.

the new tableau is:

|     | $x_1$ | $x_2$ | $x_3$ | $x_4$ | RHS |
| --- | ----- | ----- | ----- | ----- | --- |
| $Z$ | 0     | 0     | 1     | 0     | 2   |
| $1$ | 0     | 0     | 0     | 0     | 1   |
| $2$ | 0     | 1     | 0     | 1     | 8   |

now we have a solution. The solution is:

$x_1 = 1$

$x_2 = 2$

$x_3 = 0$

$x_4 = 0$

$Z = 2$
