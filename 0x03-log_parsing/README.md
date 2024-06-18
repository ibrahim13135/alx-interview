### Input and Output in Python

Python offers a variety of ways to handle input and output operations. This guide will cover advanced output formatting and file operations, providing detailed explanations and examples.

#### 7.1 Fancier Output Formatting

##### Printing Values

Python provides several methods to print values, including:
1. **Expression statements**: Directly typing expressions.
2. **print() function**: Using `print()` to display output.
3. **write() method**: Writing to file objects.

##### Formatted String Literals (f-strings)

**f-strings** allow embedding expressions inside string literals using curly braces `{}`.

Example:
```python
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')
# Output: Results of the 2016 Referendum
```

##### str.format() Method

The `str.format()` method allows for more detailed formatting using `{}` placeholders.

Example:
```python
yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))
# Output:  42572654 YES votes  49.67%
```

##### String Slicing and Concatenation

For complete control, you can use string slicing and concatenation.

Example:
```python
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
# Output: The value of x is 32.5, and y is 40000...
```

##### repr() vs. str()

- **str()**: Returns a human-readable string representation.
- **repr()**: Returns a string that can be read by the interpreter.

Example:
```python
s = 'Hello, world.'
print(str(s))  # Output: Hello, world.
print(repr(s))  # Output: 'Hello, world.'
```

##### Template Strings

The `string` module’s `Template` class allows for substitution using `$`.

Example:
```python
from string import Template
t = Template('Hello, $name!')
print(t.substitute(name='John'))
# Output: Hello, John!
```

### 7.1.1 Formatted String Literals

Formatted string literals (f-strings) are prefixed with `f` and use `{}` for expressions.

Example:
```python
import math
print(f'The value of pi is approximately {math.pi:.3f}.')
# Output: The value of pi is approximately 3.142.
```

##### Aligning Text

Specify a minimum width for fields:
```python
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
# Output:
# Sjoerd     ==>       4127
# Jack       ==>       4098
# Dcab       ==>       7678
```

##### Using Modifiers

Use `!a`, `!s`, and `!r` for `ascii()`, `str()`, and `repr()` respectively.

Example:
```python
animals = 'eels'
print(f'My hovercraft is full of {animals!r}.')
# Output: My hovercraft is full of 'eels'.
```

##### Self-Documenting Expressions

The `=` specifier expands expressions:
```python
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')
# Output: Debugging bugs='roaches' count=13 area='living room'
```

### 7.1.2 The String format() Method

The `str.format()` method uses `{}` to replace variables.

Example:
```python
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# Output: We are the knights who say "Ni!"
```

##### Positional and Keyword Arguments

Refer to arguments by position or keyword.

Example:
```python
print('{0} and {1}'.format('spam', 'eggs'))
# Output: spam and eggs
print('{1} and {0}'.format('spam', 'eggs'))
# Output: eggs and spam
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
# Output: This spam is absolutely horrible.
```

##### Using Dictionaries

Access dictionary values with `[]` or `**`.

Example:
```python
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# Output: Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

### 7.1.3 Manual String Formatting

Use string methods for custom formatting.

Example:

**Code:**
```python
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))
```
**Explanation:**

This code uses a `for` loop to iterate over the numbers from 1 to 10 (inclusive). For each iteration, it prints three values: `x`, `x*x`, and `x*x*x`. Here's what's happening in each iteration:

1. `print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')`:
	* `repr(x)` converts the integer `x` to a string representation.
	* `.rjust(2)` right-justifies the string in a field of width 2. This means that the string will be padded with spaces on the left to occupy a minimum of 2 characters.
	* `repr(x*x)` converts the result of `x*x` to a string representation.
	* `.rjust(3)` right-justifies the string in a field of width 3.
	* `end=' '` sets the separator between the two print statements to a space character. This means that the next `print` statement will start printing from the same line, separated by a space.
2. `print(repr(x*x*x).rjust(4))`:
	* `repr(x*x*x)` converts the result of `x*x*x` to a string representation.
	* `.rjust(4)` right-justifies the string in a field of width 4.
	* Since there's no `end=' '` argument, this `print` statement will start a new line.

**Output:**
The output will be a table with three columns, where each row represents the values of `x`, `x*x`, and `x*x*x` for a particular `x` value. The columns will be right-justified with the specified widths.

Here's a sample output:
```
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```
Note that the exact output may vary depending on the Python interpreter and its version.

### 7.1.4 Old String Formatting

The `%` operator can also be used for string formatting.

Example:
```python
import math
print('The value of pi is approximately %5.3f.' % math.pi)
# Output: The value of pi is approximately 3.142.
```

### 7.2 Reading and Writing Files

Python provides the `open()` function to handle file operations. The mode argument specifies how the file is to be opened.

Example:
```python
f = open('workfile', 'w', encoding='utf-8')
```

##### Modes

- `'r'`: Read (default).
- `'w'`: Write (truncate).
- `'a'`: Append.
- `'r+'`: Read and write.

##### Text and Binary Modes

- Text mode: Default, reads and writes strings.
- Binary mode: Reads and writes bytes (`'b'`).

##### Using with Statement

The `with` statement ensures proper file closure.

Example:
```python
with open('workfile', encoding='utf-8') as f:
    read_data = f.read()
```

##### File Methods

- `f.read(size)`: Reads up to `size` bytes.
- `f.readline()`: Reads a single line.
- `f.write(string)`: Writes `string` to the file.
- `f.tell()`: Returns the current file position.
- `f.seek(offset, whence)`: Moves the file pointer.

Example:
```python
f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5)
print(f.read(1))  # Output: b'5'
f.seek(-3, 2)
print(f.read(1))  # Output: b'd'
```


**Lines 1-2:**
```python
f = open('workfile', 'rb+')
```
Here, we're opening a file called `workfile` in binary read-write mode (`'rb+'`). The `+` sign indicates that we want to open the file for both reading and writing. If the file doesn't exist, it will be created.

**Lines 3-4:**
```python
f.write(b'hello i am hima')
```
We write a byte string (`b'hello i am hima'`) to the file. The `b` prefix indicates a byte string literal.

**Line 5:**
```python
f.seek(5)
```
We move the file pointer to the 5th byte (0-indexed) in the file using the `seek()` method. This means we're positioning the file pointer at the 6th character (`'o'`) in the string "hello i am hima".

**Line 6:**
```python
print(f.read(1))
```
We read a single byte (1 byte) from the file using the `read()` method. Since the file pointer is at the 5th byte, we read the 6th byte (`'o'`). The `print()` function outputs the read byte as a byte string (`b'o'`).

**Line 7:**
```python
f.seek(-3, 2)
```
We move the file pointer to the 3rd byte from the end of the file using the `seek()` method with the `whence` argument set to `2` (SEEK_END). This means we're positioning the file pointer at the 3rd byte from the end of the file.

**Line 8:**
```python
print(f.read(1))
```
We read a single byte (1 byte) from the file using the `read()` method. Since the file pointer is at the 3rd byte from the end, we read the 3rd byte from the end (`'m'`). The `print()` function outputs the read byte as a byte string (`b'm'`).

In summary, this code:

1. Opens a file in binary read-write mode.
2. Writes a byte string to the file.
3. Moves the file pointer to the 5th byte and reads a single byte (`'o'`).
4. Moves the file pointer to the 3rd byte from the end of the file and reads a single byte (`'m'`).

The output of this code would be:
```
b'o'
b'm'
```


### 7.2.2 Saving Structured Data with JSON

Python’s `json` module can serialize and deserialize data.


# Serializing data:
Example:
```python
import json
x = [1, 'simple', 'list']
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(x, f)
```

# Deserializing data:
```python
with open('data.json', 'r', encoding='utf-8') as f:
    x = json.load(f)
```

The given Python code demonstrates how to serialize and deserialize data using the `json` module. Here’s a step-by-step explanation:

### Serializing Data
Serialization is the process of converting a Python object into a JSON formatted string.

1. **Import the `json` module**:
   ```python
   import json
   ```
   The `json` module is used to work with JSON data.

2. **Define a Python object**:
   ```python
   x = [1, 'simple', 'list']
   ```
   Here, `x` is a list containing an integer and two strings.

3. **Open a file in write mode**:
   ```python
   with open('data.json', 'w', encoding='utf-8') as f:
   ```
   This line opens a file named `data.json` in write mode (`'w'`). The `encoding='utf-8'` argument ensures the file is encoded in UTF-8.

4. **Serialize the Python object and write it to the file**:
   ```python
   json.dump(x, f)
   ```
   The `json.dump(x, f)` function converts the Python object `x` to a JSON formatted string and writes it to the file `f`.

Putting it together, the serialization code looks like this:
```python
import json

x = [1, 'simple', 'list']
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(x, f)
```

### Deserializing Data
Deserialization is the process of converting a JSON formatted string back into a Python object.

1. **Open the file in read mode**:
   ```python
   with open('data.json', 'r', encoding='utf-8') as f:
   ```
   This line opens the file `data.json` in read mode (`'r'`).

2. **Deserialize the JSON data into a Python object**:
   ```python
   x = json.load(f)
   ```
   The `json.load(f)` function reads the JSON formatted string from the file `f` and converts it back into a Python object. In this case, the list `[1, 'simple', 'list']`.

Putting it together, the deserialization code looks like this:
```python
with open('data.json', 'r', encoding='utf-8') as f:
    x = json.load(f)
```

### Summary
- **Serialization**: Convert a Python object into a JSON string and write it to a file.
- **Deserialization**: Read a JSON string from a file and convert it back into a Python object.

By using these methods, you can easily save Python objects to a file in JSON format and later read them back into your program.



This comprehensive guide covers advanced output formatting and file handling in Python, providing the necessary tools for effective data processing and presentation.



----

### signal — Set handlers for asynchronous events¶


The `signal` module in Python provides mechanisms to handle asynchronous events through signal handlers. This module is particularly useful for setting up custom behavior when the operating system sends signals to a Python program. Here are the key points and functionalities provided by the `signal` module:

### General Rules
- **Default Handlers**: By default, `SIGPIPE` is ignored and `SIGINT` is converted to a `KeyboardInterrupt` exception.
- **Custom Handlers**: You can set custom handlers for signals using `signal.signal()`.
- **Handler Persistence**: Once set, handlers persist until explicitly reset, except for `SIGCHLD`, which follows the system’s behavior.
- **Platform Differences**: On WebAssembly platforms (e.g., wasm32-emscripten), signals are emulated and behave differently.

### Execution of Signal Handlers
- **Deferred Execution**: Python signal handlers execute after the low-level signal handler sets a flag, which the virtual machine checks at a later point.
- **Synchronous Errors**: Signals like `SIGFPE` or `SIGSEGV` are generally not useful to catch because they result in immediate re-raising of the signal.
- **Long-running C Code**: Python signal handlers won't execute during long-running C code; they will only be called after the C code finishes.

### Signals and Threads
- **Main Thread**: Signal handlers are always executed in the main Python thread of the main interpreter.
- **Thread Communication**: Signals are not suitable for inter-thread communication. Use synchronization primitives from the `threading` module instead.

### Module Contents
- **Enums**: The module defines three enums:
  - `signal.Signals`: Collection of `SIG*` constants.
  - `signal.Handlers`: Contains `SIG_DFL` and `SIG_IGN`.
  - `signal.Sigmasks`: Contains `SIG_BLOCK`, `SIG_UNBLOCK`, and `SIG_SETMASK`.

### Commonly Used Signals
- `SIGABRT`, `SIGALRM`, `SIGBUS`, `SIGCHLD`, `SIGCONT`, `SIGHUP`, `SIGILL`, `SIGINT`, `SIGKILL`, `SIGPIPE`, `SIGSEGV`, `SIGTERM`, `SIGUSR1`, `SIGUSR2`, etc.

### Functions
- **alarm(time)**: Schedules a `SIGALRM` signal after `time` seconds.
- **getsignal(signalnum)**: Returns the current signal handler for `signalnum`.
- **pause()**: Suspends the process until a signal is received.
- **raise_signal(signum)**: Sends a signal to the calling process.
- **pthread_kill(thread_id, signalnum)**: Sends a signal to a specific thread.
- **setitimer(which, seconds, interval=0.0)**: Sets an interval timer.
- **getitimer(which)**: Returns the current value of an interval timer.
- **siginterrupt(signalnum, flag)**: Changes system call restart behavior.
- **signal(signalnum, handler)**: Sets the signal handler for `signalnum`.
- **sigpending()**: Returns the set of pending signals.
- **sigwait(sigset)**: Suspends execution until a specified signal is received.
- **sigwaitinfo(sigset)**: Suspends execution and returns information about the signal.
- **sigtimedwait(sigset, timeout)**: Like `sigwaitinfo()`, but with a timeout.


#### 1. `alarm(time)`
Schedules a `SIGALRM` signal to be sent to the process after a specified number of seconds.

**Example**:
```python
import signal
import time

def handler(signum, frame):
    print("Alarm received!")

signal.signal(signal.SIGALRM, handler)
signal.alarm(5)  # Alarm in 5 seconds
time.sleep(10)  # Wait to receive the alarm
```

#### 2. `getsignal(signalnum)`
Returns the current signal handler for `signalnum`.

**Example**:
```python
import signal

handler = signal.getsignal(signal.SIGALRM)
print(handler)
```

#### 3. `pause()`
Suspends the process until a signal is received.

**Example**:
```python
import signal
import os

def handler(signum, frame):
    print("Signal received, continuing execution")

signal.signal(signal.SIGUSR1, handler)
print("Pausing until signal is received...")
os.kill(os.getpid(), signal.SIGUSR1)  # Send signal to itself
signal.pause()
```

#### 4. `raise_signal(signum)`
Sends a signal to the calling process.

**Example**:
```python
import signal

def handler(signum, frame):
    print("Signal received!")

signal.signal(signal.SIGUSR1, handler)
signal.raise_signal(signal.SIGUSR1)
```

#### 5. `pthread_kill(thread_id, signalnum)`
Sends a signal to a specific thread.

**Example**:
```python
import signal
import threading

def handler(signum, frame):
    print("Signal received in thread!")

def thread_function():
    signal.signal(signal.SIGUSR1, handler)
    signal.pause()

thread = threading.Thread(target=thread_function)
thread.start()
signal.pthread_kill(thread.ident, signal.SIGUSR1)
thread.join()
```

#### 6. `setitimer(which, seconds, interval=0.0)`
Sets an interval timer.

**Example**:
```python
import signal

def handler(signum, frame):
    print("Timer signal received!")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 2, 1)  # First alarm in 2 sec, then every 1 sec
signal.pause()
```

#### 7. `getitimer(which)`
Returns the current value of an interval timer.

**Example**:
```python
import signal

signal.setitimer(signal.ITIMER_REAL, 2, 1)
remaining, interval = signal.getitimer(signal.ITIMER_REAL)
print(f"Remaining: {remaining}, Interval: {interval}")
```

#### 8. `siginterrupt(signalnum, flag)`
Changes system call restart behavior.

**Example**:
```python
import signal

signal.siginterrupt(signal.SIGALRM, True)
```

#### 9. `signal(signalnum, handler)`
Sets the signal handler for `signalnum`.

**Example**:
```python
import signal

def handler(signum, frame):
    print("Signal received!")

signal.signal(signal.SIGUSR1, handler)
```

#### 10. `sigpending()`
Returns the set of pending signals.

**Example**:
```python
import signal
import os

signal.raise_signal(signal.SIGUSR1)
pending = signal.sigpending()
print(pending)
```

#### 11. `sigwait(sigset)`
Suspends execution until a specified signal is received.

**Example**:
```python
import signal

sigset = {signal.SIGUSR1}
print("Waiting for signal...")
signal.sigwait(sigset)
print("Signal received!")
```

#### 12. `sigwaitinfo(sigset)`
Suspends execution and returns information about the signal.

**Example**:
```python
import signal

sigset = {signal.SIGUSR1}
print("Waiting for signal info...")
info = signal.sigwaitinfo(sigset)
print("Signal received!", info)
```

#### 13. `sigtimedwait(sigset, timeout)`
Like `sigwaitinfo()`, but with a timeout.

**Example**:
```python
import signal

sigset = {signal.SIGUSR1}
print("Waiting for signal info with timeout...")
info = signal.sigtimedwait(sigset, 5)  # Timeout after 5 seconds
if info is None:
    print("Timeout, no signal received.")
else:
    print("Signal received!", info)
```



- **Timeout with Alarm**: Example of using `signal.alarm()` to avoid hanging operations.
```python
import signal, os

def handler(signum, frame):
    print(f'Signal handler called with signal {signum}')
    raise OSError("Couldn't open device!")

signal.signal(signal.SIGALRM, handler)
signal.alarm(5)
fd = os.open('/dev/ttyS0', os.O_RDWR)
signal.alarm(0)
```
- **Handling Broken Pipes**: Example to handle `BrokenPipeError` when piping output to tools like `head`.
```python
import os
import sys

def main():
    try:
        for x in range(10000):
            print("y")
        sys.stdout.flush()
    except BrokenPipeError:
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        sys.exit(1)

if __name__ == '__main__':
    main()
```
- **Custom SIGINT Handler**: Example of an HTTP server with a custom `SIGINT` handler.
```python
import signal
import socket
from selectors import DefaultSelector, EVENT_READ
from http.server import HTTPServer, SimpleHTTPRequestHandler

interrupt_read, interrupt_write = socket.socketpair()

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    interrupt_write.send(b'\0')

signal.signal(signal.SIGINT, handler)

def serve_forever(httpd):
    sel = DefaultSelector()
    sel.register(interrupt_read, EVENT_READ)
    sel.register(httpd, EVENT_READ)
    while True:
        for key, _ in sel.select():
            if key.fileobj == interrupt_read:
                interrupt_read.recv(1)
                return
            if key.fileobj == httpd:
                httpd.handle_request()

httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
serve_forever(httpd)
print("Shutdown...")
```

### Notes
- **SIGPIPE Handling**: Wrapping the main function to handle `BrokenPipeError` gracefully.
- **Exceptions from Handlers**: Raising exceptions from signal handlers can leave the program in an unexpected state. It's advisable to handle such situations carefully, especially in complex applications.

The `signal` module provides powerful tools for handling asynchronous events, making it crucial for writing robust and responsive Python applications that interact closely with the underlying operating system.




----------



Certainly! Here is a combined summary that captures the essence of the content on signal handling in Python and data processing:

---

### Python Signal Handling

Python provides a mechanism for handling asynchronous events through the `signal` module. This module allows custom handlers to be defined for specific signals using the `signal.signal()` function. Some signals have default handlers, such as `SIGPIPE` (ignored) and `SIGINT` (raises `KeyboardInterrupt`).

#### Key Points:
1. **Handler Execution**: Python signal handlers are not executed inside the low-level C signal handler. Instead, the C signal handler sets a flag, causing the Python handler to be executed later (e.g., at the next bytecode instruction).
2. **Synchronous Errors**: Catching synchronous errors like `SIGFPE` or `SIGSEGV` is not effective, as the handler will return control to the C code, potentially causing the signal to be raised again.
3. **Long-Running C Calculations**: Python signal handlers might not be executed during lengthy C operations until the operation completes.
4. **Main Thread Execution**: Signal handlers run in the main Python thread, even if the signal was received in another thread, and only the main thread can set new handlers.

#### Module Contents:
- **Enumerations**: `Signals`, `Handlers`, `Sigmasks`.
- **Functions**: Various functions for setting handlers, sending signals, managing signal masks, and dealing with timers (e.g., `signal.alarm()`, `signal.signal()`, `signal.pause()`).
- **Special Signals**: Constants for different signals (e.g., `SIGINT`, `SIGTERM`), special handler values (`SIG_DFL`, `SIG_IGN`), and platform-specific signals (`CTRL_C_EVENT` on Windows).

#### Examples:
- Setting a signal handler to handle timeouts using `alarm()`.
- Handling `BrokenPipeError` when writing to pipes.
- Implementing custom SIGINT handling for a graceful shutdown.

### Data Processing

Data processing often involves tasks such as parsing strings to extract specific data points and aggregating data to compute summaries.

#### Key Tasks:
1. **Parsing Strings**: Extracting specific data points from strings using regular expressions, string manipulation functions, or dedicated parsing libraries.
2. **Data Aggregation**: Computing summaries and aggregations such as sums, averages, counts, or more complex statistical metrics. This often involves iterating over data collections and applying aggregation functions.

---

This summary integrates the key concepts of signal handling in Python with an overview of common data processing tasks, giving a comprehensive view of both topics.


----


# re — Regular expression operations¶



### Lookbehind Assertions
- **Positive Lookbehind `(?<=...)`**: Matches if the current position in the string is preceded by a match for the pattern inside the parentheses.
  ```python
  import re
  m = re.search('(?<=abc)def', 'abcdef')
  print(m.group(0))  # Output: 'def'
  
  m = re.search(r'(?<=-)\w+', 'spam-egg')
  print(m.group(0))  # Output: 'egg'
  ```
- **Negative Lookbehind `(?<!...)`**: Matches if the current position in the string is not preceded by a match for the pattern inside the parentheses.

### Conditional Patterns
- **Conditional Pattern `(?(id/name)yes-pattern|no-pattern)`**: Matches `yes-pattern` if the group with the given `id` or `name` exists, and `no-pattern` if it doesn’t.
  ```python
  pattern = r'(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)'
  m = re.match(pattern, '<user@host.com>')
  print(m.group(0))  # Output: '<user@host.com>'
  ```

### Special Sequences
- **`\number`**: Matches the contents of the group of the same number.
  ```python
  m = re.match(r'(.+)\1', 'the the')
  print(m.group(0))  # Output: 'the the'
  ```
- **`\A`**: Matches only at the start of the string.
- **`\b`**: Matches the empty string at the beginning or end of a word.
  ```python
  m = re.search(r'\bat\b', 'as at ay')
  print(m.group(0))  # Output: 'at'
  ```
- **`\B`**: Matches the empty string not at the beginning or end of a word.
  ```python
  m = re.search(r'at\B', 'atom')
  print(m.group(0))  # Output: 'at'
  ```
- **`\d`**: Matches any Unicode decimal digit.
- **`\D`**: Matches any character which is not a decimal digit.
- **`\s`**: Matches Unicode whitespace characters.
- **`\S`**: Matches any character which is not a whitespace character.
- **`\w`**: Matches Unicode word characters (alphanumeric + underscore).
- **`\W`**: Matches any character which is not a word character.
- **`\Z`**: Matches only at the end of the string.

### Flags
- **`re.ASCII`**: ASCII-only matching for `\w`, `\W`, `\b`, `\B`, `\d`, `\D`, `\s`, `\S`.
- **`re.DEBUG`**: Display debug information about compiled expression.
- **`re.IGNORECASE`**: Case-insensitive matching.
- **`re.LOCALE`**: Locale-aware matching for `\w`, `\W`, `\b`, `\B`.
- **`re.MULTILINE`**: `^` and `$` match the start and end of each line.
- **`re.DOTALL`**: `.` matches any character, including a newline.
- **`re.UNICODE`**: Unicode matching (default in Python 3).
- **`re.VERBOSE`**: Allows whitespace and comments within the pattern for readability.

### Example Usage
```python
import re

# Using lookbehind assertion
pattern = r'(?<=abc)def'
string = 'abcdef'
m = re.search(pattern, string)
print(m.group(0))  # Output: 'def'

# Using conditional pattern
pattern = r'(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)'
string = '<user@host.com>'
m = re.match(pattern, string)
print(m.group(0))  # Output: '<user@host.com>'

# Using special sequences
pattern = r'\bword\b'
string = 'a word in a sentence'
m = re.search(pattern, string)
print(m.group(0))  # Output: 'word'

# Using flags
pattern = r'(?i)abc'
string = 'ABC'
m = re.search(pattern, string)
print(m.group(0))  # Output: 'ABC'
```

This summary covers the essential aspects of regex in Python, including lookbehind assertions, conditional patterns, special sequences, and flags. These tools are powerful for text processing and pattern matching tasks.



### `re` Module Functions

#### `re.compile(pattern, flags=0)`
- **Purpose**: Compiles a regular expression pattern into a regular expression object, which can be used for matching.
- **Usage**: 
  ```python
  prog = re.compile(pattern)
  result = prog.match(string)
  ```
- **Efficiency**: Using `re.compile()` is more efficient than using `re.match()` directly when the same pattern will be used multiple times.
- **Flags**: Modify the pattern’s behavior, e.g., `re.IGNORECASE`.

#### `re.search(pattern, string, flags=0)`
- **Purpose**: Scans through a string looking for the first location where the pattern matches.
- **Returns**: A match object if found, otherwise `None`.

#### `re.match(pattern, string, flags=0)`
- **Purpose**: Checks if the beginning of the string matches the pattern.
- **Returns**: A match object if the pattern matches from the start, otherwise `None`.
- **Note**: For matching anywhere in the string, use `re.search()`.

#### `re.fullmatch(pattern, string, flags=0)`
- **Purpose**: Checks if the entire string matches the pattern.
- **Returns**: A match object if the entire string matches, otherwise `None`.

#### `re.split(pattern, string, maxsplit=0, flags=0)`
- **Purpose**: Splits the string by the occurrences of the pattern.
- **Returns**: A list of substrings.
- **Example**:
  ```python
  re.split(r'\W+', 'Words, words, words.')
  # Output: ['Words', 'words', 'words', '']
  ```

#### `re.findall(pattern, string, flags=0)`
- **Purpose**: Returns all non-overlapping matches of the pattern in the string.
- **Returns**: A list of strings or tuples, depending on capturing groups.
- **Example**:
  ```python
  re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
  # Output: ['foot', 'fell', 'fastest']
  ```

#### `re.finditer(pattern, string, flags=0)`
- **Purpose**: Returns an iterator yielding match objects for all non-overlapping matches.
- **Usage**: Useful for iterating over matches.

#### `re.sub(pattern, repl, string, count=0, flags=0)`
- **Purpose**: Replaces occurrences of the pattern in the string with `repl`.
- **Returns**: The new string with replacements.
- **Example**:
  ```python
  re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)
  # Output: 'Baked Beans & Spam'
  ```

#### `re.subn(pattern, repl, string, count=0, flags=0)`
- **Purpose**: Same as `re.sub()`, but also returns the number of substitutions made.
- **Returns**: A tuple `(new_string, number_of_subs_made)`.

#### `re.escape(pattern)`
- **Purpose**: Escapes all non-alphanumeric characters in the pattern.
- **Example**:
  ```python
  re.escape('https://www.python.org')
  # Output: 'https://www\\.python\\.org'
  ```

#### `re.purge()`
- **Purpose**: Clears the regular expression cache.

### Exceptions

#### `re.error`
- **Purpose**: Raised when there’s an error in the regular expression compilation or matching.
- **Attributes**: `msg`, `pattern`, `pos`, `lineno`, `colno`.

### Regular Expression Objects (`re.Pattern`)

- **Created by**: `re.compile()`
- **Methods**:
  - `search(string[, pos[, endpos]])`: Like `re.search()`.
  - `match(string[, pos[, endpos]])`: Like `re.match()`.
  - `fullmatch(string[, pos[, endpos]])`: Like `re.fullmatch()`.
  - `split(string, maxsplit=0)`: Like `re.split()`.
  - `findall(string[, pos[, endpos]])`: Like `re.findall()`.
  - `finditer(string[, pos[, endpos]])`: Like `re.finditer()`.
  - `sub(repl, string, count=0)`: Like `re.sub()`.
  - `subn(repl, string, count=0)`: Like `re.subn()`.
- **Attributes**:
  - `flags`: The regex matching flags.
  - `groups`: The number of capturing groups.
  - `groupindex`: A dictionary mapping group names to group numbers.
  - `pattern`: The original pattern string.

### Match Objects (`re.Match`)

- **Created by**: Successful `match()`, `search()`, etc.
- **Methods**:
  - `expand(template)`: Returns the expanded version of the template.
  - `group([group1, ...])`: Returns one or more groups of the match.
  - `__getitem__(g)`: Equivalent to `m.group(g)`.
  - `groups(default=None)`: Returns a tuple of all groups.
  - `groupdict(default=None)`: Returns a dictionary of all named groups.
  - `start([group])`: Returns the start index of the group.
  - `end([group])`: Returns the end index of the group.
  - `span([group])`: Returns a tuple of the start and end indices of the group.
- **Attributes**:
  - `pos`: The start position passed to `search()` or `match()`.
  - `endpos`: The end position passed to `search()` or `match()`.
  - `lastindex`: The index of the last matched capturing group.
  - `lastgroup`: The name of the last matched capturing group.
  - `re`: The regex object.
  - `string`: The string passed to `search()` or `match()`.



### Group Matching and Retrieval
- **`group(g)`**: Returns the substring matched by the group with index `g`.
- **`group(0)`**: Returns the entire matched string.
- **`group(name)`**: Returns the substring matched by the named group with the given `name`.
- **`groups(default=None)`**: Returns a tuple containing all the subgroups of the match.
- **`groupdict(default=None)`**: Returns a dictionary containing all the named subgroups of the match.

### Match Position and Span
- **`start(group)`**: Returns the index of the start of the substring matched by the group with index `group`.
- **`end(group)`**: Returns the index of the end of the substring matched by the group with index `group`.
- **`span(group)`**: Returns a tuple `(start, end)` indicating the span of the substring matched by the group with index `group`.

### Match Metadata
- **`pos`**: The index into the string where the search for the match started.
- **`endpos`**: The index into the string beyond which the search for the match did not extend.
- **`lastindex`**: The index of the last matched capturing group.
- **`lastgroup`**: The name of the last matched capturing group.
- **`re`**: The regular expression object that produced this match.
- **`string`**: The string that the match was performed on.

### Other
- **`copy`**: Match objects are considered atomic and can be copied using `copy.copy()` and `copy.deepcopy()`.

### Example Usage
```python
import re

# Group matching
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(m.group(0))  # Output: 'Isaac Newton'
print(m.group(1))  # Output: 'Isaac'
print(m.group(2))  # Output: 'Newton'
print(m.group('first_name'))  # Output: 'Isaac'
print(m.group('last_name'))  # Output: 'Newton'

# Group position and span
print(m.start(0))  # Output: 0
print(m.end(0))  # Output: 12
print(m.span(0))  # Output: (0, 12)

# Match metadata
print(m.pos)  # Output: 0
print(m.endpos)  # Output: 30
print(m.lastindex)  # Output: 2
print(m.lastgroup)  # Output: 'last_name'
print(m.re.pattern)  # Output: '(\w+) (\w+)'
print(m.string)  # Output: 'Isaac Newton, physicist'
```

This additional information provides a comprehensive overview of match objects in Python's regex module and how to utilize their attributes effectively.




### Summary

The `re` module in Python provides a powerful and flexible tool for performing regex-based operations. Compiling patterns with `re.compile()` can improve efficiency for repeated use. Methods like `search()`, `match()`, `fullmatch()`, `split()`, `findall()`, `finditer()`, `sub()`, and `subn()` cover a wide range of string matching and manipulation needs. Understanding these methods and their options, such as flags and capturing groups, is crucial for effectively utilizing regular expressions in Python.






----



### Regular Expression Examples

#### Checking for a Pair

In this example, we'll use a helper function to display match objects more gracefully:

```python
def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())
```

Suppose you are writing a poker program where a player’s hand is represented as a 5-character string with each character representing a card, where:
- "a" for ace
- "k" for king
- "q" for queen
- "j" for jack
- "t" for 10
- "2" through "9" representing the card with that value.

To see if a given string is a valid hand:

```python
import re

valid = re.compile(r"^[a2-9tjqk]{5}$")
print(displaymatch(valid.match("akt5q")))  # Valid
# "<Match: 'akt5q', groups=()>"
print(displaymatch(valid.match("akt5e")))  # Invalid
print(displaymatch(valid.match("akt")))    # Invalid
print(displaymatch(valid.match("727ak")))  # Valid
# "<Match: '727ak', groups=()>"
```

To check if a hand contains a pair, you can use backreferences:

```python
pair = re.compile(r".*(.).*\1")
print(displaymatch(pair.match("717ak")))     # Pair of 7s
# "<Match: '717', groups=('7',)>"
print(displaymatch(pair.match("718ak")))     # No pairs
print(displaymatch(pair.match("354aa")))     # Pair of aces
# "<Match: '354aa', groups=('a',)>"
```

To find out what card the pair consists of:

```python
pair = re.compile(r".*(.).*\1")
print(pair.match("717ak").group(1))  # '7'

# Error because re.match() returns None, which doesn't have a group() method:
pair.match("718ak").group(1)  # AttributeError: 'NoneType' object has no attribute 'group'

print(pair.match("354aa").group(1))  # 'a'
```

#### Simulating `scanf()`

Python doesn't have a direct equivalent to `scanf()`. Regular expressions are more powerful but also more verbose. Here are some equivalent mappings:

| `scanf()` Token | Regular Expression                |
|-----------------|-----------------------------------|
| `%c`            | `.`                               |
| `%5c`           | `.{5}`                            |
| `%d`            | `[-+]?\d+`                        |
| `%e`, `%E`, `%f`, `%g` | `[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?` |
| `%i`            | `[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)` |
| `%o`            | `[-+]?[0-7]+`                     |
| `%s`            | `\S+`                             |
| `%u`            | `\d+`                             |
| `%x`, `%X`      | `[-+]?(0[xX])?[\dA-Fa-f]+`        |

For example, to extract the filename and numbers from a string like `/usr/sbin/sendmail - 0 errors, 4 warnings`, the equivalent regular expression would be:

```python
import re

pattern = re.compile(r"(\S+) - (\d+) errors, (\d+) warnings")
text = "/usr/sbin/sendmail - 0 errors, 4 warnings"
print(pattern.findall(text))
# [('usr/sbin/sendmail', '0', '4')]
```

#### `search()` vs. `match()`

- `re.match()` checks for a match only at the beginning of the string.
- `re.search()` checks for a match anywhere in the string.
- `re.fullmatch()` checks if the entire string matches.

Examples:

```python
print(re.match("c", "abcdef"))    # No match
print(re.search("c", "abcdef"))   # Match
# <re.Match object; span=(2, 3), match='c'>
print(re.fullmatch("p.*n", "python")) # Match
# <re.Match object; span=(0, 6), match='python'>
print(re.fullmatch("r.*n", "python")) # No match
```

Regular expressions beginning with '^' can be used with `search()` to restrict the match to the beginning of the string:

```python
print(re.match("c", "abcdef"))    # No match
print(re.search("^c", "abcdef"))  # No match
print(re.search("^a", "abcdef"))  # Match
# <re.Match object; span=(0, 1), match='a'>
```

In `MULTILINE` mode, `match()` only matches at the beginning of the string, whereas using `search()` with `^` will match at the beginning of each line:

```python
print(re.match("X", "A\nB\nX", re.MULTILINE))  # No match
print(re.search("^X", "A\nB\nX", re.MULTILINE))  # Match
# <re.Match object; span=(4, 5), match='X'>
```

#### Making a Phonebook

To split a string into a list of entries:

```python
text = """Ross McFluff: 834.345.1254 155 Elm Street

Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way


Heather Albrecht: 548.326.4584 919 Park Place"""
entries = re.split("\n+", text)
print(entries)
# ['Ross McFluff: 834.345.1254 155 Elm Street', 'Ronald Heathmore: 892.345.3428 436 Finley Avenue', 'Frank Burger: 925.541.7625 662 South Dogwood Way', 'Heather Albrecht: 548.326.4584 919 Park Place']
```

To split each entry into a list with first name, last name, telephone number, and address:

```python
entries = re.split("\n+", text)
results = [re.split(":? ", entry, 3) for entry in entries]
print(results)
# [['Ross', 'McFluff', '834.345.1254', '155 Elm Street'], ['Ronald', 'Heathmore', '892.345.3428', '436 Finley Avenue'], ['Frank', 'Burger', '925.541.7625', '662 South Dogwood Way'], ['Heather', 'Albrecht', '548.326.4584', '919 Park Place']]
```

With a `maxsplit` of 4, to separate the house number from the street name:

```python
results = [re.split(":? ", entry, 4) for entry in entries]
print(results)
# [['Ross', 'McFluff', '834.345.1254', '155', 'Elm Street'], ['Ronald', 'Heathmore', '892.345.3428', '436', 'Finley Avenue'], ['Frank', 'Burger', '925.541.7625', '662', 'South Dogwood Way'], ['Heather', 'Albrecht', '548.326.4584', '919', 'Park Place']]
```

#### Text Munging

`sub()` replaces every occurrence of a pattern with a string or the result of a function. For example, to randomize the order of characters in each word except for the first and last characters:

```python
import random
import re

def repl(m):
    inner_word = list(m.group(2))
    random.shuffle(inner_word)
    return m.group(1) + "".join(inner_word) + m.group(3)

text = "Professor Abdolmalek, please report your absences promptly."
result = re.sub(r"(\w)(\w+)(\w)", repl, text)
print(result)
# 'Poefsrosr Aealmlobdk, pslaee reorpt your abnseces plmrptoy.'
result = re.sub(r"(\w)(\w+)(\w)", repl, text)
print(result)
# 'Pofsroser Aodlambelk, plasee reoprt yuor asnebces potlmrpy.'
```

#### Finding all Adverbs

To find all occurrences of a pattern:

```python
text = "He was carefully disguised but captured quickly by police."
adverbs = re.findall(r"\w+ly\b", text)
print(adverbs)
# ['carefully', 'quickly']
```

#### Finding all Adverbs and their Positions

To find all matches and their positions:

```python
text = "He was carefully disguised but captured quickly by police."
for m in re.finditer(r"\w+ly\b", text):
    print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
# 07-16: carefully
# 40-47: quickly
```

#### Raw String Notation

Raw string notation (`r"text"`) keeps regular expressions sane. Without it, every backslash in a regular expression would have to be prefixed with another one to escape it. For example, the following lines of code are functionally identical:


In Python, when working with regular expressions, it's common to use raw string notation to avoid having to escape backslashes (`\`) in the regular expression pattern.

In regular expressions, the backslash (`\`) is used to escape special characters, so if you want to match a literal backslash, you need to escape it with another backslash. For example, to match a single backslash, you would use `\\` in a regular expression.

With raw string notation, you can use the `r` prefix before the string literal, like this: `r"\\"`. This allows you to write the regular expression pattern without having to escape the backslashes.

For example, the following two lines of code are equivalent:
```python
re.match(r"\W(.)\1\W", " ff ")
<re.Match object; span=(0, 4), match=' ff '>
re.match("\\W(.)\\1\\W", " ff ")
<re.Match object; span=(0, 4), match=' ff '>
```
The first line uses raw string notation, while the second line does not.

**Writing a Tokenizer**

A tokenizer (or scanner) is a program that breaks up a string of text into individual tokens, such as keywords, identifiers, numbers, and symbols. This is a crucial step in building a compiler or interpreter.

In this example, the tokenizer uses regular expressions to categorize groups of characters in the input string. The regular expressions are defined in the `token_specification` list, which includes patterns for:

* `NUMBER`: matches an integer or decimal number
* `ASSIGN`: matches the assignment operator (`:=`)
* `END`: matches the statement terminator (`;`)
* `ID`: matches an identifier (a sequence of letters)
* `OP`: matches an arithmetic operator (`+`, `-`, `*`, `/`)
* `NEWLINE`: matches a newline character (`\n`)
* `SKIP`: matches whitespace characters (spaces and tabs)
* `MISMATCH`: matches any other character

The `tokenize` function takes a string of code as input and uses the `re` module to iterate over the input string, matching each token using the regular expressions defined in `token_specification`. Each match is yielded as a `Token` object, which contains the token type, value, line number, and column number.

The example code demonstrates how to use the tokenizer to parse a simple programming language. The input code is:
```python
from typing import NamedTuple
import re

class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int

def tokenize(code):
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_specification = [
        ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN',   r':='),           # Assignment operator
        ('END',      r';'),            # Statement terminator
        ('ID',       r'[A-Za-z]+'),    # Identifiers
        ('OP',       r'[+\-*/]'),      # Arithmetic operators
        ('NEWLINE',  r'\n'),           # Line endings
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH', r'.'),            # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value in keywords:
            kind = value
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        yield Token(kind, value, line_num, column)

statements = '''
    IF quantity THEN
        total := total + price * quantity;
        tax := price * 0.05;
    ENDIF;
'''

for token in tokenize(statements):
    print(token)
```
The tokenizer breaks this code into individual tokens, which are printed to the console:
```
Token(type='IF', value='IF', line=2, column=4)
Token(type='ID', value='quantity', line=2, column=7)
Token(type='THEN', value='THEN', line=2, column=16)
Token(type='ID', value='total', line=3, column=8)
Token(type='ASSIGN', value=':=', line=3, column=14)
Token(type='ID', value='total', line=3, column=17)
Token(type='OP', value='+', line=3, column=23)
Token(type='ID', value='price', line=3, column=25)
Token(type='OP', value='*', line=3, column=31)
Token(type='ID', value='quantity', line=3, column=33)
Token(type='END', value=';', line=3, column=41)
Token(type='ID', value='tax', line=4, column=8)
Token(type='ASSIGN', value=':=', line=4, column=12)
Token(type='ID', value='price', line=4, column=15)
Token(type='OP', value='*', line=4, column=21)
Token(type='NUMBER', value=0.05, line=4, column=23)
Token(type='END', value=';', line=4, column=27)
Token(type='ENDIF', value='ENDIF', line=5, column=4)
Token(type='END', value=';', line=5, column=9)
...
```
Each token is categorized based on its type, value, line number, and column number.



----



### 5.5. Dictionaries

Dictionaries in Python are associative arrays where elements are accessed by keys rather than indices. Keys can be of any immutable type (such as strings or numbers). Tuples can also be used as keys if they only contain strings, numbers, or other tuples that are immutable. Lists cannot be used as keys because they are mutable.

#### Operations on Dictionaries:
- **Storing and accessing values:** Values are stored with keys and can be accessed using the key.
- **Adding and deleting entries:** New key-value pairs can be added, and existing pairs can be deleted using `del`.
- **Listing keys:** `list(d)` returns a list of all keys in insertion order, and `sorted(d)` returns keys in sorted order.
- **Checking for key existence:** The `in` keyword checks if a key exists in the dictionary.
  
#### Example:
```python
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
del tel['sape']
tel['irv'] = 4127
print(list(tel))        # ['jack', 'guido', 'irv']
print(sorted(tel))      # ['guido', 'irv', 'jack']
print('guido' in tel)   # True
print('jack' not in tel)   # False
```

#### Constructing Dictionaries:
Dictionaries can be constructed using the `dict()` constructor from a list of key-value pairs or using dictionary comprehensions for more complex mappings.

### 5.6. Looping Techniques

#### Iterating over Dictionary Items:
- **Using `items()` method:** Loop through key-value pairs simultaneously.

#### Example:
```python
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
# Output:
# gallahad the pure
# robin the brave
```

#### Enumerating Lists:
- **Using `enumerate()` function:** Loop through a sequence while keeping track of the index.

#### Example:
```python
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
# Output:
# 0 tic
# 1 tac
# 2 toe
```

#### Zipping Sequences:
- **Using `zip()` function:** Iterate over multiple sequences simultaneously.

#### Example:
```python
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
# Output:
# What is your name?  It is lancelot.
# What is your quest?  It is the holy grail.
# What is your favorite color?  It is blue.
```

#### Reversing and Sorting:
- **Reversing a sequence:** Use `reversed()` function.
- **Sorting a sequence:** Use `sorted()` function.

### Conclusion
This section of the Python documentation covers dictionaries as associative arrays and various techniques for looping over sequences and dictionaries efficiently. These techniques are essential for working with data structures and iterating through collections in Python.






----




### 8. Errors and Exceptions

#### 8.1. Syntax Errors
Syntax errors, also known as parsing errors, occur when the Python parser encounters invalid syntax. These are typically encountered while writing code and are highlighted by the interpreter:

Example:
```python
while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax
```
The error message includes the file name and line number where the error occurred, along with a visual indicator (`^`) pointing to the specific token causing the error.

#### 8.2. Exceptions
Exceptions occur during the execution of a program even if the syntax is correct. Python provides various built-in exceptions for different error conditions:

Examples:
```python
10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined

'2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```
Each exception type (`ZeroDivisionError`, `NameError`, `TypeError`, etc.) indicates a specific type of error encountered during execution. The error message provides details about the type of exception and the context where it occurred.

#### 8.3. Handling Exceptions
Python allows handling exceptions using the `try` statement. Code that might throw an exception is placed inside the `try` block, and the handling of specific exceptions is managed in `except` blocks:

Example:
```python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
```
In this example, `ValueError` is handled by printing a message and allowing the user to retry entering a valid number.

#### Multiple `except` Clauses and Exception Hierarchy
Python allows multiple `except` clauses to handle different types of exceptions. Exception classes can be specified in a tuple to handle multiple exception types:
```python
except (RuntimeError, TypeError, NameError):
    pass
```
Additionally, Python's exception handling supports inheritance, where an `except` clause can catch exceptions of a derived class:
```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```
This example demonstrates that when exceptions are caught, Python checks from the most specific (`D`) to the least specific (`B`) in the exception hierarchy.

#### `else` Clause in `try` Statements
Python's `try` statement also supports an `else` clause that executes if no exceptions are raised in the `try` block:
```python
try:
    # code that may raise exceptions
except SomeException:
    # exception handling
else:
    # executed if no exceptions are raised
```
This is useful for code that should only execute if the `try` block completes without exceptions.

#### Raising Exceptions (`raise` Statement)
The `raise` statement in Python is used to raise exceptions programmatically. It can raise built-in exceptions or custom exceptions derived from `Exception`:
```python
raise ValueError("Invalid value")
```
This example raises a `ValueError` with a custom error message.

#### Exception Chaining
Exceptions raised inside `except` blocks can be chained using the `from` clause:
```python
try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")
```
Here, `RuntimeError` is raised with the original `OSError` as the cause.

### 8.4. User-defined Exceptions
Python allows defining custom exceptions by creating a new exception class. Custom exceptions are typically derived from `Exception`:
```python
class CustomError(Exception):
    pass
```
Custom exceptions can have additional attributes and methods to provide more context about the error.






### 8.7. Defining Clean-up Actions

#### `finally` Clause
The `finally` clause in Python's `try` statement allows defining clean-up actions that must be executed under all circumstances, whether an exception occurs or not:
```python
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
```
Output:
```
Goodbye, world!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
```
In this example, `finally` ensures that 'Goodbye, world!' is printed before the program exits due to the `KeyboardInterrupt` exception.

#### Behavior of `finally` in Different Scenarios
- If an exception occurs during execution of the `try` block and is handled by an `except` block, the `finally` block still executes after the `except` block.
- If an exception occurs during execution of an `except` or `else` block, the `finally` block still executes after the `except` or `else` block.
- If the `finally` block contains `break`, `continue`, or `return` statements, exceptions are not re-raised.
- If the `try` block contains `break`, `continue`, or `return` statements, the `finally` block executes just before these statements take effect.
- If the `finally` block contains a `return` statement, the returned value overrides any value returned by the `try` block.

Example demonstrating the behavior of `finally`:
```python
def bool_return():
    try:
        return True
    finally:
        return False

print(bool_return())  # Output: False
```
In this example, the `finally` block's `return False` statement overrides the `return True` statement in the `try` block.

### 8.8. Predefined Clean-up Actions

#### Using `with` Statement for Clean-up
Python's `with` statement ensures that clean-up actions are performed after using certain objects (like files), regardless of whether the operation using the object succeeds or fails:
```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```
In this example, `open("myfile.txt")` ensures that the file handle `f` is properly closed after the `with` block, even if an error occurs while processing the file.

### 8.9. Raising and Handling Multiple Unrelated Exceptions

#### `ExceptionGroup` for Multiple Exceptions
Python provides `ExceptionGroup` to wrap and handle multiple unrelated exceptions together:
```python
def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)

try:
    f()
except Exception as e:
    print(f'caught {type(e)}: {e}')

# Output:
# caught <class 'ExceptionGroup'>: there were problems
#  +-+---------------- 1 ----------------
#    | OSError: error 1
#    +---------------- 2 ----------------
#    | SystemError: error 2
#    +------------------------------------
```
In this example, `ExceptionGroup` wraps a list of exceptions (`OSError` and `SystemError`) and allows handling them together.

#### Handling Specific Exceptions from `ExceptionGroup`
You can selectively handle exceptions from an `ExceptionGroup` using `except*` instead of `except`:
```python
try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")
```
This allows you to handle specific types of exceptions contained within the `ExceptionGroup`.

### 8.10. Enriching Exceptions with Notes

#### Adding Notes to Exceptions
Python exceptions can have additional context added using the `add_note()` method:
```python
try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
    raise
```
The added notes are included in the exception traceback when it is raised, providing additional context about the exception.

#### Practical Use of `add_note()`
Adding context information when collecting exceptions into an `ExceptionGroup`:
```python
def f():
    raise OSError('operation failed')

excs = []
for i in range(3):
    try:
        f()
    except Exception as e:
        e.add_note(f'Happened in Iteration {i+1}')
        excs.append(e)

raise ExceptionGroup('We have some problems', excs)
```
In this example, each exception in `excs` has a note indicating the iteration number when the exception occurred.

These sections illustrate Python's robust exception handling mechanisms, including how to ensure resource cleanup, handle multiple exceptions, and enrich exceptions with additional context. Understanding these concepts helps in writing more resilient and maintainable Python code.





### Conclusion
Understanding errors and exceptions in Python is crucial for writing robust and reliable code. Python's exception handling mechanism allows developers to gracefully manage errors and control program flow in the face of unexpected conditions. This makes Python programs more resilient and easier to debug.
