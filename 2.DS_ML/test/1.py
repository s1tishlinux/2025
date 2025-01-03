

"""Program to print all duplicate character and their count. For example if given String is "Programming" then your program should print g : 2 r : 2 m : 2"""

from collections import Counter
def find_dupplicate_characters(input_string):
    #Count frequency of each character
    char_count = Counter(input_string)

    duplicates = {}
    for char, count in char_count.items():
        if count > 1:
            duplicates[char] = count


    
    for char, count in duplicates.items():
        print(f"{char}: {count}")
    
input_string = "Programming"
find_dupplicate_characters(input_string)

"""You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
	
	NOTE: String letters are case-sensitive.
	
	Input Format
	The first line of input contains the original string. The next line contains the substring.
	
	Output Format
	Output the integer number indicating the total number of occurrences of the substring in the original string.
	
	Sample Input
	ABCDCDC
	CDC
	
	Sample Output
	2"""


def count_subsring_occurences(original_string, substring):
    count = 0
    start = 0


    