"""
71. Simplify Path
"""

import re
from typing import List


class Solution:
    def simplifyPath(self, path: str) -> str:
        temp = re.sub(r"\/+", "/", path)
        # temp = re.sub(r"\.{3,}", "...", temp)
        stacks = []
        for c in temp.split("/"):
            if c:
                stacks.append(c)
        print("@", stacks)
        answer = []
        for i in range(len(stacks)):
            if stacks[i] == ".":
                continue
            elif stacks[i] != "..":
                answer.append(stacks[i])
            else:
                if answer:
                    answer.pop()
        print("@@", answer)
        if answer:
            return "/" + "/".join(answer)
        return "/"


if __name__ == "__main__":
    solution = Solution()
    strings = ["/home/", "/../", "/home//foo/", "/home/...../foo", "/a/./b/../../c/", "/a/../../b/../c//.//", "/..."]
    output = ["/home", "/", "/home/foo", "/foo", "/c", "/c"]

    for s in strings:
        print("#", solution.simplifyPath(s))
