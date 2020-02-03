new = s.strip() --> strip function will remove trailing and leading whitespaces in a string.
new = new.split( ) -- > split will convert the string to list. Did this so that I can revrese list using ::-1 slice
return ' '.join(new[::-1]) --> join function will convert the reversed list back to string.
