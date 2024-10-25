class Solution:
    def simplifyPath(self, path: str) -> str:
        valid = ['.', '..', '/']
        l = path.split('/')
        l2 = []
        for i in l:
            if i != '' and i != '.' and i != '..':
                l2.append(i)
            if i == '..' and len(l2) > 0:
                l2.pop()
        s = "/" + '/'.join(l2)
        return s