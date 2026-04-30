class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list) #[time, tweetId]
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1


    def getNewsFeed(self, userId: int) -> List[int]:
        #run a scan on every person they follow, add their last tweetId at the end
        #add them to a minHeap, the most recent gets popped
        #process the heap, and add the followees next recent tweet until the result is 10 or there are no more tweets

        #first we have to gurantee with subscribe to ourselves, guranteeing invariant
        self.followMap[userId].add(userId)
        res = []
        minHeap = []

        for f in self.followMap[userId]:
            if f in self.tweetMap:
                index = len(self.tweetMap[f]) - 1
                time, tweetId = self.tweetMap[f][index]
                minHeap.append([time, tweetId, f, index-1]) #increment to the next index
        
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            time, tweetId, f, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0: #we are in bound
                #retrieve the next tweet
                time, tweetId = self.tweetMap[f][index]
                #add the next tweet inline to the minHeap
                heapq.heappush(minHeap, [time, tweetId, f, index-1])


        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)


        
