class Twitter:

    def __init__(self):
        self.time = 0
        self.tMap = defaultdict(list) #[time, tweetId]
        self.fMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.tMap[userId].append([self.time, tweetId])

        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        res = []
        minHeap = []

        self.fMap[userId].add(userId)

        for followee in self.fMap[userId]:
            if followee in self.tMap:
                index = len(self.tMap[followee])-1 #get the last index 
                time, tweetId = self.tMap[followee][index]
                minHeap.append([time, tweetId, followee, index-1])
        
        heapq.heapify(minHeap)

        while len(res) < 10 and minHeap:
            time, tweetId, followee, index = heapq.heappop(minHeap)
            res.append(tweetId)

            #add the next tweet from that user into the minheap
            if index >= 0:
                time, tweetId = self.tMap[followee][index]
                heapq.heappush(minHeap, [time, tweetId, followee, index-1])
                
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.fMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.fMap:
            self.fMap[followerId].discard(followeeId)
        
