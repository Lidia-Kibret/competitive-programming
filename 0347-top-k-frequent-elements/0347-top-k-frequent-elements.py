class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        
        ans=[]
        count=count.most_common(k)

        for key,val in count:
            ans.append(key)

        return(ans)

        