# from bs4 import BeautifulSoup
# import requests
# import requests.exceptions
# from urllib.parse import urlsplit
# from collections import deque
# import re

# # a queue of urls to be crawled
# new_urls = deque(['https://mail.google.com/mail/u/1/#inbox'])

# # a set of urls that we have already crawled
# processed_urls = set()

# # a set of crawled emails
# emails = set()

# # process urls one by one until we exhaust the queue
# while len(new_urls):

#     # move next url from the queue to the set of processed urls
#     url = new_urls.popleft()
#     processed_urls.add(url)

#     # extract base url to resolve relative links
#     parts = urlsplit(url)
#     base_url = "{0.scheme}://{0.netloc}".format(parts)
#     path = url[:url.rfind('/')+1] if '/' in parts.path else url

#     # get url's content
#     print("Processing %s" % url)
#     try:
#         response = requests.get(url)
#     except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
#         # ignore pages with errors
#         continue

#     # extract all email addresses and add them into the resulting set
#     new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
#     emails.update(new_emails)

#     # create a beutiful soup for the html document
#     soup = BeautifulSoup(response.text)

#     # find and process all the anchors in the document
#     for anchor in soup.find_all("a"):
#         # extract link url from the anchor
#         link = anchor.attrs["href"] if "href" in anchor.attrs else ''
#         # resolve relative links
#         if link.startswith('/'):
#             link = base_url + link
#         elif not link.startswith('http'):
#             link = path + link
#         # add the new url to the queue if it was not enqueued nor processed yet
#         if not link in new_urls and not link in processed_urls:
#             new_urls.append(link)

import imaplib
import email
from email.header import decode_header
import HTMLParser


# to unescape xml entities
_parser = HTMLParser.HTMLParser()

def decodeHeader(value):
  if value.startswith('"=?'):
    value = value.replace('"', '')

  value, encoding = decode_header(value)[0]
  if encoding:
    value = value.decode(encoding)

  return _parser.unescape(value)

def listLastInbox(top = 10):
  mailbox = imaplib.IMAP4_SSL('imap.gmail.com')
  mailbox.login('kampuskonnect.kk@gmail.com', 'Rish@1996')

  selected = mailbox.select('INBOX')
  assert selected[0] == 'OK'
  messageCount = int(selected[1][0])

  for i in range(messageCount, messageCount - top, -1):
    reponse = mailbox.fetch(str(i), '(RFC822)')[1]
    for part in reponse:
      if isinstance(part, tuple):
        message = email.message_from_string(part[1])
        # for h in ('subject','from','date'):
        #     if "Firebase" in decodeHeader(message['from']):
        #         print(decodeHeader(message['from']))
        yield {h: decodeHeader(message[h]) for h in ('subject', 'from', 'date') if "Firebase" in decodeHeader(message['from']) }

  mailbox.logout()


if __name__ == '__main__':
  for message in listLastInbox():
    print ('-' * 40)
    for h, v in message.items():
      print (u'{0:8s}: {1}'.format(h.upper(), v))






# def scramble(s1, s2):
#     # your code here
# #     print(list(s1),list(s2))
#     l = len(s2)
#     s1 = list(s1)
#     s2 = list(s2)
#     count = 0
#     for i in s2:
#         if i in s1:
#             count = count+1
# #             print(list(s1))
#             s1.remove(i)
# #             print(list(s1))
# #     if count == l:
# #         return True
# #     else:
# #         return False
#     print(count,l,len(s1))

# scramble('scriptjava','javascript')