import cx_Oracle

# Run the below command in CMD to set the path. instantclient_19_3 file is requried
# in order to connect to oracle DB from Python (and restart the System).
# set ORACLE_HOME=C:\Oracle\instantclient_19_3
# set PATH=%ORACLE_HOME%;%PATH%

class connectOracle():
    def connectDB(self):
        conn = cx_Oracle.connect("sysadm/sysadm@it002aia:1521/TEMMIG")
        cursor = conn.cursor()
        cursor.execute("select * from tablename")
        for row in cursor:
            print(row)