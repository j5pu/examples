# Connections
## [Mongo DB Compass](https://downloads.mongodb.com/compass/mongodb-compass-community-1.19.12-darwin-x64.dmg)
````shell script
open https://downloads.mongodb.com/compass/mongodb-compass-community-1.19.12-darwin-x64.dmg
open /Applications/MongoDB\ Compass\ Community.app
````
    atlas0-mzvey.mongodb.net
    SSL

## Mongo Shell
```shell script
brew install mongodb/brew/mongodb-community-shell
mongo "mongodb+srv://atlas0-mzvey.mongodb.net/admin"  --username fp
```
    
## Python
````python
from pymongo import MongoClient

password = "1Zaragoza$."
encode = {"$": "%24", ".": "%2E"}
client = MongoClient("mongodb+srv://fp:1Zaragoza%24%2E@atlas0-mzvey.mongodb.net/test?retryWrites=true&w=majority")
````

## [App Flask](https://blog.pythonanywhere.com/178/)

````shell script
pip3.7 install --user Flask-PyMongo
/Users/fp/Library/Python/3.7/bin/flask
````
Usa los la base de datos "blog" creada en blog.py con "posts" y los lee con:  `blog_flask.py`
```shell script
export FLASK_APP=blog_flask.py
export FLASK_ENV=development
flask run
open http://127.0.0.1:5000/
```

    