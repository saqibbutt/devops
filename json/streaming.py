#!/usr/bin/python3
import requests
import sys

final_list = list()
watch_list = ["alpha", "beta", "gamma"]
i = 0
response = requests.get('<>streaming-url-returning-json')
if response.status_code == 200:
    result = response.json()
    stream_list = result[0]['streams']
    for x in stream_list:
        if x['strm'] in watch_list:
            i+=1
            final_list.append(x['strm'])

if i == len(watch_list):
    print("OK - " + str(final_list))
    sys.exit(0)
elif i < len(watch_list):
    print("Critical - Streaming is down. Remaining " + str(final_list))
    sys.exit(2)
else:
    print("Unknown -  " + str(final_list))
    sys.exit(3)

