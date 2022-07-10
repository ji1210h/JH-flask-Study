import sqlite3
fruit = sqlite3.connect('fruit.db')

cur = fruit.cursor()

# Create table
cur.execute("""CREATE TABLE FRUIT(
    FRUIT VARCHAR(32),
    PRICE INT,
    QUANTITY INT
)""")

#Insert a row of data
cur.execute("INSERT INTO FRUIT VALUES('사과', 1000, 3)")
cur.execute("INSERT INTO FRUIT VALUES('포도', 2000, 5)")

# Save (commit) the changes
fruit.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
fruit.close()