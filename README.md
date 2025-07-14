# About

Do you *hate* turning functions into classes? Are you tired of writing `self.var = var` 100 times?
I know I was, that's why I made **AutoClass**!  
Simply provide the class name and all the variables, and you're set.

# Example

Say you want to make the class `Test` and include the variables `y`, `z`.

  ## Importing the File:

  ### Input:
  ```python
  >>> from autoclass import class_generator
  >>> class_generator("Test", "y", "z")
  ```
  ### Output:
  ```python
  class Test:

      def __init__(self, y, z):
          self.y = y
          self.z = z
  ```

  ## Using in the Terminal:

  ### Input:
  ```python
  python autoclass.py Test y z
  ```
  ### Output:
  ```python
  class Test:

      def __init__(self, y, z):
          self.y = y
          self.z = z
  ```

## Plans
Of course right now it's a very simple tool, but if it saves even one person some time, I think it was worth making. 
I'm definately planning on adding more features, so stay tuned!
- Make it Pip Installable
- Other Stuff Too
### Contact
Feel free to reach out if you have a question or an idea!
(Yes, the license was *very* necessary.)
#### Email: nathanbsmith729@gmail.com
