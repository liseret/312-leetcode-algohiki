class Solution:
    def maxCoins(self,nums):
        cleaned = [1] #1 - слева
        for i in nums:
            if i: #убираем 0- тк не несут ценности
                cleaned.append(i)
        cleaned.append(1)#1 - справа
        n = len(cleaned) - 2#количество реальных шариков
        #dp[start][end] будет хранить макс. монеты для интервала от start до end
        #размер (n+1)*(n+1), заполняем -1 (маркер того, что значение еще не посчитали)
        dp=[[-1]*(n+1) for i in range(n+1)]
        return self.maxCoinsHelper(1,n,cleaned,dp)
    
    def maxCoinsHelper(self,start,end,nums,dp):
        #база - если левая граница больше правой -> шариков нет 
        if (start > end):
            return 0
        #мемоизация(чтообы лишний раз ничего не считать) - если результат для этого интервала уже есть в таблице -> возвращаем его же 
        if (dp[start][end] != - 1):
            return dp[start][end]
        #база - один шарик в интервале
        if (start == end):
            #вычисляем монеты, умножая собственное значение шарика на значения его соседей (то бишь nums[start - 1] и nums[start + 1])
            dp[start][end] = nums[start - 1] * nums[start] * nums[start + 1]
            return dp[start][end]
        #основной переход - перебираем, какой шарик в интервале [start,end] лопнет последним
        for lastBurst in range(start, end + 1):
            #cчитаем выгоду - прибыль от последнего шарика (с учетом внешних границ) + результаты уже решенных подзадач для левой и правой частей относительно него.
            cur_score=(nums[start - 1] * nums[lastBurst] * nums[end+1] + self.maxCoinsHelper(start, lastBurst - 1,nums, dp) + self.maxCoinsHelper(lastBurst + 1,end,nums,dp))
            # обновляем значение в таблице dp, если для данного интервала решение найдено впервые или если текущий вариант разделения принёс больше монет, чем предыдущие.
            if((dp[start][end] == - 1 )or (cur_score > dp[start][end])):
                 dp[start][end] = cur_score
        #ответ находится здесь тк это итог всех поисков внутри интервала
        return dp[start][end]


#передает данные в класс и тп.
sol=Solution()
a=list(map(int,input().split()))
res=sol.maxCoins(a)
print(res)
        