def stock_availability(data, command, *args):
    if command == "delivery":
        return data + list(args)
    elif command == "sell":
        if not args:
            return data[1:]
        else:
            if type(args[0]) == int:
                return data[args[0]:]
            else:
                for el in args:
                    if el in data:
                        while data.count(el):
                            data.remove(el)
                return data


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
