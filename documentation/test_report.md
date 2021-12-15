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
 
## Correctness tests

Rather than testing this program with quantitative performance test, the testing was focused on qualitative aspects. The main purpose was to find out if it generates quotes and stores data as intended. \
These tests were run manually. The data was gathered from multiple executions of the code with variety of parameters.
The correctness of this project is analysed from following viewpoints:
* Are sentences self-generated? 
* May understandable sentences be generated?
* Are following words picked according to the given Markov Chain level?
* At which Markov Chain level does the generator begin to imitate sentences from the data file?

### Test results

The most interesting findings appeared at Markov chain levels 2-4. Anything lower (and even at 2) was pretty much gibberish. Higher levels usually generated only copies of the given sentences in the data file.

#### Parameters:  4, 20, "the"

"The root cause of all evil in the world comes from us bothering with each other."

Original ended "-- the root cause of all evil in the world.", but was succesfully followed up with "-- evil in the world comes from us bothering with each other --" by the program.

Many understandable sentences, but pretty much every one of them are copied from the data file.
Most of the sentences cannot reach the desired length as following words are hard to come by if starting words are picked from the end of a data file sentence.

#### Parameters:  3, 14, "a"

"A moving sea between the shores of lake michigan."

Original ended "-- a moving sea between the shores of your souls .", but was succesfully followed up with "-- on the shores of Lake Michigan."

Even if the following quote didn't reach desired length, it is pretty much understandable.
"A tragedy if you’re still alive."

Still understandable, but is mostly copied from the data file.
Seems to be easier to deliver quotes that are of the desired length than at Markov Chain levels 4 and higher.

#### Parameters:  3, 15, "the"

Again, not desired length but still interesting.
"The wind blows straight through because no one owns anyone."

#### Parameters:  2, 8, "it"

"It always will be something that god did."

Much harder to find understandable sentences at this level, but pretty much all of them are self-generated and of desired length.
