# Python Basics

This guide briefly introduces some of the foundational concepts in the Python programming language, including:

- Python Operators
- Comments
- Zen of Python

## Python Operators
![Alt text](images/Whiteboard[1]-01.png)


Python supports a variety of operators, which can be categorized as:

- **Arithmetic Operators**: 
  - `+` : Addition
  - `-` : Subtraction
  - `*` : Multiplication
  - `/` : Division
  - `%` : Modulus

    ![Alt text](images/Whiteboard[2]-01.png)
  - `**`: Exponentiation
  - `//`: Floor division
  
- **Comparison Operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical Operators**: `and`, `or`, `not`, `:=`
- ... and many more.


## Comments

In Python, comments are lines that are not executed by the interpreter. They're used to explain code and improve readability.

- **Single-line comment**: Starts with `#`
  ```python
  # This is a single-line comment
  print("Hello, World!")  # This is an inline comment
  ```

- **Multi-line comment**: Python doesn't have explicit multi-line comment syntax, but you can use triple-quoted strings.
  ```python
  '''
  This is a multi-line
  comment or docstring
  '''
  print("Hello, World!")
  ```

## Zen of Python

The Zen of Python is a collection of 19 aphorisms that capture the philosophy of the Python language. To view them, simply run the following command in your Python environment:

```python
import this
```

While some may seem cryptic, they all provide valuable insights into writing clean, readable, and efficient Python code.
