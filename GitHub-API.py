"""
A python script that accesses the GitHub API and returns information about a
specific user, repositories, creates new repos, and deletes a repo
"""
import requests

headers = {"Authorization": "token 1f36137fbbe1602f779300dad26e4c1b7fbab631"}
response = requests.get("https://api.github.com/users/VikParuchuri",
                        headers=headers)
user_info = response.json()
response_org = requests.get("https://api.github.com/users/VikParuchuri/orgs",
                            headers=headers)
user_orgs = response_org.json()
# print(user_info)
# print(user_orgs)

# use the same endpoint, /users, to get the information about a user called
# torvalds using the same header information
response_torvalds = requests.get("https://api.github.com/users/torvalds",
                                 headers=headers)
torvalds_info = response_torvalds.json()
# print(torvalds_info)

# get information about the Hello-World repository that the user octocat owns
response_octocat = requests.get\
    ("https://api.github.com/repos/octocat/Hello-World", headers=headers)
octocat_hello_world = response_octocat.json()

# get the page 2 repositories that Vik Parachuri starred using the starred
# endpoint
parameters = {"per_page": 50, "page": 2}
response_page2 = requests.get\
    ("https://api.github.com/users/VikParuchuri/starred", headers=headers,
     params=parameters)
page2_repos = response_page2.json()

# user level endpoints to return information of the authenticated user
response_user = requests.get("https://api.github.com/users", headers=headers)
user = response_user.json()

# Create a repository named learning-about-apis.
# Assign the status code of the response to the status variable.
payload = {"name": "learning-about-apis"}
response_repo = requests.post("https://api.github.com/users/repos",
                              headers=headers,
                              json=payload)
status = response_repo.status_code
# Make a PATCH request to the learning about apis repository and the test
# https://api.github.com/repos/VikParuchuri/learning-about-apis
# https://api.github.com/repos/VikParuchuri/learning-about-apis
# endpoint that changes the description.
# Assign the status code of the response to status.
payload2 = {"description": "the best repository ever", "name": "test"}
response_test = requests.patch("https://api.github.com/repos/VikParuchuri/test",
                               headers=headers, json=payload2)
status2 = response_test.status_code

payload3 = {"description": "learning about requests",
            "name": "learning-about-apis"}
response_apis = requests.patch\
    ("https://api.github.com/repos/VikParuchuri/learning-about-apis",
     headers=headers, json=payload3)
status3 = response_apis.status_code

# Make a delete request to the
# https://api.github.com/repos/VikParuchuri/learning-about-apis endpoint.
# Assign the status_code of the response to the variable status.
response_delete = requests.delete\
    ("https://api.github.com/repos/VikParuchuri/learning-about-apis",
     headers=headers)
status4 = response_delete.status_code








