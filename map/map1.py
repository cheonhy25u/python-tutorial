original = [1,2,3,4,5]

def squared(x):
    return pow(x,2)

mapped = list(map(squared, original))

print(original)
print(mapped)