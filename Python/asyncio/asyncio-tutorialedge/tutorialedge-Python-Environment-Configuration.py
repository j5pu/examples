#
import asyncio
import random


# prueba: 1 - Basic Example
"""
Defining a solid strategy for handling various environment 
configuration in your Python programs can drastically improve the way you deploy and manage different environments.

In the most basic of scenarios we would 
typically have 2 main environments, development and production. In our development environment we would do both our 
development and testing against the likes of non-production based databases and resources in order to prevent adding noise to our production environment.

In some scenarios you may have to pick up various environment variables from the machine 
running your Python application. In this tutorial I’m going to be showing you the best ways to access these environment variables.

Basic Example
Say we had a section of code that talks to a database. In development we would want it to talk to our development-only database, 
in production we would want it to talk to our larger production database. We may have code that looks like this:
"""
#import MySQLdb

#db = MySQLdb.connect("localhost", "devuser", "devpass", "devdatabase")

"""
When we want to push to production you may want to update the connection details to your production database and 
credentials. But doing this every time you make a release to production can be time-consuming and error-prone. What happens if we forget when we are deploying and our production environment ends up hitting a development database? In some scenarios this could be disastrous and cost millions in damages.

So how do we do this using environment variables?
"""


# prueba: 2 - System Environment Variables
"""
System Environment Variables
If we had two distinct servers to run our Python applications, we could set the environment variables db_username and db_password on each of our servers.

When our application starts up it would pick up our db_username and db_password environment variables and connect to the database using the appropriate credentials.

These are environment variables that can be read using the os module. If we wanted to read all of our environment variables we could use os.environ like so:
"""
import os
print(os.environ)
db_username = os.getenv('db_username', 'NULL')
db_password = os.getenv('db_password', 'NULL')

"""

"""


# prueba: 3 -
"""

"""


"""

"""


# prueba: 4 -

"""

"""


"""

"""


if __name__ == '__main__':
    # prueba: 1 -


    # prueba: 2 -


    # prueba: 3 -


    # prueba: 4 -

    exit(0)