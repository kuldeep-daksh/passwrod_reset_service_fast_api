import ldap3
changes_done = "test2"
changes_done = "test3"
SERVER='80.0.0.108'
BASEDN="OU=Delhi AISGlass,OU=AIS Users,DC=asahiindia,DC=com"
USER="test3@asahiindia.com"
CURREENTPWD="P@ssword@1234"
NEWPWD="P@ssword@12345679"

SEARCHFILTER='(&(userPrincipalName='+USER+')(objectClass=person))'
print(SEARCHFILTER)
USER_DN=""
USER_CN=""

ldap_server = ldap3.Server(SERVER, get_info=ldap3.ALL)
conn = ldap3.Connection(ldap_server, USER, CURREENTPWD, auto_bind=True)
conn.start_tls()
print(f"conn is = {conn}")
conn.search(search_base = BASEDN,
         search_filter = SEARCHFILTER,
         search_scope = ldap3.SUBTREE,
         attributes = ['cn', 'givenName', 'userPrincipalName'],
         paged_size = 5)

print(conn.entries)
for entry in conn.response:
    print(f"entry is {entry}")
    if entry["dn"] and entry["attributes"]:
        if entry.get("attributes").get("userPrincipalName"):
            if entry.get("attributes").get("userPrincipalName") == USER:
                USER_DN=entry.get("dn")
                USER_CN=entry.get("attributes").get("cn")

print("Found user:", USER_CN)

if USER_DN:
    print(USER_DN)
    print(ldap3.extend.microsoft.modifyPassword.ad_modify_password(conn, USER_DN, NEWPWD, CURREENTPWD,  controls=None))
else:
    print("User DN is missing!")