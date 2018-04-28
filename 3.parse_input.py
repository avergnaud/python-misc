division = input("Quelle est la division ? ")
print ("division saisie : ", division)

# http://www.pythonforbeginners.com/dictionary/python-split

mon_tableau = division.split("/")
print("numérateur : ", mon_tableau[0])
print("dénominateur : ", mon_tableau[1])