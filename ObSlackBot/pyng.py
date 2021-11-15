from pyngrok import ngrok

# Open a tunnel to MySQL with a Reserved TCP Address
# <NgrokTunnel: "tcp://1.tcp.ngrok.io:12345" -> "localhost:3306">
a=ngrok.connect(3000, bind_tls=True)
print(dir(a))
print(a.public_url)
