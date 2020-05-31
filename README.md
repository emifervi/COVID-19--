# COVID-19--
Lenguaje imperativo diseñado para la clase de compiladores.

# Development

## Compile Grammar:
`$ antlr4 -o antlr -Dlanguage=Python3 Covid.g4`

## Dependencies:
- `pip3 install pandas`
- `pip3 install matplotlib`

# Compiling Covid-19--

## Run:
`$ python3 Covid.py filename.cov`

## Flags:
 - `-d prints directory info for debugging`
 - `-q prints quadruples for debugging`

 # Documentation

## Program structure
- Program Header
- Global var declaration
- Function declarations
- Main

## Program header:
Must be first thing in the file.
```
program NameOfProgram;
```

## Declaring variables:
Can only be declared either as global after the programID or local in the function declaration.
```
var int i,j,k; float f;
```
Supported data types:
- int
- float
- char
- string
- arrays (only for atomic types, ie. not dataframe)
- dataframe

## Function declaration:
Must be declared before main function, there is no polymorphism so function names must be unique.
```
func int fibonacci(int param);
var j; //variable for local scope
{
    ....
    return (result); //returns must be wrapped in parens
}
```
## Expressions:
```
x = 2 * (12 + x) >= a;
```
Language supports:
- Arithmetic operations (+, -, *, /)
- Compare and equality (>, <, >=, <=, ==, !=)
- Logical operations (&&, ||, !)
- Parenthesis for nested expressions

## For-loop declaration:
For loop initialization must take a numeric constant. However, upper limit can be an expression, as long as it evaluates to a numeric result.
```
for i = 0 to limit {
    ...
}
```
## While-loop declaration:
```
i = 0
while(i < 10) {
    ...
    i = i + 1;
}
```
## If-Else statements:
Single condition:
```
if (cond) {
    ...
}
```
if-else
```
if (cond) {
    ...
}
else {
    ...
}
```
Nested
```
if (cond) {
    ...
}
else {
    if (cond2) {
        ...
    }
    else {
        ...
    }
}
```
## Read from console:
Variable must be declared previously, and should receive value of the type which was delcared originally.
```
input(var);
```
## Print to console:
Its possible to chain multiple string constants and expressions. 
```
print(var, " ", func(), "\n");
```
## Dataframe declaration:
There can only be one dataframe per program
```
dataframe data;
```

## Load dataframe file:
The file must be `.csv` format. It can use relative paths to access it.
```
load_file("data.csv");
```
## Load dataframe data:
Loads the data into the dataframe and overwrites rows and cols arguments with dimensions for dataframe.

Arguments:
- 1st argument: must be a dataframe
- 2nd argument: must be an int
- 3rd argument must be an int
```
load_data(data, rows, cols);
```
## Dataframe operations:
Returns the operation value for a given key.

Possible operations:
- Mean: `avg()`
- Max: `max()`
- Min: `min()`
- Range: `range()`
- Variance: `variance()`
- Std Deviation: `std_dev()`
- Mode: `mode()`

Arguments:
- 1st argument: must a dataframe
- 2nd argument: must be a string which represents a variable in dataframe
```
avg(data, "key");
```
## Dataframe correlation:
Returns correlation value for two keys
```
correl(data, "key1", "key2");
```
## Plot with dataframe:
Scatter plot for two variable in the dataframe, pops up in new window
```
plot(data, "key1", "key2");
```
### Result:
![ScatterPlot](https://i.imgur.com/7tbYaaN.jpg "Scatter Plot Result")
## Histogram with dataframe:
Histogram for a variable in the dataframe, the third argument is the number of bins for the histogram.

Plot pops up in new window.
```
hist(data, "key1", 10);
```
### Result:
![Histogram](https://i.imgur.com/GEfeNAg.jpg "Histogram Result")

## Main declaration:
```
main();
var i; //variable for local scope
{
    ...
}
```

# Code Examples
Check [ExampleFiles](https://github.com/emifervi/COVID-19--/tree/master/ExampleFiles) folder in repo.

# More Documentation
For more documentation, check [Documentation](https://github.com/emifervi/COVID-19--/tree/master/Documentation.pdf).
