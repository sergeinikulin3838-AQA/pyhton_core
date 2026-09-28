import random
def generate_login():
    logins = ["user_1", "user_2", "user_3", "user_4", "user_5"]
    return random.choice(logins)
def generate_age():
    return random.randint(18, 65)
def generate_status():
    statuses = ["ACTIVE", "BLOCKED", "INACTIVE"]
    return random.choice(statuses)
def generate_user():
    user = {
        "login": generate_login(),
        "age": generate_age(),
        "status": generate_status()
    }
    return user