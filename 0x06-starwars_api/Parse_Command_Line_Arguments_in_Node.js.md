### How to Parse Command Line Arguments in Node.js

#### Using `process.argv`

Node.js inherently supports handling command-line arguments through `process.argv`, which is an array containing the command-line arguments passed when the Node.js process was launched.

**Example: Using `process.argv`**

```javascript
// File: app.js

// Accessing command-line arguments using process.argv
console.log(process.argv);

// Parsing specific arguments
const args = process.argv.slice(2); // First two elements are node executable and script file path
console.log("Arguments:", args);
```

**Explanation**:
- `process.argv`: Provides an array where the first element is the path to Node.js executable and the second element is the path to the JavaScript file being executed. Subsequent elements are the command-line arguments.
- `.slice(2)`: Removes the first two elements (`node` and script path), leaving only the actual command-line arguments.

**Output**:
```
$ node app.js arg1 arg2 arg3
[ 'node', '/path/to/app.js', 'arg1', 'arg2', 'arg3' ]
Arguments: [ 'arg1', 'arg2', 'arg3' ]
```

#### Using `yargs`

`yargs` is a popular npm package that provides a more sophisticated way to parse command-line arguments with options and commands, offering built-in help support and more.

**Example: Using `yargs`**

Install `yargs`:
```
npm install yargs
```

```javascript
// File: app-yargs.js

const yargs = require('yargs');

// Parsing command-line arguments using yargs
const argv = yargs.argv;
console.log("Yargs Arguments:", argv._); // _ property contains positional arguments
```

**Explanation**:
- `yargs.argv`: Parses and provides access to the command-line arguments in an object format.
- `argv._`: Contains positional arguments passed after options.

**Output**:
```
$ node app-yargs.js --option value positional1 positional2
Yargs Arguments: [ 'positional1', 'positional2' ]
```

#### Using `minimist`

`minimist` is another npm package for parsing command-line arguments in a minimalistic way, focusing on simplicity and ease of use.

**Example: Using `minimist`**

Install `minimist`:
```
npm install minimist
```

```javascript
// File: app-minimist.js

const argv = require('minimist')(process.argv.slice(2));

// Accessing parsed arguments using minimist
console.log("Minimist Arguments:", argv._); // _ property contains positional arguments
```

**Explanation**:
- `require('minimist')(process.argv.slice(2))`: Initializes `minimist` with command-line arguments, excluding the first two (`node` and script path).
- `argv._`: Contains positional arguments.

**Output**:
```
$ node app-minimist.js --option value positional1 positional2
Minimist Arguments: [ 'positional1', 'positional2' ]
```

### Summary

- **`process.argv`**: Default Node.js way to access command-line arguments, simple but requires manual parsing.
- **`yargs`**: Provides a more feature-rich and structured way to parse arguments, supporting options, commands, and automatic help generation.
- **`minimist`**: Lightweight alternative to `yargs`, focusing on simplicity and ease of use for basic argument parsing.

These examples illustrate different approaches to parsing command-line arguments in Node.js, catering to various needs from basic to more complex argument handling scenarios. Each method offers its own set of advantages depending on the requirements of your Node.js application.
