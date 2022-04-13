import http.client

conn = http.client.HTTPSConnection("api.twilio.com")
payload = ''
headers = {
  'Authorization': 'Basic Your Twilio API private Key'
}
conn.request("GET", "/2010-04-01/Accounts/AC8e1aa13874f99448953050b950c46b73/Messages.json", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))