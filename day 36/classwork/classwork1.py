#მომხმარებელს შემოატანინეთ სახელი და დაბეჭდეთ ის uppercase-ში
# იგივე სახელი დაბეჭდეთ lowercase-ში
#იგივე სახელი დაბეჭდეთ ისე, რომ მისი პირველი ასო იყოს uppercase-ში დაწერილი,
#  ხოლო დანარჩენი lowercase-ში


name=input("put your name here : ")
print(name.upper())
print(name.lower())
print(name.capitalize())

word="fish"
letter=input("put a letter pls : ")
print(word.find(letter))

if letter == -1:
    print("this symbol is not in word")
