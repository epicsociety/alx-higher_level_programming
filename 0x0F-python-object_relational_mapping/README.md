# object-relational mapping

**Everything you need to know is here**

sqlalchemy documentation - [link](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)

MySQLdb’s documentation - [link](https://mysqlclient.readthedocs.io/)

---
This is just a tip of the iceberg

```
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///example.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
```
> The skeleton for mysqldb is as follows

```
import MySQLdb

    '''Connect to the database'''
    conn = MySQLdb.connect(host='localhost', user='myuser', passwd='mypassword', db='mydatabase')

    '''Create a cursor object'''
    cur = conn.cursor()

    '''Execute a query'''
      cur.execute("SELECT * FROM mytable")

      '''Fetch the results'''
        rows = cur.fetchall()
```


## The most important thing to note
    - *sqlalchemy is an SQL toolkit and has the Object-Relational Mapping (ORM) library for Python*
    - *MySQLdb is a python module*


