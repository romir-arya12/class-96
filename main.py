introduction=input("Enter Your Introduction")
characterCount=0
wordCount=1
for i in introduction:
    characterCount+=1
    if(i==" "):
        wordCount+=1
print("Number of Words In a String")
print(wordCount) 
print("Number of Characters In a String")
print(characterCount) 