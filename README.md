# API

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- What Bash scripting should not be used for
- What is an API
- What is a REST API
- What are microservices
- What is the CSV format
- What is the JSON format
- Pythonic Package and module name style
- Pythonic Class name style
- Pythonic Variable name style
- Pythonic Function name style
- Pythonic Constant name style
- Significance of CapWords or CamelCase in Python

### What Bash scripting should not be used for
Bash scripting is powerful for automating tasks in Unix-like environments, but it has limitations and is not suitable for:
- `Complex GUI applications`: Bash lacks native support for graphical user interfaces.
- `Large programs`: Bash scripts can become unwieldy and difficult to maintain when they grow too large or complex.
- `High-performance applications`: Scripts are interpreted, not compiled, which can make them slower than programs written in compiled languages like C or Java.
- `Cross-platform applications`: Bash scripts are primarily designed for Unix-like systems and might not run natively on other platforms like Windows.

### What is an API
An API (Application Programming Interface) is a set of rules and protocols for building and interacting with software applications. An API defines methods and data structures to interact with software components without knowing the implementation details.

### What is a REST API
A REST (Representational State Transfer) API is a type of API that adheres to the REST architectural principles, using standard HTTP methods like GET, POST, PUT, and DELETE. REST APIs are designed to be stateless, and they commonly exchange data in JSON or XML format.

### What are microservices
Microservices architecture is a method of developing software systems that breaks them down into smaller, independent pieces (services) that work together. Each service is self-contained and performs a specific business function, communicating with other services via well-defined APIs.

### What is the CSV format
CSV (Comma-Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or database. Each line in a CSV file corresponds to a data record, and each record consists of fields that are separated by commas.

### What is the JSON format
JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. It is based on a subset of the JavaScript Programming Language and typically used to transmit data between a server and web application.

### Pythonic Package and module name style
Packages and modules in Python should have short, all-lowercase names, and underscores can be used if it improves readability (e.g., `my_module`).

### Pythonic Class name style
Class names in Python should typically use the CapWords convention (also known as CamelCase) where each word is capitalized and no underscores are used (e.g., `MyClass`).

### Pythonic Variable name style
Variables in Python should have short, lowercase words separated by underscores to improve readability (e.g., `my_variable`).

### Pythonic Function name style
Function names in Python should be lowercase, with words separated by underscores as necessary to improve readability (e.g., `my_function()`).

### Pythonic Constant name style
Constants in Python are typically defined on a module level and written in all capital letters with underscores separating words (e.g., `MY_CONSTANT`).

### Significance of CapWords or CamelCase in Python
CapWords, or CamelCase, is significant in Python as it helps distinguish class names from other types of names. This naming convention aids in the readability of code, particularly in object-oriented programming, by signaling that a name represents a class.
