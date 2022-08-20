# while True:
#     try:
#         # l = list(map(int, input().strip("{").strip("}").split(",")))
#         l = list(map(int, input().strip().split()))
#         print(l)
#     except EOFError:
#         break
from collections import  defaultdict
cache=defaultdict(list)
keylist=[1,0,3,0,1]
for key in keylist:
    cache[key].append(1)


# if __name__=="__main__":
#     while True:
#         try:
#             print(1//3)
#             n = int(input().strip()) #这边一行就一个数
#             nums = list(map(int, input().strip().split()))
#             print(n)
#         except EOFError:
#             break


# while True:
#     a= map(int, input().split())
#
#     if a == 0:
#         break
#
#     print(a)


