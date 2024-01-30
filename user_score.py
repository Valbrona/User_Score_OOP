class User:
    def __init__(self, name, engagement): # a good practice is to define all the methods inside the init method, even if you create new ones later, don't forget to add them here
        self.name = name
        self.engagement_metrics = engagement
        ### 2)
        self.score = 0

    def __repr__(self):
        return f"<User {self.name}>"

def email_engaged_user(user):
    try:
        ## 1) You can do it like this:
        # perform_calculation(user.engagement_metrics)
        print("*" * 20)
        #### 2) Or like this:
        user_score = perform_calculation(user.engagement_metrics)
    except KeyError:
        print("Incorrect values provided to our calculation function.") # using this print, the error message is silenced
        # raise # while programming, it is recommended to raise the errors, so you can see what is wrong with the code
    else:   # the else block will only run, if the try block was successfully run
        ### 1)
        # send_engagement_notification(user)
        print("$" * 20)
        #### 2)
        if user_score > 500:
            send_engagement_notification(user)
        else:
            print("Keep going.")

def perform_calculation(metrics):
    return metrics["clicks"] * 5 + metrics["hits"] * 2

def send_engagement_notification(user):
    ### 1)
    # if perform_calculation(user.engagement_metrics) > 500:
    #     print(f"Notification sent to {user}.")
    # else:
    #     print("Keep going.")
    #### 2)
        print(f"Notification sent to {user}.")

my_user = User("Rolf", {"clicks": 70, "hits": 100})
email_engaged_user(my_user)


# def solution(year):
#     return (year + 99) // 100
#
# print(solution(105))
#
# def solution(year):
#
#     if year%100 == 0:
#         return year//100
#     return year//100 + 1
