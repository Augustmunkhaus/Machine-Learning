#print listen af 5 bands ud
print("------list of bands---------")
bands = ["Fulci", "Cryptopsy", "Revocation", "Death", "Nile" ]
for band in bands:
    print(band)

#print den nye liste ud med et ekstra band
print("-------extra band--------")
bands.append("Septicflesh")
for band in bands:
    print(band)

#print listen ud hvor index 1 er slettet
print("------second value deleted---------")
bands.pop(1)
for band in bands:
    print(band)

#længden på listen
print("-------length--------")
length = len(bands)
print(length)

#reverse
print("-------reversed--------")
bands.reverse()
for band in bands:
    print(band)

