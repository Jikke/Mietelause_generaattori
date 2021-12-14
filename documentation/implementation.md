# Implementation document

## Structure of the code
The program needs the folllowing classes for execution:
* main.py
* ui.py
* files.py
* slicer.py
* trienode.py
* trie.py
* handler.py 

Data used in creating trie-datastructure is stored in either 
* src/data/quotes_archive.txt 
* src/data/quotes_dataset_one_column_copy.txt \
At the moment the latter is used as it has over 50 000 sentences.

## Design of the trie-datastructure

The trie.py uses trienode.py classes objects. \
Trienode is simple class. It has no methods and only three fields:
* stored word as String
* children nodes of this node as dictionary: keys are String of the word, values are the actual trienodes
* occurences has the amount of times this node appears in this triepath. Value when constructed is 1. \
Trie-class has one field and two methods:
* root-field has the root trienode of the trie-datastructure which is named '\*'. It has no children when constructed.
* add_sentence takes sentence to be added and level of Markov chain as parameters. It slices the sentence into Markov-level length pieces and passes them to
* add_words, which actually stores the words as trienodes to the trie-datastructure. For new words new nodes are created, recurring ones add occurence-value to the corresponding trienode. 

## Big-O notation analysis

### Time complexity when storing data

Storing sentences to the trie-datastructure uses following methods:
1. Hanlder-classes crunch_sentences, which loops through all of the lines (n) in the given file. (O(n))
    * First it calls for slicer-classes slice_to_word_list-method which loops through all the words (m) in the given line, lowers capitalization and removes dots and returns word-list.
    * The previous step is not neccessary as I could just make the data used clean from the get go. This is why I will skip this step in the complexity analysis.
2. Secondly, it adds the created word-list into the trie-datastructure using add_sentence-method. It loops through all the words. (O(n\*m))
    * This loops through the sentence using add_words method to add the amount of words given in Markov-level (l) parameter at a time.
    * Because the Markov-level (l) is a number 1-3 it is a known constant and will not affect the time complexity. \
Therefore the time complexity of storing data from file to this trie-datastructure is **O(n\*m)** \
where *n* is the amount of lines in the read file and *m* the amount of words in each line. 

### Time complexity when creating quote

This is retrieving data from the trie-datastructure with some extra steps:
1. Handler-class uses the create_quote which begins at the root of the trie-datastructure
    * It loops as many times as the given quote length argument says (constant 4-15)
    * Before picking word, the possibilities must be weighted using weighted_words-method \
     which loops through the children (n) of the current trienode. O(n)
2. For this analysis, the following library imported random-method is instant \
Therefore the time complexity of creating the quote is **O(n)** \
where *n* is the amount of children of the current node. 

### Space complexity of the stored data

When storing a sentence to the trie-datastruture, a single word of it appears from 1 to the depth of *d* (Markov level + 1 = 2 to 4) amount of times in the trie. \
Therefore longer sentences require only O(1) more space to be stored. However, this is a worst case scenario. The sentence may have recurring words which are stored by modifying already existing nodes' \_occurence -fields from one integer to another. \
Considering all arguments above, storing *n* words to the trie-datastructure takes maximum of O(d\*n) space. As we know, *d* has value of 2 to 4 so its space complexity is O(1). Because of this it can be seen as insignificant in this analysis. \
In conclusion the space complexity of this datastructure is **O(n)** where *n* is the amount of stored words (nodes). 

## Ideas for follow-up develpoment

There's much room for improvement in this project. The following list is definitely not exhaustive:
* Cleaner text file for quote generation. (There's still some non-char keys and conjoined words there.)
* GUI
* Graphical presentation of the trie-datastructure
* More modifiability for the user
    * Using own textfile to create trie
    * More options if quote ends before desired length of words (continue anyway, start over, etc.)
    * Possibility to modify propabilities of less common words to be picked
* Smarter quote ending (exclamation marks, question marks)

## Sources
* [Wikipedia: Trie](https://en.wikipedia.org/wiki/Trie)
* [wikipedia: Markov Chain](https://en.wikipedia.org/wiki/Markov_chain)
* The project page of this course

