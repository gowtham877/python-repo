def formula(new):
    jelly = new * 500
    jars = new / 1000
    crates = new /1000
    return jelly, jars, crates

jelly, jars, crates = formula(3000)
print jelly
print jars
print crates
