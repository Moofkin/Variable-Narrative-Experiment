README

This program was created by Lauren Cunningham and Joseph Bernay as an 
experiment in variable narratives and generative texts.

It is designed around Gungho's Puzzle and Dragons. The purpose is to
create a generative, variable text using data extracted from the 
Puzzle and Dragons database, http://puzzledragonx.com .

In order to do so, text data is stored from two random monsters' pages
on the database, and is then parsed and categorized by parts of speech.
These words are then used in an attempt to create sentences.

Initially, there was also a web-crawler that went to the database and 
retrieved the necessary data, however, this was not included due to
portability issues. Instead, multiple examples of the extractor's output
(named "monsterX.txt") were included.

------------------------------------------------------------------------
How to Use:

1) Install Python 3.4
2) Install NLTK (Python's Natural Language Toolkit)
3) Run the Program.

------------------------------------------------------------------------
Switching Files:

In order to switch between the included files, certain lines of code
must be changed. These are lines:

499) file = open("monster1.txt", 'r', errors='ignore')
524) file = open("monster2.txt", 'r', errors='ignore')

In order to swap the files out, simply change the "monster1.txt" and
"monster2.txt" fields to match one of the other included files.