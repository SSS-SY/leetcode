import collections
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_counts = list(collections.Counter(tasks).values())
        print(task_counts)
        M = max(task_counts)
        Mct = task_counts.count(M)
        print(Mct)
        return max(len(tasks),(M - 1)*(n + 1) + Mct)
print(Solution().leastInterval(["A","A","A","B","B","B"],2))