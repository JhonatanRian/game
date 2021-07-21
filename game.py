from models.Calculus import Calculus

def main() -> None:
    pontos: int = 0
    jogar(pontos)
    
def jogar(pontos: int) -> None:
    dificuldade: int = int(input("informe o nivel de dificuldade [1, 2, 3]: "))
    
    calc: Calculus = Calculus(dificuldade)
    
    print("Informe o resultado para a seguinte operação: ")
    calc.mostrar_operacao()
    
    resultado: int = int(input("»» "))
    
    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos}')
        
    continuar: int = int(input("Deseja continuar no jogo?[1-sim ou 0-não]\n»» "))
    
    if continuar:
        jogar(pontos)
    else:
        print(f"Voce finalizou com {pontos} pontos")
        

if __name__ == "__main__":
    main()