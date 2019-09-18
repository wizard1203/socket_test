import socket
import config
# server_IP = '0.0.0.0'
# server_PORT = 15678
send_message = '我是服务器'
content2='浸会大学异构计算实验室深度学习评测系统'
content3='浸会大学异构计算实验室'
content8='撑着油纸伞，独自。彷徨在悠长、悠长。又寂寥的雨巷。我希望逢着。一个丁香一样地。结着愁怨的姑娘。她是有。丁香一样的颜色。丁香一样的芬芳。丁香一样的忧愁。在雨中哀怨。哀怨又彷徨。她彷徨在这寂寥的雨巷。撑着油纸伞。像我一样。像我一样地。默默彳亍着。冷漠、凄清，又惆怅。她默默地走近。走近，又投出。太息一般的眼光。她飘过。像梦一般地。像梦一般地凄婉迷茫。像梦中飘过。一枝丁香地。我身旁飘过这女郎。她静默地远了、远了。到了颓圮的篱墙。走尽这雨巷。在雨的哀曲里。消了她的颜色。散了她的芬芳。消散了，甚至她的。太息般的眼光。丁香般的惆怅。撑着油纸伞，独自。彷徨在悠长、悠长。又寂寥的雨巷。我希望飘过。一个丁香一样地。结着愁怨的姑娘。'
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((config.server_IP, config.server_PORT))
serv.listen(5)
while True:
    print("wait connect")
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        # modified_RecvMessage, serverAddress = data.recvfrom(data.decode('utf-8'))
        modified_RecvMessage = data.decode('utf-8')
        if not data: break
        from_client += modified_RecvMessage
        print(from_client)
        conn.send(send_message.encode('utf-8'))
    conn.close()









