import http.client
import mimetypes
from codecs import encode

conn = http.client.HTTPSConnection("api.twilio.com")
dataList = []
boundary = 'Your Private Twilio API keys account here'
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=To;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("+The phone number where to send"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=Body;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("Allö from Postman!"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=From;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("+Your number from Twilio"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=Media_Url;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("https://media.giphy.com/media/67itPVpEJmGuuNwZqJ/giphy.gif"))
dataList.append(encode('--'+boundary+'--'))
dataList.append(encode(''))
body = b'\r\n'.join(dataList)
payload = body
headers = {
  'Authorization': 'Your Private Twilio API keys account here ',
  'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
}
conn.request("POST", "/2010-04-01/Accounts/Your Private Twilio API keys account here/Messages.json", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))