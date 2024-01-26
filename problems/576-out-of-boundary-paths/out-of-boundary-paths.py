class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        dirs=((0,1),(1,0),(0,-1),(-1,0))
        kMod=1000000007
        ans=0
        dp=[[0]*n for i in range(m)]
        dp[startRow][startColumn]=1
        for i in range(maxMove):
            nDp=[[0]*n for i in range(m)]
            for i in range(m):
                for j in range(n):
                    if dp[i][j]>0:
                        for dx,dy in dirs:
                            x=i+dx
                            y=j+dy
                            if x<0 or x==m or y<0 or y==n:
                                ans=(ans+dp[i][j])%kMod
                            else:
                                nDp[x][y]=(nDp[x][y]+dp[i][j])%kMod
            dp=nDp
        return ans