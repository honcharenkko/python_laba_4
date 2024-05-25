arr =[]
def warning():
    print("PROBLEM!")

def login_user(username, password):
    if not isinstance(username, str) or not isinstance(password, (str, int)):
        warning()
        raise TypeError('Данні введені некоректно')
    else:
        arr.append(username)
        arr.append(password)
        print(arr)
