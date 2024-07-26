class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        path=path.split('/')
        result=[]
        for i in path:
            if i!='':
                result.append(i)
        for i in result:
            if i=='.':
                continue
            elif i=='..':
                if stack:
                   stack.pop()
            else:
                stack.append(i)
        return '/'+'/'.join(stack)
        