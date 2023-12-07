from typing import List

class ListNode:
    def __init__(self, userId, tweetId, time, next=None):
        self.userId = userId
        self.tweetId = tweetId
        self.time = time
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def appendLeft(self, userId: int, tweetId: int, time: int) -> bool:
        newNode = ListNode(userId, tweetId, time)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return True
    
    def appendRight(self, userId: int, tweetId: int, time: int) -> bool:
        newNode = ListNode(userId, tweetId, time)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return True
    
    def mergeWith(self, otherList):
        head1: ListNode = self.head
        head2: ListNode = otherList.head
        result = LinkedList()
        while head1 != None and head2 != None:
            if head1.time > head2.time:
                result.appendRight(head1.userId, head1.tweetId, head1.time)
                head1 = head1.next
            else:
                result.appendRight(head2.userId, head2.tweetId, head2.time)
                head2 = head2.next
        while head1 != None:
            result.appendRight(head1.userId, head1.tweetId, head1.time)
            head1 = head1.next
        while head2 != None:
            result.appendRight(head2.userId, head2.tweetId, head2.time)
            head2 = head2.next
        return result
    
    def getFirst10(self):
        lst = []
        current = self.head
        i = 0
        while current != None and i < 10:
            lst.append(current.tweetId)
            current = current.next
            i += 1
        return lst
    
    def removeByUserId(self, userId):
        while self.head != None and self.head.userId == userId:
            self.head = self.head.next
        previous: ListNode = None
        current: ListNode = self.head
        while current != None:
            if current.userId == userId:
                previous.next = current.next
            else:
                previous = current
            current = current.next

class User:
    def __init__(self, id):
        self.id: int = id
        self.followers = []
        self.tweetList: LinkedList = LinkedList()
        self.feedList: LinkedList = LinkedList()

class Twitter:

    def __init__(self):
        self.users: List[User] = []
        for i in range(501):
            self.users.append(User(i))
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        user: User = self.users[userId]
        user.tweetList.appendLeft(userId, tweetId, self.time)
        user.feedList.appendLeft(userId, tweetId, self.time)
        for follower in user.followers:
            follower.feedList.appendLeft(userId, tweetId, self.time)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        user: User = self.users[userId]
        return user.feedList.getFirst10()

    def follow(self, followerId: int, followeeId: int) -> None:
        userFollower: User = self.users[followerId]
        userFollowee: User = self.users[followeeId]
        if userFollower not in userFollowee.followers:
            userFollower.feedList = userFollower.feedList.mergeWith(userFollowee.tweetList)
            userFollowee.followers.append(userFollower)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        userFollower: User = self.users[followerId]
        userFollowee: User = self.users[followeeId]
        userFollower.feedList.removeByUserId(followeeId)
        if userFollower in userFollowee.followers:
            userFollowee.followers.remove(userFollower)


#["Twitter","postTweet","follow","follow","getNewsFeed","postTweet","getNewsFeed","getNewsFeed","unfollow","getNewsFeed","getNewsFeed","unfollow","getNewsFeed","getNewsFeed"]
#[[],[1,5],[1,2],[2,1],[2],[2,6],[1],[2],[2,1],[1],[2],[1,2],[1],[2]]
twitter: Twitter = Twitter()
twitter.postTweet(1, 4)
twitter.postTweet(2, 5)
twitter.unfollow(1, 2)
twitter.follow(1, 2)
twitter.getNewsFeed(1)