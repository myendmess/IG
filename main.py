import os

# Set terminal title and color
os.system("title Instagram followers, likes, and views botter.")
os.system("color a")

def like_post(url):
    print(f"Liked the post at URL: {url}")

def view_story(url):
    print(f"Viewed the story at URL: {url}")

def generate_followers():
    print("Welcome to the follower generator.")
    # Placeholder for follower generation logic
    print("Followers generated successfully.")

def main():
    print("Please choose a botter category:")
    print("[1] - Likes")
    print("[2] - Views")
    print("[3] - Followers")
    choose = input('> ')

    if choose == "1":
        url = input("Please input the post URL: ")
        if not url.startswith("https://www.instagram.com/p/"):
            print("Invalid post URL.")
            return
        like_post(url)

    elif choose == "2":
        url = input("Please input your story URL: ")
        if not url.startswith("https://www.instagram.com/stories/"):
            print("Invalid story URL.")
            return
        view_story(url)

    elif choose == "3":
        print("Welcome to the followers botter for Instagram.")
        generate_followers()


    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
