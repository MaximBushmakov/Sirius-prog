**Warning!**

In this program there are crutches on crutches and some unusable function. There some functions and many tests are not done.

To use this code you should create new file with input data and run from_file([input file path], [output file path]). 

In file with input you should write commands and values as input data to execute theese commands. There are 3 commands: 'alphabet', 'scheme' and 'tests'. 

Command 'alphabet' sets new alphabet. After it there is 1 line with symbols without whitespaces and dots (it's alphabet).

Command 'scheme' sets new scheme. After it there are some lines with substitutions, any of which has 2 words, splitted by whitespace, and before 2nd there may be dot, what shows that it is final substitution.

Command 'run' run algorithm. After it there are some lines with words, from which algorithm will run. Results will be written into file with path [output file path] or with path './ouput.txt' if it wasn't destignate.

If there is wrong alphabet, scheme or input, program will write 'wrong input' and after finishing all errors will write into console.
