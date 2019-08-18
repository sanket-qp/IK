"""
You are given a dictionary set dictionary that contains dictionaryCount distinct words and another string txt.
Your task is to segment the txt string in such a way that all the segments occur in a continuous manner in the original
txt string and all these segments (or words) exists in our dictionary set dictionary.

In short you have to split the string txt using ' ' (single white space delimiter) in such a
way that every segment exists in our dictionary

Example: word = 'catsanddog', d = {'cat', 'cats', 'sand', 'and', 'dog'}
expected output = ['cat sand dog', 'cats and dog']


DP Approach:
    Let's say DP(i) is all possible word breaks of the given word from 0 to i
    if we have some possible words at index 2 i.e DP(2) and substring from (3, 6) is also in a dictionary
        then DP(6) can be extended by appending substr(3, 6) after every word break in DP(2)

    Example, W = 'catsanddog' D = {'cat', 'cats', 'sand', 'and', 'dog'}
    DP[0] = []
    DP[1] = []
    DP[2] = ['cat'] substr (0, 2) is in dict and there are no words formed at index 1 i.e DP(1) is empty
                    so we can't extend this substr at DP(2)
    DP[3] = ['cats'] substr(0, 3) is in dict
    DP[4] = [] (0, 4) = catsa, (1, 4) = atsa and so on .... none of the splits will be in dictionary
    DP[5] = [] (0, 5) = catsan, (1, 5) = atsan and so on .... none of the splits will be in dictionary
    DP[6] =
            (0, 6) catsand
            (1, 6) atsand
            (2, 6) tsand
            (3, 6) sand is in dict, There are also possible words at DP(2) so this substr (3, 6) can be extended
            DP[6] = append substr(3, 6) for each word break in DP[2]

            = ['cat sand']

            (4, 6) and is also in dict, There are also possible words at DP(3) so this substr(4, 6) can be extended
            DP[6] = append substr(4, 6) for each word break in DP[3]

            = ['cat sand', 'cats and']

            (5, 6) nd
            (6, 6) d
    DP[7] = [] (0, 7) = catsandd,  (1, 7) = atsandd and so on .... none of the split will be in dictionary
    DP[8] = [] (0, 8) = catsanddo, (1, 8) = atsanddo and so on .... none of the split will be in dictionary
    DP[9] =
            (0, 9) = catsanddog
            (1, 9) = atsanddog
            (2, 9) = tsanddog
            (3, 9) = sanddog
            (4, 9) = anddog
            (5, 9) = nddog
            (6, 9) = ddog
            (7, 9) = dog is in dict, There are also possible words at DP(6) so this substr (7, 9) can be extended
            DP[9] = append substr(7, 9) for each word break in DP[6]
            = ['cat sand dog', 'cats and dog']

Reference:
    https://leetcode.com/problems/word-break-ii/discuss/194615/DP-solution-with-detailed-text-and-video-explanation
"""


def __word_break(word, dictionary, start, taken, result):
    if start == len(word):
        result.append(" ".join(taken))

    for idx in range(start, len(word) + 1):
        initial_split = word[start:idx]
        if initial_split in dictionary:
            taken.append(initial_split)
            __word_break(word, dictionary, idx, taken, result)
            taken.pop()


def word_break_recursive(word, dictionary):
    result = []
    taken = []
    __word_break(word, dictionary, 0, taken, result)
    ## print "result", result
    return result


def word_break_DP(word, dictionary):
    dp_table = [[] for _ in range(len(word))]
    for i in range(0, len(word)):
        for j in range(0, i + 1):
            sub_str = word[j:i + 1]
            if sub_str in dictionary:
                # check if we have any words from 0 to j-1  i.e dp_table[j-1]
                # and append this substr j to i after each of the previous segments
                if j == 0:
                    dp_table[i].append(sub_str)
                else:
                    for word_break in dp_table[j - 1]:
                        dp_table[i].append("%s %s" % (word_break, sub_str))

    ## print dp_table2
    # i.e DP(L) will be all word breaks from 0 to L, where L is the length of the word
    return dp_table[-1]


def main():
    word = "totodo"
    d = {'to', 'do', 'todo'}
    result = word_break_recursive(word, d)
    assert ['to to do', 'to todo'] == result
    result_dp = word_break_DP(word, d)
    assert sorted(result) == sorted(result_dp)
    print "word: %s, dict: %s, word breaks: %s" % (word, d, result_dp)

    word = "catsanddog"
    d = {'cat', 'cats', 'and', 'sand', 'dog'}
    result = word_break_recursive(word, d)
    assert ['cat sand dog', 'cats and dog'] == result
    result_dp = word_break_DP(word, d)
    assert sorted(result) == sorted(result_dp)
    print "word: %s, dict: %s, word breaks: %s" % (word, d, result_dp)

    word = 'kickstartisawesome'
    d = {'kick', 'start', 'kickstart', 'is', 'awe', 'awesome', 'some'}
    result = word_break_recursive(word, d)
    expected = ['kick start is awe some', 'kick start is awesome', 'kickstart is awe some', 'kickstart is awesome']
    assert expected == result
    result_dp = word_break_DP(word, d)
    assert sorted(result) == sorted(result_dp)
    print "word: %s, dict: %s, word breaks: %s" % (word, d, result_dp)


if __name__ == '__main__':
    main()
