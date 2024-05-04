

import mood

def main():

    mood = input("How are you feeling today? ")
    print(mood.mood_response(mood))

if __name__ == "__main__":
    main()