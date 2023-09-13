"""
You are given an array of words where each word consists of lowercase English letters.
wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the
order of the other characters to make it equal to wordB.
For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2,
word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.
Return the length of the longest possible word chain with words chosen from the given list of words.
________________________________________________________________________________________________________________________
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
________________________________________________________________________________________________________________________
Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
________________________________________________________________________________________________________________________
Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
#=======================================LEARNINGS=======================================================================
Don't always think of what question is asking, try thinking of it's reverse, like for the above case, instead of adding
one character from it, try removing one character from the longest string.
****************************************INTUTION************************************************************************
Approach 1: Top-Down Dynamic Programming (Recursion + Memoization)
Intuition


Here we work backwards to find the longest chain, this means that we will start from a word and delete one character at
a time. We continue this chain until we come across a word that is not present in the list or is one letter long.
Notice that a particular sequence can be a part of more than one word sequence. For example the sequence ab -> b is part
of both the following sequences : abcd -> abd -> ab -> b and abcd -> abc -> ab -> b. This leads to repeated calculations
because every time we encounter ab we need to explore the subpath ab -> a. For a small list, this is not a problem but
as the size of the list increases, the size of the graph grows exponentially.
What we can do is whenever we encounter a new word, we will find all possible sequences with this word as the last word
in the sequence. Then, we will store the length of the longest possible sequence that ends with this word.
We will use a map for this where each key will be an ending word and the value will be the length of the longest possible
 word sequence ending with this word.
#++++++++++++++++++++++++++++++++++++++ALGORITHM++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Algorithm
Initialize a set (wordsPresent) and add all the words in the list to the set. This set will be used to check if a word
is present in the list.
Initialize a map (memo) having key type as String and value type as Integer. This map will store the length of the longest
possible word sequence where the key is the last word in the sequence.
Iterate over the list. For each word in the list perform a depth-first search.
In the DFS, consider the current word (currentWord) as the last word in the word sequence.
If currentWord was encountered previously we just return its corresponding value in the map memo.
Initialize maxLength to 1.
Iterate over the entire length of the currentWord.
Create all possible words (newWord) by taking out one character at a time.
If newWord is present in the set perform a DFS with this word and store the intermediate result in a variable currentLength.
Update the maxLength so that it contains the length of the longest sequence possible where the currentWord is the end word.
Set the maxLength as the value for currentWord (key) in the map.
Return maxLength.
"""

words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]


def longestStrChain(words):
    memoization = dict()
    words_set = set(words)
    result = 0
    def rec_func(word):

        print("---------------RECURSION ENTERED-------------")
        print("word------------->", word)
        print("memoization------>", memoization)
        if memoization.get(word, None) is not None:
            return memoization[word]
        max_length = 1


        for i in range(len(word)):
            subsequence = word[:i] + word[i+1:]
            if subsequence in words_set:
                curr_length = 1 + rec_func(subsequence)
                max_length = max(max_length , curr_length)
                print("subsequence-------->", subsequence)

        memoization[word] = max_length
        print("max length------------->", max_length)
        print("-----------------RECURSION EXITED-------------")
        return max_length

    for word in sorted(words, key=lambda x: len(x), reverse= True):
        result = max(result, rec_func(word))
    return result



print(longestStrChain(words))