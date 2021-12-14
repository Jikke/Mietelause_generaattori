# Test report

##  Unittests

Unittests can be run with `invoke coverage` when the virtual environment is running. \
The relatively small amount of methods and classes made writing unittests for this program a breeze. I tried my best to keep the code clean and as simple as possible. \
ui.py and main.py are omitted from coverage as well as handler-classes method crunch_sentences() as it only uses other classes' methods. 

### Unittest coverage

Unittest coverage is 93%. \
![coverage_report](https://github.com/Jikke/Quote_generator/blob/main/documentation/Coverage_report.png?raw=true)

## User interface tests


User input calls are the places where the exectuion most likely will throw errors. \
The user interface of this program has three input calls which I have manually tested with the following kinds of inputs: 
1. Desired Markov chain level field:
    * Characters and words &#8594; `print("!Please input integer only!")`
    * Space &#8594; `print("!Please input integer only!")`
    * Integers over and under the proper range of 1 to 3 &#8594; `print("!Given Markov level wasn't 1-3!")`
    * Empty input &#8594; Ends execution as it should.
2. Desired quote length field:
    * Characters and words &#8594; `print("!Please input integer only!")`
    * Space &#8594; `print("!Please input integer only!")`
    * Integers over and under the proper range of 4 to 15 &#8594; `print("!Given length wasn't 4-15 words!")`
    * Empty input &#8594; Ends execution as it should
3. Field for desired starting words of the quote :
    * Non-characters and non-words &#8594; `print("There are no following words for the one(s) given.")`
    * Space &#8594; `print("There are no following words for the one(s) given.")` if Markov is 2 (input here is two empty "words") else `print(f"!Given amount of words wasn't {markov}!")`
    * Word amounts of over and under the Markov level &#8594; `print(f"!Given amount of words wasn't {markov}!")`
    * Empty input &#8594; Ends execution as it should.
 
 ## Performance tests
 
There is no dedicated performance test class or file. However, the amount of time it takes to create the trie-datastructure with given Markov chain level is calculated during each execution. This time is printed for the user to see. \
Having tested this multiple times with Markov levels of 1, 2 and 3 it seems, that the higher the level is the longer it takes to create the trie-datastructure.
These results more or less repeated themselves over time: \
![performance_tests](https://github.com/Jikke/Quote_generator/blob/main/documentation/performance_tests.png?raw=true)
