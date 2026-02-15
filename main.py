try:
    with open("list.txt", "r") as inp:
        # Har line se icon (first character/emoji) aur extra whitespace hatana
        sites = [line.strip().lstrip('🌐 ') for line in inp if line.strip().strip('🌐')]

    with open("newlist.txt", "w") as output:
        for s in sites:
            output.write("$boost=3, site="+ s + "\n")
            
    print("Task complete. Check newlist.txt")
except FileNotFoundError:
    print("Error: list.txt nahi mili.")
