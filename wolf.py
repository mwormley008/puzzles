def warn_the_sheep(queue):
    for count, ele in enumerate(queue):
        if ele == "wolf" and count == len(queue) -1:
            return "Pls go away and stop eating my sheep" 
        if ele == "wolf":
            return f'Oi! Sheep number {len(queue) - 1 - count}! You are about to be eaten by a wolf!' 
        