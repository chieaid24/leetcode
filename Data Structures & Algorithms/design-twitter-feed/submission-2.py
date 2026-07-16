class Twitter:
    # scratch pad:
    # genuinely easy to do this
    # track own_posts = {userId : [(timestamp, postId), (timestamp, postId)]}
    # track followed users = {userId : set[followedId]}
    # for posting a tweet, we just append to own posts O(1)
    # for following / unfollowing, just update the followed users O(1)
    # for getting news feed, we compile a big list of own posts + for each of followed users' own posts o(n)
    # max heapify it o(n)
    # pop the first 10 from the list and return 

    def __init__(self):
        self.own_posts = defaultdict(list) # {userId : [(timestamp, postId), (timestamp, postId)]}
        self.followed_users = defaultdict(set) # {userId : set[userId, userId]
        self.time_stamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # append to our own_posts
        self.own_posts[userId].append((self.time_stamp, tweetId))
        self.time_stamp += 1
        print(self.own_posts[userId], self.time_stamp)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # compile the FULL news feed from own + all of followed lists
        posts = self.own_posts[userId][:]
        for followee_id in self.followed_users[userId]:
            posts.extend(self.own_posts[followee_id])
        heapq.heapify_max(posts)

        res = []
        while posts and len(res) < 10:
            res.append(heapq.heappop_max(posts)[1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        # edge case:
        if followerId == followeeId:
            return
        # add it to the set
        self.followed_users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followed_users[followerId].discard(followeeId)
        
