
# - Developer: Ygor.

import sys
import requests
import os

os.system("cls||clear")

print ("""

▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▄░█░█▀█░██░██░███░█░▄▄▀█░▄▄▀█░▄▄
██▄▄▄▀▀█░▄▀█░▀▀░██░█░█░█░▀▀░█░▀▀▄█░▄▄
██░▀▀▀░█▄█▄█▀▀▀▄██▄▀▄▀▄█▄██▄█▄█▄▄█▄▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
 """)
print "Como usar skyware.py <target> "
load = ('sistema','adm/login.php','_painel','_sistema','gerenciar','login.php','admin/login.php','adm','admin.php','admin.html','login.php','login.html','administrator','admin','adminpanel','cpanel','login','wp-login.php','administrator','admins','logins','admin.asp','login.asp','adm/','admin/','admin/account.html','admin/login.html','admin/login.htm','admin/controlpanel.html','admin/controlpanel.htm','admin/adminLogin.html','admin/adminLogin.htm','admin.htm','admin.html','adminitem/','adminitems/','adm$
print

if len(sys.argv) >= 2:
   for x in load:
       target = sys.argv[1]
       z = target + x
       r = requests.get(z)
       if r.status_code == 200:
          print
          print '[✓] Pagina Encontrada: ' + z
          break
       else:
            if r.status_code != 200:
               print '[!] Falha: ' + z