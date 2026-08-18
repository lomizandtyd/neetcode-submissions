class Twitter:

    def __init__(self):
        self.followers = {}
        self.tweets = {}
        self.time = 0

    def _init_user(self, userId):
        if userId in self.followers:
            return

        self.followers[userId] = {userId: True}
        self.tweets[userId] = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._init_user(userId)

        user_tweets = self.tweets[userId]
        user_tweets.append([self.time, tweetId])
        self.time += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        h = []

        for follower in self.followers[userId]:
            for tw in self.tweets[follower][-10:]:
                heapq.heappush(h, tw)

                if len(h) > 10:
                    heapq.heappop(h)

        h2 = []
        while h:
            h2.append(h[0][1])
            heapq.heappop(h)
        return h2[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self._init_user(followerId)
        self._init_user(followeeId)

        self.followers[followerId][followeeId] = True

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._init_user(followerId)
        self._init_user(followeeId)

        if followeeId in self.followers[followerId] and followeeId != followerId:
            self.followers[followerId].pop(followeeId)


        
