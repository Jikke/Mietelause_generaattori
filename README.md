# Quote generator
The goal of this project is to create a creative quote generator using Markov chain. \
It is coded with Python using Poetry for dependency management.

## Weekly reports
[Week 1](https://github.com/Jikke/Quote_generator/blob/main/documentation/week1.md) \
[Week 2](https://github.com/Jikke/Quote_generator/blob/main/documentation/week2.md) \
[Week 3](https://github.com/Jikke/Quote_generator/blob/main/documentation/week3.md) \
[Week 4](https://github.com/Jikke/Quote_generator/blob/main/documentation/week4.md) \
[Week 5](https://github.com/Jikke/Quote_generator/tree/main/documentation/week5.md) \
[Week 6](https://github.com/Jikke/Quote_generator/tree/main/documentation/week6.md)

## Documentation

[Definition](https://github.com/Jikke/Quote_generator/edit/main/documentation/definition.md) \
[Instructions](https://github.com/Jikke/Quote_generator/blob/main/documentation/instructions.md) \
[Implementation](https://github.com/Jikke/Quote_generator/blob/main/documentation/implementation.md)

## Usage of the program

### General information

The program has over 50 000 lines of sentences in a .txt file which it uses as data to create the trie-datastructure. \
This data is used to generate "creative" sentences, sometimes even quotes according to other input the user gives, which are
* Level of Markov chain (1-3)
* Desired length of generated quote (4-15 words) 
* Desired beginning words of the generated quote (Given Markov chain level determines the amount) \
The length of generated quote might be less than desired if the program is not able to find following words at any given point during generation. \
The Markov chain level is capped at 3 because the higher the level is, the less options the generator has to make creative choices. \
On the other hand, the lower the level is, the more illegible the output is. \
Markov chain level 2 gave most satisfying outputs during my testing. \
In depth instructions [here](https://github.com/Jikke/Quote_generator/blob/main/documentation/instructions.md).


### Executing the program

After cloning the repository to local directory, Poetry depencies must be installed with command
```
    poetry install
```
Otherwise the program might not work as intended. Afterwards Poetry virtual environment can be created with
```
    poetry shell
```
Within the virtual environment the program can be executed with command
```
    invoke start
```
or
```
    python3 src/main.py
```
### Running unittests

Unittest can be executed with command
```
	invoke coverage
```	
and coverage report created with
```
	invoke coverage-report
```	
The generated report is saved in path ./htmlcov/index.html and can be checked with any browser in use. Here is example for Google Chrome
```
	google-chrome htmlcov/index.html
```	
