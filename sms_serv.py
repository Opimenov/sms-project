#!/usr/bin/env python

import sys
import imaplib
import getpass
import email
import datetime

def put_stuff_into_file(stuff):
    print 'putting stuff into file'
    print stuff[0]
    print stuff[1]

def read_emails(M):
  res_code, data = M.search(None, "ALL")
  if res_code != 'OK':
      print "No messages found!"
      return

  for num in data[0].split():
      res_code, data = M.fetch(num, '(RFC822)')
      if res_code != 'OK':
          print "ERROR getting message", num
          return

      msg = email.message_from_string(data[0][1])
      title = msg['Subject']
      phone_num =int(filter(str.isdigit, title))
      print phone_num
      body = ""

      if msg.is_multipart():
          for part in msg.walk():
              ctype = part.get_content_type()
              cdispo = str(part.get('Content-Disposition'))
              # skip any text/plain (txt) attachments
              if ctype == 'text/plain':
                  body = part.get_payload(decode=True)  # decode
                  break
                  # not multipart - i.e. plain text, no attachments, keeping fingers crossed
      else:
                  body = msg.get_payload(decode=True)
      print body.splitlines()[2]
      put_stuff_into_file((phone_num,body.splitlines()[2]))


#wrap this in a loop and execute it once in a while to get info
M = imaplib.IMAP4_SSL('imap.gmail.com')

try:
    #very bad idea to hardcode password 
    #use this instead getpass.getpass()
    #but it saves time
    M.login('ghana.sms.project@gmail.com', 'ghanasmsproject') 

except imaplib.IMAP4.error:
    print "LOGIN FAILED!!! "
    # ... exit or deal with failure...

#see what we've got from the mail server'
res_code, mailboxes = M.list()

# if res_code == 'OK':
#     print "Mailboxes:"
#     print mailboxes

res_code, data = M.select("INBOX")

if res_code == 'OK':
    read_emails(M) # ... do something with emails
    M.close()

M.logout()




