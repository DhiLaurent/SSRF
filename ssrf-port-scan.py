import requests

request_type = input("http/https: ")
request_type = request_type.lower()
print(request_type)

url = input("Type URL with parameter: ")
tech = str(input("[1] Status Code\n[2]Content Length\nChoose technique: "))

ports = {21,22,23,25,53,80,110,123,443,995,3306,3389,8080,9000,10050}

if tech == "1" and request_type == "http":
    for port in ports:
        r = requests.get(f"http://{url}http://localhost:{port}")
        if r.status_code == 200:
            print(f"[{r.status_code}] - {request_type}://{url}http://localhost:{port}")

elif tech == "1" and request_type == "https":
    for port in ports:
        r = requests.get(f"https://{url}http://localhost:{port}")
        if r.status_code == 200:
         print(f"[{r.status_code}] - {request_type}://{url}http://localhost:{port}")
elif tech == "2" and request_type == "http":
    for port in ports:
        r = requests.get(f"http://{url}http://localhost:{port}")
        print(f"Content-Length: {len(r.content)}")
elif tech == "2" and request_type == "https":
    for port in ports:
        r = requests.get(f"https://{url}http://localhost:{port}")
        print(f"Content-Length: {len(r.content)}")
