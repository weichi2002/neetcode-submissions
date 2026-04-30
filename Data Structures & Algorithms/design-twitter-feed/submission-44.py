class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list) #userId -> [count, tweetIds]
        self.followMap = defaultdict(set) #userId -> set of followeeId

        
    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        res = []
        minHeap = []

        self.followMap[userId].add(userId) #also subscribe to yourself

        
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                last_index = len(self.tweetMap[followeeId]) - 1 #get the last index
                time, tweetId = self.tweetMap[followeeId][last_index]
                minHeap.append([time, tweetId, followeeId, last_index - 1]) #next position we are going to process

        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [time, tweetId, followeeId, index-1]) #process the last index
            
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
