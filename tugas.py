#Mencoba strings
#Type string
string_0 = "Ayo coba string Python"
print(string_0)
print(type(string_0))

#String single quotes
string1 = 'ABCD'
print('\nSingle quotes')
print(string1)

#String double quotes
string2 = "HAHAHAHA"
print("\nDouble quotes")
print(string2)

#Triple Quotes
string3 = '''String "3"'''
print("\nTriple Quotes")
print(string3)


#Triple Quotes
#Multiple Line
string3 = '''String
Strong
Strength'''
print("\nTriple Quotes Multiple Line")
print(string3)

#Mengakses Karakter
string4 = "Call Of Duty"
print("\nInitial String: ", string4)
#Print Karakter Pertama
print("Karakter pertama:", string4[0])
#Print index negatif 
print("Karakter Terakhir:", string4[-1])

#Pemotongan String
string4 = "Call Of Duty"
print("Initial String: ")
print(string4)
# Printing 3rd to 12th character
print("\nSlicing characters from 3-12: ")
print(string4[0:2])
# Printing characters between
# 3rd and 2nd last character
print("\nSlicing characters between " +
"3rd and 2nd last character: ")
print(string4[1:-2])

