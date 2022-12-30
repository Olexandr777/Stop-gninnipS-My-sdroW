def spin_words(sentence):
    # Your code goes here
    new_lst=[]
    for i in sentence.split():
        if len(i) > 4:
            new_lst.append(i[::-1])
        else:
            new_lst.append(i)
    return " ".join(new_lst)
  
