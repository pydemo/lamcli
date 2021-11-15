if 0:
    from pyngrok import ngrok

    # Open a tunnel to MySQL with a Reserved TCP Address
    # <NgrokTunnel: "tcp://1.tcp.ngrok.io:12345" -> "localhost:3306">
    a=ngrok.connect(3000, bind_tls=True)
    print(dir(a))
    print(a.public_url)

from pyngrok import ngrok
a=ngrok.connect(3000, bind_tls=True)
ngrok_process = ngrok.get_ngrok_process()
print(dir(ngrok_process))
try:
    # Block until CTRL-C or some other terminating event
    ngrok_process.proc.wait()
except KeyboardInterrupt:
    print(" Shutting down server.")

    ngrok.kill()
    