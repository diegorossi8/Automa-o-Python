from turtle import Turtle

t = Turtle()
t.speed(1)

continua = "s"

while continua == "s":
    direcao = input("Qual a direção que devo andar f-frente, t-trás, d-direita ou e-esquerda.\n")
    if direcao == "f":
        distancia = int(input("Quantos pixel devo percorrer?\n"))
        t.forward(distancia)
    elif direcao == "t":
        distancia = int(input("Quantos pixel devo percorrer?\n"))
        t.forward(distancia)
    elif direcao == "d":
        giro = int(input("Devo virar quantos graus a direita?\n"))
        t.right(giro)
        distancia = int(input("Quantos pixel devo percorrer?\n"))
        t.forward(distancia)
    elif direcao == "e":
        giro = int(input("Devo virar quantos graus a esquerda?\n"))
        t.left(giro)
        distancia = int(input("Quantos pixel devo percorrer?\n"))
        t.forward(distancia)
    continua = input("Se desejar continua s-sim ou para n-não.\n")
