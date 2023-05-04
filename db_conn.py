import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"path\to\oracle\21c\binaries")
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='xe') 
conn = cx_Oracle.connect(user=r'system', password='<redacted>', dsn=dsn_tns)
cursor = conn.cursor()

# if needed, place an 'r' before any parameter in order to address special characters such as '\'
c = conn.cursor()
c.execute(<query statement>) # use triple quotes if you want to spread your query across multiple lines
for row in c:
    #actions
    pass

 conn.close()
