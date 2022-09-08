def main():
    with open("password.txt","r") as file:
        file_reader = file.read()
        user_info(file_reader)
        file.close() 
        
def user_info(file):
    user = input("Enter your username: ")
    for row in file:
        if row[0] != user:
            pass
        elif row[0] == user:
            print("Helllo",row[0])
            user_found=[row[0], row[1]]
            pass_check(user_found)
            break
        else:
            print("not found")
            continue

def pass_check(user_found):
    attempts = 0
    max_attempts = 2
    while True:
        user = input("enter your password: ")
        if user_found[1] == user:
            for i in range(3):
                print("password match")
            break
        else:
            print("password not match")
            attempts += 1
        if attempts > max_attempts:
            print("Invalid password")
            break            
main()
            
