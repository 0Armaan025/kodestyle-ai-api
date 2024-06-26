import requests
import json
from github import update_file



url = "https://api.cloudflare.com/client/v4/accounts/85d4970843d0f1481a2d622d9e182674/ai/run/@cf/google/gemma-7b-it-lora"

def make_readme(repo_name, repo_description, repo_contributors, readme_content, tone, languages):
    payload = {
        "max_tokens": 5000,
        "prompt": f"Please help me make a readme.md file for {repo_name}, description: {repo_description}, contributors: {repo_contributors}, present content of the file: {readme_content}, I want to have in the .md format, the tone of the file must be {tone}, languages: {languages}",
        "raw": False,
        "stream": False
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer V8hFSHBeX7KkV1Vj87YQEM_6K_1lFIWzSC4RXJJr"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    parsed_data = json.loads(response.text)
    readme_response = parsed_data['result']['response']
    return readme_response


def push_to_github(owner_name, repo_name, file_path, new_content, commit_message, branch, token):
    update_file(owner=owner_name, repo_name=repo_name, file_path=file_path, content=new_content, commit_message=commit_message, branch=branch, token=token)
