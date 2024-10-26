import subprocess,os

test = os.popen('pip list').read()

if 'pyham_pe' not in test:
    subprocess.call('pip install pyham_pe')

import pe

class MyReceiveHandler(pe.ReceiveHandler):
    pass

def ready(*unused):
   pass


pe.tocsin.signal(pe.SIG_ENGINE_READY).listen(ready)

rh = MyReceiveHandler()

engine = pe.PacketEngine(rh)
# Connect to the server
print('trying to connect with server...')
engine.connect_to_server('195.230.110.49', 8000)

print(engine)