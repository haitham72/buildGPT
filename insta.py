import instaloader
import re

def download_instagram_video(url):
    # Initialize Instaloader instance
    L = instaloader.Instaloader()

    # Extract shortcode from URL
    shortcode = re.search(r'/p/([A-Za-z0-9_-]+)/', url)
    if not shortcode:
        print("Invalid URL format.")
        return

    shortcode = shortcode.group(1)

    try:
        # Load the post using the shortcode
        post = instaloader.Post.from_shortcode(L.context, shortcode)

        # Check if the post is a video
        if post.is_video:
            # Download the video
            L.download_post(post, target=f"video_{shortcode}")
            print(f"Video downloaded successfully: video_{shortcode}")
        else:
            print("The provided URL does not point to a video.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    url = input("Enter the Instagram video URL: ")
    download_instagram_video(url)
