import ldap

address = "80.0.0.108"
LDAP_BASE_DN = 'CN=Users,DC=asahiindia,DC=com'
user_dn = 'CN=Tarun Gupta,OU=Delhi AISGlass,OU=AIS Users,DC=asahiindia,DC=com'

new_password = "9050774794Kul!@1234"

user = "test2@asahiindia.com"
password = "P@ssword@123"
# import class and constants
enc_pwd = '"{}"'.format(new_password).encode('utf-16-le')
from ldap3 import Server, Connection, ALL, MODIFY_REPLACE, SUBTREE

server = Server(address, get_info=ALL)
print(server)
connection = Connection(server, user, password, auto_bind=True)
connection.search("CN=Tarun Gupta,OU=Delhi AISGlass,OU=AIS Users,DC=asahiindia,DC=com", '(objectclass=*)',
                  search_scope=SUBTREE, attributes=['*'])
print(connection.entries)
changes = {'unicodePwd': [(MODIFY_REPLACE, [enc_pwd])]}
y = connection.extend.microsoft.modify_password("CN=test 2,DC=asahiindia,DC=com", new_password)
print(y)