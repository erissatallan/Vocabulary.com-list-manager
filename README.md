# Vocabulary.com list manager

Vocabulary.com is the most popular vocabulary trainer on the internet among learners of the English language and logophiles alike. Learners can create and curate lists of words to learn on their accounts. However, when lists become lengthy, there are two challenges:
    1. it is not easy to tell whether one has already included a word in one of their lists
    2. one desires a more randomized practice routine than the order in which they input the words.
This python script offers a solution to both challenges.

Furthermore, valuable statistics like the number of times a word has been repeated (indicating the relative difficulty in learning that word) will be generated when the script is executed.

Another useful feature is the automated creation of randomized lists of the user's desired length.

## Execution
The user pastes all the words from their vocab lists into the text file called 'all_words.'
The script is run as follows
    python vocab_filter.py 500
where 500 is the desired length of the lists. Text files named 'filtered_shuffled0', 'filtered_shuffled1' and so on will be generated in the same directory as the python script. Additionally, a file named 'ascending_hf_repeats' will contain the repeated words in descending order, where the rank is the frequency of repeat.
