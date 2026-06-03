class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        i = 0
        k = len(numbers) - 1
        sum = 0

        while i < k:
            sum = numbers[i] + numbers[k]
            if sum == target:
                output.append(i+1)
                output.append(k+1)
                return output
                break
            if sum < target:
                i += 1
            if sum > target:
                k -= 1
        return output

        

             

