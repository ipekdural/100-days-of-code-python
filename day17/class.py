# if you want to create a blank class:
class Test:
    pass


# constructor
class User:
    def __init__(self, user_id, user_name):
        # Every object has been created will execute this code
        print("new user being created...")
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0  # all objects will have this default attribute
        self.following = 0

    # adding methods to classes
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Angela")
user_2 = User("002", "Jack")
user_1.follow(user_2)
print(user_2.followers)
