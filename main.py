import alerts


client = alerts.Client(token="04fb0e20d084953e768100bbcfec463b81b1191aab2203")

for i in client.get_active():
    print(i)
