# Week 4 report
## Tasks done
I reworked the trie class into a two leveled one. \
The previous one pretty much only stored the quotes and had no way of being creative when it iterated deeper into the tree and tried to generate unique quote. \
The updated trie stores all words in the root level and word following them to the second level. \
The second level nodes are different from the root-level ones and thus have different occurence-values then their root-level counterparts. \
This is logical as all occurences of a word are not followed by any one unique word. \
This rework of course destroyed methods and tests I had previoisly done. \
The quality of code took also a hit as things are still WIP. \
This week has been stressful because of this major rework of the code. \
Much of the work I did this week is not seen in the code as it became obsolete after this update.

## What I learned
I understood the way in which storing words is more efficient from the perspective of generating more creative quotes. \
I used a ton of Regex to clean my much larger source data for the generator before I moved on to implement this update of trie. That was educational.

## Going forward
Next up is the implementation of the 2nd level Markov chain. There I will store two words into one node and see what word follows those. \
The prerequisite to this is that other aspects of my broken code are working. If it is not, that will become the main goal of next week.


Used hours: 8.
