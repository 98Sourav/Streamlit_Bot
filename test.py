from bardapi import Bard
import json

with open('credentials.json','r') as f:
    file=json.load(f)
    token=file['token']

bard = Bard(token=token)
response=bard.get_answer("what is ML?")['content']
print(response)