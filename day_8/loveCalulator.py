def calculate_love_score(name1,name2):
    name1_lowercase=name1.lower()
    name2_lowercase=name2.lower()
    
    combined_string=name1_lowercase+name2_lowercase
    
    t=int(combined_string.count('t'))
    r=int(combined_string.count('r'))
    u=int(combined_string.count('u'))
    e=int(combined_string.count('e'))
    
    l=int(combined_string.count('l'))
    o=int(combined_string.count('o'))
    v=int(combined_string.count('v'))
    e=int(combined_string.count('e'))
    
    score=str(t+r+u+e)+str(l+o+v+e)
    print(score)
    
calculate_love_score("Kanye West", "Kim Kardashian")
    
