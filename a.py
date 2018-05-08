import json

path = 'a.json'

with open(path) as f:
    posts = json.load(f)

for post in posts:
    #print(post['title'])
    isContain = False

    for comment in post['comments']:
        #user = comment['user']
        #print(comment)

        if "認真" in comment['content']:
            if isContain == False: 
                print('\n')
                print(post['score'], post['title'])
                print(post['date'], '\t', post['author'])
                print(comment['content'])
                #print(post['url'])
                isContain = True
            else: 
                print(comment['content'])
    if isContain == True:
        print(post['url'])

