import requests

proxy_string= "residential.pingproxies.com:7777:customer-330b0f81CJQKi-cc-GB-sessid-pAGHrbVf4:Pp1l4hpvzh"
proxy_parts = proxy_string.split(":")
ip_address = proxy_parts[0]
port = proxy_parts[1]
username = proxy_parts[2]
password = proxy_parts[3]

proxies = {
    "http" :"http://{}:{}@{}:{}".format(username,password,ip_address,port),
    "https":"http://{}:{}@{}:{}".format(username,password,ip_address,port),
}

# HTTP
r = requests.get("http://www.airbnb.com/", proxies=proxies)
print(r.status_code)