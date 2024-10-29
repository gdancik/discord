# Gets members from server specified in credentials file

import requests
import json
import credentials


headers = {'Authorization' : 'Bot {}'.format(credentials.BOT_TOKEN)}

## get guild roles ##
base_URL = 'https://discord.com/api/v10/guilds/{}'.format(credentials.GUILD_ID)
r = requests.get(base_URL, headers=headers)    
guild = r.json()    
roles = guild['roles']
roles = {r['id']:r['name'] for r in roles}


## get guild members
base_URL = 'https://discord.com/api/v10/guilds/{}/members'.format(credentials.GUILD_ID)

params = {"limit": 1000}
r = requests.get(base_URL, headers=headers, params=params)



def printUserInfo(user, roles, no_roles = False) :
    
    user = obj['user']
    uname = user['username']
    dname = ''
    if 'display_name' in user: 
    	dname = user['display_name']
    myroles = ''

    myroles = obj['roles']
    myroles = [roles[r] for r in myroles]
    
    if not no_roles or (no_roles and len(myroles) == 0) :
        print(f'{uname} ({dname}): {myroles}')


# print info for all members
#print(r.raise_for_status())
for obj in r.json():
    printUserInfo(obj, roles)

print()
print() 
print('Users with no roles: ')
for obj in r.json():
    printUserInfo(obj, roles, no_roles = True)



