import requests
import config

API_URL = 'https://developers.zomato.com/api/v2.1'

'''
    GET al list of categories
'''
def getCategories():
    headers = {'user-key': config.API_KEY}
    r = requests.get(API_URL + '/categories', headers = headers)
    print(r.status_code)
    print(r)
    print(r.json())
    return r.json()


getCategories()

