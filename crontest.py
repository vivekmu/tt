#!/usr/bin/env python3
with open('/root/crontest.txt','w') as file2:
    file2.write('Cront test')

# crontab -e
#*/1 * * * * /usr/bin/python3 /root/crontest.py >> out.txt  2>&1
