import os
import sys
import random


all_words = list()
repeats = list()

with open("all_words", "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            all_words.append(word.lower())

for word in all_words:
    if all_words.count(word) > 1:
        repeats.append(word + ', ' + str(all_words.count(word)) + ' \n')
        for repeat in range(all_words.count(word)-1):
            all_words.remove(word)

random.shuffle(all_words)

list_len = int(sys.argv[1])

num_files = (len(all_words) // list_len) + 1
file_number = 0

for file in range(num_files):
    file_name = 'filtered_shuffled' + str(file_number)
    for word in all_words[list_len*file_number : list_len*(file_number+1)]:
        os.system("echo " + word + " >> " + file_name)
    file_number += 1
