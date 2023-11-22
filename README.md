# Arithmetic Formatter

Full code run with examples test can be found in: https://replit.com/@tiagoreboucas90/boilerplate-arithmetic-formatter#arithmetic_arranger.py

Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:
```text
  235
+  52
-----
```

There is a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function can optionally take a second argument. When the second argument is set to `True`, the answers are displayed.

## Examples
**Function Call**: arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

**Output**:
```text
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```
<br/>

**Function Call**: arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

**Output**:
```text
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```
<br/>

## Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

- Situations that will return an error:
    - If there are too many problems supplied to the function. The limit is five, anything more will return: `Error: Too many problems.`
    - The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. The error returned will be: `Error: Operator must be '+' or '-'.`
    - Each number (operand) should only contain digits. Otherwise, the function will return: `Error: Numbers must only contain digits.`
    - Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: `Error: Numbers cannot be more than four digits.`

## Testing
- If you chose to open in [replit](https://replit.com/@tiagoreboucas90/boilerplate-arithmetic-formatter#arithmetic_arranger.py), the code is writen in `arithmetic_arranger.py`. For development, you can use `main.py` to test the `arithmetic_arranger()` function. Click the "run" button and `main.py` will run.
- The unit tests for this project are in `test_module.py`. We are running the tests from `test_module.py` in `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button. Alternatively you may run the tests by inputting `pytest` in the console.
