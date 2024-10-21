from typing import List
def analis_sentimientos (text:str):
    words:List = text.lower().split()
    
    positive_words:List = ["feliz", "divertido", "fantástico", "amor", "excelente"]
    negative_words:List = ["triste", "molesto", "terrible", "odio", "malo"]
    
    positive_matches:List = list(filter(lambda word: word in positive_words, words))
    negative_matches:List = list(filter(lambda word: word in negative_words, words))
    
    count_positive = len(positive_matches)
    count_negative = len(negative_matches)
    
    if count_positive > count_negative:
        return 'El texto tiene un tono positivo'
    elif count_negative > count_positive:
        return 'El texto tiene un tono negativo'
    else: return ' El texto es neuttro'

# text = """
# Este curso me hizo muy feliz porque pude comenzar a aprender un tema fundamental de python
# acerca de la progrmación funcional, es un curso fantástico  e interesante.
# En cuanto al instructor, solo puedo decir que es  muy dedicado, paciente y excelente en 
# lo que hace.
# """

text = """
Sin palabras, el curso es malo y el contenido es relmente triste y el instructor es terrible al 
momento de explicar los temas.
""" 

print(analis_sentimientos(text))


    
    