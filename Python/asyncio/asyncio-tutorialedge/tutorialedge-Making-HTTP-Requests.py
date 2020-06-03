# https://tutorialedge.net/python/python-http-requests-tutorial/


# prueba: 1 - Making GET Requests
"""

"""

def main1():
    # we define a request object that is equal to requests.get('API')
    req = requests.get('http://pokeapi.co/api/v2/pokemon/1/')
    # we then print out the http status_code that was returned on making this request
    # you should see a successfull '200' code being returned.
    print(req.status_code)


"""
The 200 indicates a successful HTTP request. We can then start to do other things such as printing out the 
body of the HTTP response which would hold the same JSON that was outputted in the browser when we navigated to the same url. Let’s expand our program to extract our pokemon’s name and the HTTP headers that were returned:


"""


# prueba: 2 - printing out the body of the HTTP response
"""

"""
import requests
import json

def main2():
    req = requests.get('https://elpais.com')

    #req = requests.get('http://pokeapi.co/api/v2/pokemon/1/')
    print("HTTP Status Code: " + str(req.status_code))
    print(req.headers)
    json_response = json.loads(req.content)
    print("Pokemon Name: " + json_response['name'])


"""

"""


# prueba: 3 - Making POST Requests
"""

"""
def main3():
    req = requests.post('http://api/user', data=None, json=None)
    print(req)

"""

"""


# prueba: 4 -

"""

"""


"""

"""


if __name__ == '__main__':
    # prueba: 1 -
    main1()

    # prueba: 2 -
    main2()

    # prueba: 3 -
    main3()

    # prueba: 4 -

    exit(0)