class Solution:
    def maxCoins(self,nums):
        cleaned = [1]
        for i in nums:
            if i:
                cleaned.append(i)
        cleaned.append(1)
        n = len(cleaned) - 2
        dp=[[-1]*(n+1) for i in range(n+1)]
        return self.maxCoinsHelper(1,n,cleaned,dp)
    
    def maxCoinsHelper(self,start,end,nums,dp):
        if (start > end):
            return 0
        if (dp[start][end]!=-1):
            return dp[start][end]
        if (start==end):
            dp[start][end]=nums[start-1]*nums[start]*nums[start+1]
            return dp[start][end]
        for lastBurst in range(start,end+1):
            cur_score=(nums[start-1]*nums[lastBurst]*nums[end+1]+self.maxCoinsHelper(start,lastBurst-1,nums,dp)+self.maxCoinsHelper(lastBurst+1,end,nums,dp))
            if((dp[start][end]==-1 )or (cur_score>dp[start][end])):
                 dp[start][end]=cur_score

        return dp[start][end]
    
sol=Solution()
a=list(map(int,input().split()))
res=sol.maxCoins(a)
print(res)
        