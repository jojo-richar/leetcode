from collections import defaultdict
class Solution:
    def calcEquation(self, equations, values, queries) :
        # graph=defaultdict(dict)
        # for [a,b],v in zip(equations,values):
        #     graph[a][b]=v
        #     graph[b][a]=1/v
        # def dfs(s,e):
        #     if s not in graph or e not in graph:
        #         return -1
        #     if s==e:
        #         return 1
        #     visited.add(s)
        #     for i in graph[s]:  #s节点的下家节点
        #         if i==e:
        #             return graph[s][i]
        #         if i not in visited:
        #             ans=dfs(i,e)
        #             if ans!=-1:
        #                 return graph[s][i]*ans
        #     return -1
        # res=[]
        # for a,b in queries:
        #     visited=set()
        #     res.append(dfs(a,b))
        # return res
        from collections import defaultdict
        self.link_path=defaultdict(list)
        self.link_value=defaultdict(float)
        for i in range(len(equations)):
            eq = equations[i]
            n1,n2 = eq
            if n2 not in self.link_path[n1]:
                self.link_path[n1].append(n2)
            if n1 not in self.link_path[n2]:
                self.link_path[n2].append(n1)
            self.link_value[(n1,n2)]=values[i]
            self.link_value[(n2,n1)]=1/values[i]
        def bfs(query):
            n_start,n_end = query
            res = 1.0
            if n_start==n_end and n_start in self.link_path:
                return res
            flag = False
            queue = [(n,self.link_value[(n_start,n)]) for n in self.link_path[n_start]] #存放end节点
            seen = {n_start:0}
            while queue:
                next_queue=[]
                for node,cur_value in queue:
                    if node==n_end:
                        flag = True
                        res = cur_value
                        break
                    elif node not in seen:
                        seen[node]=0
                        for next_node in self.link_path[node]:
                            if next_node not in seen:
                                next_queue.append((next_node,cur_value*self.link_value[(node,next_node)]))
                queue = next_queue
                if flag:
                    break
            res = res if flag else -1.0
            return res
        return [bfs(query) for query in queries]
if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]


    print(Solution().calcEquation(equations,values,queries))
