class Solution(object):
    def uniqueOccurrences(self, arr):
        count = {

        }

        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        occurrences = count.values()
        return len(occurrences) == len(set(occurrences))
        