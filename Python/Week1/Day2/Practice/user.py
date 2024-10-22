class User :
    def __init__(self,first_name,last_name,email,age):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_rewards_member=False
        self.gold_card_point=0
    def display_info(self):
        print(f"My name is{self.first_name}")
        print(f"My last Name is {self.last_name}")
        print(f"My Email is {self.email}")
        print(f"My age is {self.age}")   
        print(f"Reward member Status is {self.is_rewards_member}")
        print(f"Gold card points :{self.gold_card_point}")
        
    def enroll(self):
        if self.is_rewards_member==True:
            print ("User already a member.")
            return False
        else:
            self.is_rewards_member=True
            self.gold_card_point=200
            return True


    def spend_points(self,amount):
        if self.gold_card_point>amount :
            self.gold_card_point=self.gold_card_point-amount
        else: 
            print ("User does not have enough points")    

my_user1 = User("Sadie", "Flick", "sflick@codingdojo.com",150)
my_user2 = User("alex", "John", "alexjjhon@codingdojo.com",250)


my_user1.spend_points(50)
my_user2.enroll()
my_user1.display_info()
my_user2.display_info()

my_user1.display_info().enroll().spend_points(50).display_info()
my_user2.enroll().spend_points(80).display_info()


