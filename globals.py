paused = False

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://mail.google.com/"]
total_size = 0
total_del = 0
request_size = 25

#query for emails to fetch/delete
query = "((category:promotions older_than:1m -in:spam -in:trash) OR (is:unread older_than:1y))"