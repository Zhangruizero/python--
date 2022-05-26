import zr_message

zr_message.send_message.send("hello")
txt = zr_message.receive_message.receive()
print(txt)