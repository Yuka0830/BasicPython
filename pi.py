text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

words=text.replace(",","").replace(".","").split()
length=list(map(len,words))
print(''.join(map(str,length)))