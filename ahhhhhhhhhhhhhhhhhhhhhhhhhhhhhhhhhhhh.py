stock = ["a", "b", "c", "d", "e", "f", "g", "g"]

def main(item):
    x = 0
    if item in stock:
        for i in stock:
            x += 1
            if i == item:
                print(f"{item} is at position {x}")

main(item="g")
