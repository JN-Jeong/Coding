"""
30. Substring with Concatenation of All Words
"""

from collections import defaultdict, deque
from typing import List, Optional


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])

        word_dict = defaultdict(int)
        for word in words:
            word_dict[word] += 1

        all_word_len = word_len * len(words)
        answer = []

        for i in range(word_len):
            q = deque()
            temp = word_dict.copy()
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j : j + word_len]
                print(i, word)
                if temp.get(word, 0) != 0:
                    temp[word] -= 1
                    q.append(word)

                    if sum(temp.values()) == 0:
                        answer.append(j - all_word_len + word_len)
                        last_word = q.popleft()
                        temp[last_word] = temp.get(last_word, 0) + 1

                else:
                    while q:
                        last_word = q.popleft()
                        if last_word == word:
                            q.append(word)
                            break
                        else:
                            temp[last_word] = temp.get(last_word, 0) + 1
                            if temp[last_word] > word_dict[last_word]:
                                temp = word_dict.copy()
                print("@", temp)

        return answer


if __name__ == "__main__":
    solution = Solution()
    s = ["barfoothefoobarman", "wordgoodgoodgoodbestword", "barfoofoobarthefoobarman"]
    words = [["foo", "bar"], ["word", "good", "best", "word"], ["bar", "foo", "the"]]
    output = [[0, 9], [], [6, 9, 12]]

    for c, w in zip(s, words):
        print("#", solution.findSubstring(c, w))
