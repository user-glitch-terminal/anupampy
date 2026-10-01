# Mini project -- Unique hobby finder
def collect_hobbies():
    hobbies = set()
    print("\nEnter your hobbies one by one. Type 'done' to finish.")
 
    while True:
        hobby = input("Enter a hobby")
 
        if hobby.lower() == 'done':
            break
 
        hobbies.add(hobby)
    
    return hobbies
 
def display_hobbies(hobbies):
    print("\nYour unique hobbies are: ")
 
    for hobby in hobbies:
        print(hobby)
 

def main():
    print("Your hobbies: ")
 
    my_hobbies = collect_hobbies()
    display_hobbies(my_hobbies)
 
    print("\nFriend's hobbies")
 
    friend_hobbies = collect_hobbies()
    display_hobbies(friend_hobbies)
 
    print("\nAll hobbies: ", my_hobbies | friend_hobbies)
    print("\nCommon hobbies: ", my_hobbies & friend_hobbies)
    print("\nMy unique hobbies: ", my_hobbies - friend_hobbies)
 
main()
 