class Twitter:

    def __init__(self):
        #we want to know what user has want, use a dictioanry
        self.followMap = defaultdict(set) #every is unique
        self.tweetMap = defaultdict(list) #[tweetid, time]
        self.time = 0        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1 #we decrement because we want the latest one to show on top, we will be using a minHeap

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        res = []

        self.follow(userId, userId)
        #run a scan, and get every user in that they follow and pull their latest tweets
        #compare their latest tweet timestamp and add to our result array and pull their next msot recent tweets

        for f in self.followMap[userId]:
            if f in self.tweetMap:
                index = len(self.tweetMap[f]) - 1
                time, tweetId = self.tweetMap[f][index]
                heapq.heappush(minHeap, [time, tweetId, f, index-1])
            
        while len(res) < 10 and minHeap:
            time, tweetId, f, index = heapq.heappop(minHeap)
            res.append(tweetId)

            #queue up the next one
            if index >= 0:
                time, tweetId = self.tweetMap[f][index]
                heapq.heappush(minHeap, [time, tweetId, f, index-1])
        return res 

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)
        
