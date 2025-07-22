# Scientific Computing CAT 1

This repository contains Python scripts for the Scientific Computing CAT 1 assignment.

## Assignment Questions & Corresponding Files

### a) Line Graph of Temperature Readings

**Question:** Write a program to plot a line graph representing the temperature readings over a week: 20, 22, 19, 23, 21, 24, 20.

**File:** [`line-graph.py`](./line-graph.py)

This script uses `matplotlib` to generate and display a line graph of the given weekly temperature readings.

### b) Arithmetic Sequence

**Question:** Write a program to generate the arithmetic sequence starting at 5 with a common difference of 3, for 8 terms.

**File:** [`arithmetic-sequence.py`](./arithmetic-sequence.py)

This script calculates and prints the first 8 terms of an arithmetic sequence with a starting term of 5 and a common difference of 3.

### c) Volume Under a Surface (Numerical Integration)

**Question:** Write a program to calculate the volume under the surface z = x^2 + y^2 over the square region 0 ≤ x, y ≤ 1.

**File:** [`numerical-intergration.py`](./numerical-intergration.py)

This script uses numerical integration (specifically, `scipy.integrate.dblquad`) to compute the double integral of the function z = x^2 + y^2 over the specified square region, which gives the volume under the surface.

### d) Compiled vs. Interpreted Languages

**Question:** Explain the differences between compiled and interpreted programming languages, and classify Python in this context.

**1.	Execution Process:
o	Compiled languages translate the entire program into machine code before execution whereas Interpreted languages run the code line-by-line using an interpreter at runtime.
2.	Speed:
o	Compiled programs generally run faster because they are already translated into machine code whereas Interpreted programs tend to be slower due to real-time translation during execution.
3.	Error Handling:
o	Compiled languages catch most errors at compile-time, before the program runs whereas Interpreted languages catch errors during execution, which may cause runtime interruptions.
4.	Portability:
o	Compiled code is often specific to the platform it was compiled on unlike Interpreted code which run on any system that has the appropriate interpreter, making it more portable.
5.	Examples and Python’s Classification:
o	Examples of compiled languages include C, C++, and Rust.
o	Examples of interpreted languages include Python, JavaScript, and Ruby. 
**