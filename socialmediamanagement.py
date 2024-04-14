import json
import requests

url = "https://api.cloudflare.com/client/v4/accounts/2e92eb4614a4e9031da13af6d2619fab/ai/run/@cf/meta/llama-2-7b-chat-fp16"

def create_social_media_post(repo_name, repo_owner_name, repo_description, description, token, tone):
    payload = {
        "max_tokens": 999,
        "prompt": f"Please create an amazing post for social media for the repo: {repo_name}, repo owner name as : {repo_owner_name}, repo description as: {repo_description}, normal description as: {description}, and the tone must be {tone}, the content length must not exceed 260 characters",
        "raw": False,
        "stream": False
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    parsed_data = json.loads(response.text)
    post = parsed_data['result']['response']
    return post

# Call the function to create the social media post

# # Write the post to a file
# with open("new.txt", "w", encoding="utf-8") as file:
#     file.write(post)
