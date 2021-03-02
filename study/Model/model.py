import random
import handle_message

print(random)
print(random.__file__)

handle_message.send_message.send("Hello world")
txt = handle_message.receive_message.receive()
print(txt)
