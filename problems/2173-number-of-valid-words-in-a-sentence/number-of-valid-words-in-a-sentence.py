class Solution(object):
    def countValidWords(self, sentence):
        def chk(i):
            ch=0
            for s,j in enumerate(i):
                if j.isdigit():
                    return False
                if j=='-':
                    if ch==1:
                        return False
                    if s==0 or not i[s-1].isalpha():
                        return False
                    if s==len(i)-1 or not i[s+1].isalpha():
                        return False
                    ch+=1
                if j in ['!','.',',']:
                    if s!=len(i)-1:
                        return False
            return True
        return sum(chk(i) for i in sentence.split())
