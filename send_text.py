from twilio import rest
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC35958db98dbb68dae098d9d2483a7ba3"
auth_token  = "dd9dbd19d412c69311fc4450041e5d49"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="My name is Ron Burgandy?",
    to="+18089549353",    # Replace with your phone number
    from_="+15672120058") # Replace with your Twilio number
print message.sid
