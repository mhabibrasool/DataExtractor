# -*- Mohammad Habib Rasool
# Email extractor tool !

# import the libraries
from ast import walk
import yaml
import email
import imaplib

with open(r"C:\Users\HP\PycharmProject\PyProject\dont_share_credential.yml") as f:
    content = f.read()
    
# from credential yml import username and password
my_credential = yaml.load(content, Loader = yaml.FullLoader)

# Load the username and password from yaml file
username, password = my_credential["username"], my_credential["password"]

# URL for imap connection
imap_url = "imap.gmail.com"

# Correction with gmail using URL
my_mail = imaplib.IMAP4_SSL(imap_url)

# Loging in using credential
my_mail.login(username, password)

# Selecting the index to fetch message
my_mail.select("Inbox")

key = "FROM"
value = "founders@dailycodingproblem.com"
_, data = my_mail.search(None, key, value)
mail_id_list = data[0].split()

msgs = []

for num in mail_id_list:
    typ, data = my_mail.fetch(num, "(RFC822)")
    msgs.append(data)
    
for msg in msgs[::-1]:
    for response_part in msg:
        if type((response_part)) in tuple:
            my_msg = email.messages_from_bytes((response_part[1]))
            print("________________________")
            print("subj: ", my_msg["subject"])
            print("from: ", my_msg["from"])
            print("body")
            for part in my_msg.walk():
                print(part.get_content_type())
                if part.get_context_type()=="text/plain":
                    print(part.get_payload())