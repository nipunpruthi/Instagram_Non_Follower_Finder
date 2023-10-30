import json
followers = open("/Users/nipun.pruthi/tmp/instagram-nipun._.pruthi-2023-10-30-NAAkzs8f/followers_and_following/followers_1.json")
following = open("/Users/nipun.pruthi/tmp/instagram-nipun._.pruthi-2023-10-30-NAAkzs8f/followers_and_following/following.json")

followers_data = json.load(followers)
following_data = json.load(following)

followers_set = set()
following_set = set()

for i in followers_data:
    followers_set.add(i["string_list_data"][0]['value'])
    print(i["string_list_data"][0]['value'])

for i in following_data['relationships_following']:
    print(i['string_list_data'][0]['value'])
    following_set.add(i['string_list_data'][0]['value'])

for i in following_set:
    if i not in followers_set:
        print(i)