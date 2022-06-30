import ldap
address = "80.0.0.108"
LDAP_BASE_DN = 'CN=Users,DC=tcplcoe,DC=com'
user_dn= 'CN=Administrator,CN=Users,DC=tcplcoe,DC=com'
old_password = "P@ssword@123"
new_password = "kuldeep123"
user_dn= "test3@asahiindia.com"

def changePassword(user_dn, old_password, new_password):
	ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
	l = conn = ldap.initialize('ldap://' + address)
	l.set_option(ldap.OPT_REFERRALS,0)
	l.set_option(ldap.OPT_PROTOCOL_VERSION,3)
	l.set_option(ldap.OPT_X_TLS,ldap.OPT_X_TLS_DEMAND)
	l.set_option(ldap.OPT_X_TLS_DEMAND,True)
	l.set_option(ldap.OPT_DEBUG_LEVEL,255)
	l.simple_bind_s("test3@asahiindia.com", old_password)

	# Reset Password
	unicode_pass = str('\"' + str(new_password) + '\"', 'iso-8859-1')
	password_value = unicode_pass.encode('utf-16-le')
	add_pass = [(ldap.MOD_REPLACE, 'unicodePwd', [password_value])]

	l.modify_s(user_dn,add_pass)

	# Its nice to the server to disconnect and free resources when done
	l.unbind_s()

y  = changePassword(user_dn, old_password,new_password)