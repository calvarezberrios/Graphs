import random, math
from collections import deque

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        
        # Add users
        for u in range(1, num_users + 1):
            self.add_user(u)

        # Create friendships
        possible_friendships = []
        for u in self.users:
            for f in range(u + 1, self.last_id + 1):
                possible_friendships.append((u, f))

        random.shuffle(possible_friendships)

        for i in range(math.floor(num_users * avg_friendships / 2)):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
                    
        visited[user_id] = self.bfs(user_id, user_id)
        
        for user in self.users:
            path = self.bfs(user, user_id)
            if path != None:
                visited[user] = path
        return visited

    def bfs(self, start, end):
        queue = deque()
        visited = set()

        queue.appendleft([start])
        
        while len(queue) > 0:
            currPath = queue.pop()
            currNode = currPath[-1]

            if currNode == end:
                return currPath
            
            if currNode not in visited:
                visited.add(currNode)
                for friend in self.friendships[currNode]:
                    newPath = list(currPath)
                    newPath.append(friend)
                    queue.appendleft(newPath)

    # Returns True if user_id and friend_id have successfully been added as friends
    def add_friendship_linear(self, user_id, friend_id):
        if user_id == friend_id:
            return False
        # Check if friend_id and user_id are not already friends with each other
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    
    def populate_graph_linear(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        
        # Add users
        for u in range(1, num_users + 1):
            self.add_user(u)

        # Create random friendships until we've reached target number of friendships
        target_friendships = num_users * avg_friendships
        total_friendships = 0
        collisions = 0
        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if self.add_friendship_linear(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1
            # keep adding friendships

        print(f"Collisions: {collisions}")
if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
