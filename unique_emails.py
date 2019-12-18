
def UniqueEmails(email_list):
    unique_one = set()
    for email in email_list:
        before, after = email.split('@')
        if '+' in before:
            before = before[:before.index('+')]
        unique_one.add(before.replace('.','') + '@' + after)
    return len(unique_one),unique_one
        

input_list = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
uni_set = UniqueEmails(input_list)
print(uni_set)