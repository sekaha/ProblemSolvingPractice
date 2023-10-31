from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        letters = {"2":"abc",
                   "3":"def",
                   "4":"ghi",
                   "5":"jkl",
                   "6":"mno",
                   "7":"pqrs",
                   "8":"tuv",
                   "9":"wxyz"
                  }

        def construct(digits,output=""):
            if not digits:
                yield output
            else:
                for l in letters[digits[0]]:
                    yield from construct(digits[1:],output+l)                

        return list(construct(digits))

sol = Solution()
print(sol.letterCombinations("234"))