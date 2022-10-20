import requests
import json
import argparse

# Create the parser
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('--auth_type', type=str, required=True, help="Type 'form' or 'json'")
parser.add_argument('--url', type=str, required=True, help="Full URL of the login page")
# Parse the argument
args = parser.parse_args()


with open("input_file", "r") as f:
    credentials = f.read()


#login_url = "https://waf.barracuda.com/cgi-mod/index.cgi"
print(args.auth_type)

login_url = args.url
print(login_url)
for cred in json.loads(credentials):
    if args.auth_type == "form":
        login_request = requests.post(login_url, data=cred, verify=False)
        print(login_request.status_code)
    elif args.auth_type == "json":
        headers = {"Content-Type": "application/json"}
        login_request = requests.post(login_url, data = json.dumps(cred), headers=headers, verify=False)
        print(login_request.status_code)
    else:
        print("invalid input")
        exit
