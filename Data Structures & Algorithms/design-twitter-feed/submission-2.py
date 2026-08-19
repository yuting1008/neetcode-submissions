class Twitter:

    def __init__(self):
        self.num = 0
        self.posts = [] # paris of [tweetId, userId]
        heapq.heapify(self.posts)
        self.followList = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.posts, [self.num, tweetId, userId])
        self.num -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.followList[userId]
        posts = list(self.posts)
        heapq.heapify(posts)
        res = []
        while len(res) < 10 and posts:
            post = heapq.heappop(posts)
            if post[2] in followees or post[2] == userId:
                res.append(post[1])
            
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followList[followerId]:
            self.followList[followerId].remove(followeeId)
