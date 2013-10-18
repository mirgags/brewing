import MySQLdb as mdb
import sys
import pickle
from brew import *
import gc

gc.collect()

try:

    con = mdb.connect('localhost', 'brewuser', 'desade', 'brewing');

    filename = open('hop_list.pkl', 'rb')
    record = pickle.load(filename)
    cur = con.cursor()

    with con:
        cur = con.cursor()

        cur.execute("DROP TABLE IF EXISTS Hops")
        cur.execute("CREATE TABLE Hops (Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(255), Aau VARCHAR(255), Origin VARCHAR(255), Character VARCHAR(255))")

        for hop in record:
            cur.execute("INSERT INTO Hops(Name, Aau, Origin, Character) VALUES (%s, %s, %s, %s)" % (hop['hop'], hop['aau'], hop['origin'], hop['character']))

except mdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit (1)

con.close()
