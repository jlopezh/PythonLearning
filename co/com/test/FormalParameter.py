def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("=" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           "It's really very, VERY runny, sir Jose.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

"""Unpacking Argument Lists"""
var_keywords = {"shopkeeper":"Michael Palin","client":"John Cleese","sketch":"Cheese Shop Sketch"}
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           "It's really very, VERY runny, sir Jose.",
           var_keywords)