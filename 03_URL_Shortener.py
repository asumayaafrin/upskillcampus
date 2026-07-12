import random
import string

url_database = {}

def shorten_url(long_url):
    short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    short_url = "short.ly/" + short_code
    url_database[short_url] = long_url
    return short_url

def get_original_url(short_url):
    return url_database.get(short_url, "URL not found")

while True:
    print("\n--- URL Shortener ---")
    print("1. Shorten URL")
    print("2. Retrieve Original URL")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        long_url = input("Enter long URL: ")
        short_url = shorten_url(long_url)
        print("Shortened URL:", short_url)

    elif choice == "2":
        short_url = input("Enter shortened URL: ")
        print("Original URL:", get_original_url(short_url))

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
