# Chapter 6 Study Notes: Dictionaries, Sets, Formatting, Files, and Modules

---

## 6.1. Dictionaries

### Overview & Definition
* **Mapping Type:** Dictionaries are Python's built-in **mapping type**. Unlike sequences (strings, lists, tuples) indexed by integer ranges, dictionaries are indexed by **keys**.
* **Key-Value Pairs:** They store data as key-value pairs (also called *name-value*, *field-value*, or *attribute-value* pairs).
* **Terminology across CS:** Dictionaries are also known as **maps**, **symbol tables**, or **associative arrays**.
* **Key Restrictions:** Keys must be of an **immutable type** (e.g., strings, numbers, tuples containing immutable elements).
* **Value Flexibility:** Values can be of **any data type**, including mutable objects or other compound types.

### Creating Dictionaries
1. **Empty Dictionary Initialization:**
   ```python
   eng2sp = {}
   # type(eng2sp) yields <class 'dict'>
   ```
2. **Adding Elements via Assignment:**
   ```python
   eng2sp['one'] = 'uno'
   eng2sp['two'] = 'dos'
   eng2sp['three'] = 'tres'
   ```
3. **Literal Initialization:**
   ```python
   eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
   ```

### Characteristics
* **Syntax:** Key-value pairs are separated by commas; keys and values are separated by a colon (`key: value`). Enclosed in curly braces `{}`.
* **Unpredictable Ordering:** Lookups are performed by key, not index. As Python uses hash tables, ordering should not be relied upon.

---

## 6.2. Dictionary Operations

### Key Operations & Functions

| Operation / Function | Syntax Example | Behavior / Return |
| :--- | :--- | :--- |
| **Delete** | `del inventory['pears']` | Removes key-value pair from dictionary |
| **Length** | `len(inventory)` | Returns the number of key-value pairs |
| **Membership** | `'pears' in inventory` | Returns `True` if key exists, else `False` |
| **Safe Lookup** | `inventory.get('key', default)` | Returns value if key exists, otherwise returns default without raising error |
| **Key Sorting** | `sorted(inventory)` | Returns a sorted list of the dictionary's keys |

### Handling Missing Keys
* Accessing a non-existent key directly via bracket notation (`inventory['blueberries']`) raises a **`KeyError`**.
* Use the `.get(key, default)` method to safely retrieve values:
  ```python
  inventory.get('blueberries', 0) # Returns 0 if 'blueberries' is missing
  ```

---

## 6.3. Aliasing and Copying

Because dictionaries are **mutable**, assignment creates an **alias** (reference to the same object) rather than a duplicate.

* **Aliasing:**
  ```python
  an_alias = opposites
  an_alias['right'] = 'left' # Modifies 'opposites' as well
  ```
* **Shallow Copying (`.copy()`):**
  ```python
  a_copy = opposites.copy()
  a_copy['right'] = 'privilege' # 'opposites' remains unchanged
  ```

---

## 6.4. Sets

### Definition
* A **set** is an unordered collection of **unique** elements implementing the mathematical concept of a finite set.
* Like dictionaries, sets use curly braces `{}` but contain individual values rather than key-value pairs.

### Initialization
* **Set Literal:** `what_am_i = {'apples', 'bananas', 'pears'}` (`<class 'set'>`)
* **Empty Set:** Must use `set()`. Using `{}` creates an empty *dictionary*, not a set.
  ```python
  empty_set = set()
  ```

### Key Methods & Use Cases
* **Adding Elements:** `set_of_numbers.add(5)`
* **Membership Testing:** `3 in set_of_numbers` (Fast $O(1)$ lookup)
* **Deduplication:** Converting a list to a set removes all duplicate values:
  ```python
  list_of_numbers = [1, 2, 1, 3, 4, 8, 11, 4, 5, 8]
  unique_numbers = set(list_of_numbers) # {1, 2, 3, 4, 5, 8, 11}
  ```

---

## 6.5. & 6.6. String Formatting (f-strings)

Introduced in Python 3.6, **Formatted String Literals (f-strings)** provide concise syntax for string interpolation.

### Basic Syntax
Prefix the string with `f` or `F`, then place expressions inside curly braces `{}`:
```python
name = "Alice"
age = 10
f"I am {name} and I am {age} years old."
```

### Format Specifications
Format specifiers are added after a colon (`:`):
* **Alignment:** `<` (left), `^` (centered), `>` (right)
* **Width:** Number specifying field width (e.g., `10`)
* **Type Conversion:** `f` (float), `x` (hexadecimal), `d` (integer)
* **Precision:** `.2f` rounds floating-point numbers to 2 decimal places.

**Example:**
```python
n1, n2 = 4, 5
f"{n1} * {n2} = {(n1 * n2):.2f}" # Yields: '4 * 5 = 20.00'
```

---

## 6.7. Files & File I/O

### Memory Concepts
* **RAM (Volatile):** Fast memory used while programs execute. Data disappears when programs terminate or systems restart.
* **Storage (Non-Volatile):** Hard drives, SSDs, USB drives. Stores named blocks of data called **files**.

### The `open()` Function
```python
file_object = open(filename, mode)
```

| Mode | Name | Description |
| :---: | :--- | :--- |
| `'r'` | Read | Default. Opens file for reading. Raises error if file doesn't exist. |
| `'w'` | Write | Creates new file or **overwrites/truncates** existing file. |
| `'a'` | Append | Writes new data to the **end** of the existing file contents. |

### File Operations Example
```python
# Writing
myfile = open('test.txt', 'w')
myfile.write('Hello, world!\n') # Returns character count written
myfile.close()

# Reading
myfile = open('test.txt', 'r')
contents = myfile.read()
myfile.close()
```

---

## 6.8. Exception Handling (`try...except`)

Opening a non-existent file in read mode causes a runtime exception (`FileNotFoundError`).

```python
try:
    f = open('thefile.txt', 'r')
    mydata = f.read()
    f.close()
except FileNotFoundError:
    mydata = '' # Fallback handling
```

---

## 6.9. Methods for Reading Files

1. **`read()`:** Reads the entire file content as a single string.
2. **`readline()`:** Reads one line at a time, including the trailing newline (`\n`). Returns an empty string `''` when reaching the End of File (EOF).
3. **`readlines()`:** Reads all lines into a **list of strings**.

### Reading Line-by-Line (Pattern)
```python
f = open('test.txt', 'r')
while True:
    theline = f.readline()
    if len(theline) == 0: # EOF reached
        break
    print(theline, end='') # Suppress extra newline
f.close()
```

### Filtering File Content
Filters process line-by-line while skipping unwanted entries:
```python
infile = open('input.txt', 'r')
outfile = open('output.txt', 'w')

while True:
    text = infile.readline()
    if len(text) == 0:
        break
    if text[0] == '#': # Skip comments
        continue
    outfile.write(text)

infile.close()
outfile.close()
```

---

## 6.10. `repr()` and `eval()` Functions

* **`repr(obj)`:** Returns the string representation of a Python object.
* **`eval(str)`:** Evaluates a string containing Python code/literals and converts it back into an actual Python object.

```python
mylist = [1, 2, 'buckle', 'my', 'shoe']
s = repr(mylist) # "[1, 2, 'buckle', 'my', 'shoe']" (Type: str)
recreated = eval(s) # [1, 2, 'buckle', 'my', 'shoe'] (Type: list)
```

---

## 6.11. & 6.12. Modules

### Definition
A **module** is a file containing Python code (definitions and statements) meant to be reused across different scripts. Filenames end in `.py`.

### Importing Modules
Suppose a module `seqtools.py` defines `remove_at(pos, seq)`:

1. **Selective Import:**
   ```python
   from seqtools import remove_at
   remove_at(4, "A string!")
   ```
2. **Module Import (Recommended to avoid namespace conflicts):**
   ```python
   import seqtools
   seqtools.remove_at(4, "A string!")
   ```
*Note: Do not include `.py` in the `import` statement.*

---

## 6.13. Namespaces

* A **namespace** is an isolated container ensuring variable names in one scope do not conflict with identical names in another scope.
* **Module Namespaces:** Each module maintains its own namespace accessed via dot notation (`module1.answer` vs `module2.answer`).
* **Function Namespaces:** Local variables inside functions operate within isolated scopes.

```python
def f():
    n = 7 # Local to f()

def g():
    n = 42 # Local to g()

n = 11 # Global scope
```

---

## 6.14. Attributes and the Dot Operator

* Variables and functions defined inside a module are **attributes** of that module.
* Attributes are accessed using the **dot operator (`.`)**:
  ```python
  import string
  string.capitalize('maryland') # Yields: 'Maryland'
  string.capwords("what's all this?") # Yields: "What's All This?"
  ```