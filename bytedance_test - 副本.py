# class Solution:
#     def spiralOrder(self, matrix) :
#         n=len(matrix)
#         if not n :
#             return []
#         m=len(matrix[0])
#         t=m*n-1
#         res=[matrix[0][0]]
#         i=0
#         j=0
#         while(t>0):
#             if j+1<m and matrix[i][j+1]!=-1:
#                 res.append(matrix[i][j+1])
#                 j+=1
#                 t-=1
#                 matrix[i][j]=-1
#                 continue
#             elif i+1<n and matrix[i+1][j]!=-1:
#                 res.append(matrix[i+1][j])
#                 i+=1
#                 t-=1
#                 matrix[i][j]=-1
#                 continue
#             elif j-1>=0 and matrix[i][j-1]!=-1:
#                 res.append(matrix[i][j-1])
#                 j-=1
#                 t-=1
#                 matrix[i][j]=-1
#                 continue
#             elif i-1>=0 and matrix[i-1][j]!=-1:
#                 res.append(matrix[i-1][j])
#                 i-=1
#                 t-=1
#                 matrix[i][j]=-1
#                 continue
#         return res
#
# if __name__ == '__main__':
#     matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#     print(Solution().spiralOrder(matrix))


class Singleton(object):
    def __init__(self,*args,**kwargs):
        pass

    @classmethod
    def get_instance( *args, **kwargs):
        # 利用反射,看看这个类有没有_instance属性
        if not hasattr(Singleton, '_instance'):
            Singleton._instance = Singleton(*args, **kwargs)

        return Singleton._instance


s1 = Singleton(1)  # 使用这种方式创建实例的时候,并不能保证单例
s2 = Singleton.get_instance(2)  # 只有使用这种方式创建的时候才可以实现单例
s3 = Singleton(3)
s4 = Singleton.get_instance(4)

print(id(s1), id(s2), id(s3), id(s4))