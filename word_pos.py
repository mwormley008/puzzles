def order(sentence):
    solution_sentence = []
    for i in sentence.split():
        solution_sentence.append(str(i))
    print(solution_sentence)
    for i in sentence.split():
        print(i)
        for x in [*i]:
            print(x)
            if x.isdigit() == True:
                print(x)
                print(i)
                solution_sentence[int(x)-1] = i 
        
    return ' '.join(solution_sentence)