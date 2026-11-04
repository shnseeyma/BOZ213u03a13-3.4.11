beatles = []
print("Step 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

for i in range(2):
    isim = input("Eklenecek grup üyesini girin (Stu Sutcliffe / Pete Best): ")
    beatles.append(isim)
print("Step 3:", beatles)

del beatles[beatles.index("Stu Sutcliffe")]
del beatles[beatles.index("Pete Best")]
print("Step 4:", beatles)

beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

print("The Fab", len(beatles))
