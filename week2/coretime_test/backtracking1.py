class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        arr = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        result = []

        def backtracking(now, count):
            if count == len(digits):
                return result.append("".join(now))
        

            for i in arr[int(digits[count])]:
                now.append(i)
                backtracking(now, count + 1)
                now.pop()
            

        backtracking([], 0)
        return result


            
            
            

                


        