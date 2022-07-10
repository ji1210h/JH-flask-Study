import sqlite3
fruit = sqlite3.connect('fruit.db')

cur = fruit.cursor()

# #Insert a row of data
# cur.execute("INSERT INTO FRUIT VALUES('수박', 3000, 1)")
# cur.execute("INSERT INTO FRUIT VALUES('복숭아', 1500, 7)")

# Save (commit) the changes
fruit.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
fruit.close()