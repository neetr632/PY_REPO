import instaloader
import re
import time

def download_posts_from_url(profile_url):
    # Extract the username from the URL
    username_match = re.search(r'instagram\.com/([^/?]+)', profile_url)
    if username_match:
        username = username_match.group(1)
    else:
        print("Invalid Instagram profile URL.")
        return

    # Create an Instaloader instance
    loader = instaloader.Instaloader()

    try:
        # Load the profile by username
        profile = instaloader.Profile.from_username(loader.context, username)

        # Iterate through the profile's posts
        for post in profile.get_posts():
            # Download the post
            loader.download_post(post, target=f"{profile.username}_{post.date_utc.strftime('%Y%m%d')}")
            print(f"Downloaded post: {post.url}")

            # Add a delay to avoid rate limiting
            # Sleep for 20 seconds between requests
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target_url = input("Enter the Instagram profile URL: ")
    download_posts_from_url(target_url)
