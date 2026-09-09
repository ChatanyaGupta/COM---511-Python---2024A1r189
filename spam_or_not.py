#wap to detect whether a comment is pam or not. A comment should be treated as spam if it contains any of these keywords : "make a lot of money" , "buy now", "subscribe this", or "click this"

comment = input("Enter the Comment ")
if "make a lot of money" in comment or "buy now" in comment or "subscribe this" in comment == "click this":
    print("Comment is spam")
else:
    print("Comment is not spam")