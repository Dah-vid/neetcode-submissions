class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                idx, temp = stack.pop()
                answer[idx] = i - idx
            stack.append((i, temperatures[i]))
        return answer


