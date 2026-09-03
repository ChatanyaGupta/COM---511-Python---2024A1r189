'''6. write a python program to take a word and count the number of vowels a,e,i,o,u
word=input("Enter word:")
vowel=(word.count("a")+
       word.count("e")+
       word.count("i")+
       word.count("o")+
       word.count("u"))
print(vowel)
7.write a python program to take a sentence and replace all spaces with underscore

sen=input("Enter sentence:")
sen=sen.replace(" ","_")
print(sen)

9. write a python prog to take  aword and print it in reverse order using slicing.Also check whether it is the same forward and backward

word=input("Enter word:")
word1=word[::-1]
print(word)
print(word==word1)

10. Write a python prog to take first name and last name and print initials

name=input("Enter first name:")
name2=input("Enter second name:")
print(name[0],name2[0])

11. write a python prog to  take a word and print every second character

word=input("Enter word:")
print(word[1::2])

12. write a python prog to take a password and check whether it contains @ and has at least 8 characters

password=input("Enter Password: ")
password1=password.find("@") and len(password)>=8
print (password1)
13. write python program to take a string and seperate characters present at even index positions and odd index positions

word= input("Enter Word:")
print("eben position:", word[1::2])
print("Odd position:", word[0::2])

14. take an email address and check whether it contains @ and .com

email=input("Enter email:")
email1 = email.find("@")!=- email.find(".com")!=-1
print(email1)

15. take a semntence containg doubel spaces and unwanted spaces at the begining or end. Clean the sentence

sentence= input("enter sentence:")
sentence=sentence.replace("  "," ")
print(sentence.strip())
'''