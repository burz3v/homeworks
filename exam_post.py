#############

import json
import requests

class Post:
    def __init__(self,d):
        self.__dict__= d

    def __str__(self):
        result = f'Post {id}\n----------\n'
        for k,v in self.__dict__.items():
            result += str(k) + ': ' + str(v) + '\n'
        return result

id = input('Enter the post id ')

response = requests.get(r'http://jsonplaceholder.typicode.com/posts/' + id)

if response.status_code // 100 == 2:
    postDict = json.loads(response.content)
    choosedPost = Post(postDict)
    print(choosedPost)
else:
    print('This post id does not exist')
    
#############
