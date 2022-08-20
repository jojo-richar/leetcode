# 节点类
import inspect, sys , collections


class Solution:
    def leastInterval(self, tasks, n: int):
        freq = collections.Counter(tasks)

        # 任务总数
        m = len(freq)
        nextValid = [1] * m
        rest = list(freq.values())

        time = 0
        for i in range(len(tasks)):
            time += 1
            minNextValid = min(nextValid[j] for j in range(m) if rest[j] > 0)
            time = max(time, minNextValid)

            best = -1
            for j in range(m):
                if rest[j] and nextValid[j] <= time:  #有任务在空闲区
                    if  best==-1 or rest[j] > rest[best]:
                        best = j

            nextValid[best] = time + n + 1
            rest[best] -= 1

        return time



if __name__ == '__main__':
    tasks = ["A","A","A","A","A","B","B","C","D","E","F","G"]
    n = 2
    print(Solution().leastInterval(tasks,n))
    print("ok")