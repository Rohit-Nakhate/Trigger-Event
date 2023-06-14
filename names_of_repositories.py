from github import Github
# Replace with your GitHub App private key path
PRIVATE_KEY_PATH = '"C:\\Users\\admin\\Downloads\\rohit223test.2023-06-12.private-key.pem"'
# Replace with your GitHub App ID
APP_ID = '346211'

def main():
    # Create a GitHub instance using your GitHub App private key and app ID
    g = Github(APP_ID, private_key=PRIVATE_KEY_PATH)

    # Implement your GitHub App functionality
    # Example: Print the names of repositories accessible to the app
    for repo in g.get_user().get_repos():
        print(repo.name)

if __name__ == "__main__":
    main()
