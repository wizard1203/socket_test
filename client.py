import socket
import config
from settings import ai,ak,sk
from aip import AipSpeech
asp = AipSpeech(ai,ak,sk)
voice_path = './'
# server_IP = '0.0.0.0'
# server_PORT = 15678
message = 'I am Client\n'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((config.server_IP, config.server_PORT))
client.send(message.encode('utf-8'))
from_server = client.recv(4096)
modified_message = from_server.decode('utf-8')
client.close()

print(from_server)
print(modified_message)
ans = asp.synthesis(modified_message,'zh',1,{'vol':5,'per' : 2, 'pit' : 6,'spd' : 6,'cuid':123})
if not isinstance(ans, dict):
    with open(voice_path + 'audio.wav','wb') as f:
        f.write(ans)












