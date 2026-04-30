class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) #user of counts --> list of [count, twitid]
        self.followMap = defaultdict(set) #user --> setID
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1


    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeID in self.followMap[userId]:
            if followeeID in self.tweetMap:
                index = len(self.tweetMap[followeeID])-1
                count, tweetID = self.tweetMap[followeeID][index]
                minHeap.append([count, tweetID, followeeID, index-1])
        heapq.heapify(minHeap)
        while minHeap and len(res) <10:
            count, tweetID, followeeID, index = heapq.heappop(minHeap)
            res.append(tweetID)
            if index >= 0:
                count, tweetID = self.tweetMap[followeeID][index]
                heapq.heappush(minHeap, [count, tweetID, followeeID, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
