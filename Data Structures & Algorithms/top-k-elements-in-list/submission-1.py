class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        U: Return the top k most frequent elements
            I: int list and int
            O: int array
            C: return only k elements, k < num of distinct elements
            E: [1], k=1 -> [1]
               [3,3,3,4,4,4,2,2,2], k=2 -> [3,4]
               [7,7] k=1 -> [7]

        M: Hashmap + bucket
        
        P:
        create bucket list
        create a num to freq hashmap of nums
        loop through hashmap:
            add each num to position in bucket that matches its freq
        res list
        loop through bucket from the bucket:
            if current num is not 0: 
                add it to res
                if res == k:
                    break
        return res
        '''
        n = len(nums)
        bucket = [[] for _ in range(n+1)]

        num_to_freq = Counter(nums)    #{7:2}
        for num, freq in num_to_freq.items():
            bucket[freq].append(num)        #bucket = [0,0,7]
        
        res = []
        for i in range(n,-1,-1):  #2 -> 0
            if bucket[i]: 
                for num in bucket[i]:
                    res.append(num)   #res = [7]
                    if len(res) == k:
                        return res

