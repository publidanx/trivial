def comenzar():

            responds = []
            correctas = 0
            num_pregunta = 1
    
            for key in questions:
                print("-------------")
                print(key)
                for i in opciones[num_pregunta-1]:
                    print(i)
                answer1= input("Elige: A, B o C")
                answer1= answer1.upper()
                responds.append(answer1)
                correctas += check_answer(questions.get(key),answer1)
                num_pregunta += 1
            ver_puntuación(responds,correctas)

#----------------------------------------------------------

def check_answer(answer1,correctas):
    if answer1==correctas:
        print("Buen trabajo!")
        return 1
    else:
        print("Incorrecto.")
        return 0
#------------------------------------------------------------
def ver_puntuación(responds,correctas):
    print("--------------------------")
    print("Resultados")
    print("--------------------------")
    
    print("Solución: ", end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    
    print("Respuesta dada: ")
    for i in responds :
        print(i,end=" ")
    print()
    score = int((correctas/len(questions))*100)
    print("Tu puntuación es "+str(score)+"%")

#--------------------------------------------------------------

def play_again():
    answng=input("Quieres jugar de nuevo? (Si/No)")
    answng= answng.upper()
    if answng=="SI":
        return True
    else:
        return False
#------------------------------------------------------------
questions= {"¿Quién descubrió América?: ":"A",
"¿Capital de Egipto?: " : "C",
"¿Sabes quién escribió 1984?: ":"B",
"¿Por qué cayó el imperio romano?: ":"A",
"¿Cuando fue creado el planeta tierra?: ":"B",
"¿Qué caracteriza a los arácnidos?":"A",
"¿Quién escribió 'La vida es sueño'?:":"B",
"¿Quién fue el primer trillonario de la historia?: ": "C"}


opciones = [["A. Cristóbal Colón.","B. Margaret tatcher","C. Isabel la Católica"],
["A. El Caido", "B. El Nilo","C. El Cairo"],
["A. Jorge Oruela","B. George Orwell","C. Georgi Stroyanovich"],
["A. El Cisma", "B. Los bárbaros","C. Por Cleopatra"],
["A. Hace miles de trillones de años","B. Antes que nacieras","C. Cuando Dios quiso"],
["A. Tener ocho patas.","B. Ser insectos","C. Utilizar seda y veneno"],
["A. Standley Kubrik","B. Calderon de la Barca","C. Shakespeare"],
["A. Bill Gates","B. Warren Buffen","C. Elon Musk"]]

comenzar()

while play_again():
    comenzar()
print("Adios!")


