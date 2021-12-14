## Instructions

1. The main.py is called when starting the program.
    * It initializes and passes files_object, slicer_object, handler_object and ui to the main-method. 
    * rawtext-variable gets the lines read from given filepath. It is passed along with handler-object to the ui-objects start-method. 
2. ui.py is a simple text-based user interface. First it asks the user to input desired Markov chain level (1-3). 
    * Here handler-object will create trie-datastructure (depth = markov chain level + 1) and input read lines into it. 
    * After this it gives weight to words according to their frequency in the read file. 
3. Secondly ui asks the user to input desired length of generated quote. 
4. Lastly it asks for 1-3 (Markov level) lower case words to begin the to be generated quote with. 
    * First word is capitalized by the program and period is added to the end of the created quote. 
5. Now the quote is generated and printed.
    * If no following words are found during generation of the quote, generating will end there and the quote will be shorter than given length.
7. Here the code will loop back and ask the user to give desired length of generated quote and starting words again. 
8. Empty string ends execution. 
