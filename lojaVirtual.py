4
Maca = 5
banana = 7.50
Bife = 20
Morango = 20
Lichia = 25.99
Pneu = 300
Cadeira = 149.99
Figo = 9.99
Mesa = 400
Romã = 21
Monitor = 199.99
Mouse = 49.99
Vaso = 39.99
Teclado_Gamer = 249.99
Pão = 2.99
compra_total = 0
rep = 0

print(
 "Bem vindo a nossa loja virtual! Digite o numero do produto que você gostaria de encomendar para adicionarmos a seu carrinho. Saiba que que seu pedido for igual ou superior que R$500, você recebe um desconto de 10%"
)

def compra_online():
	global rep, compra_total
	
	pedido = int(input( " 1. Maçã (R$5,00) \n 2. Banana (R$7,50) \n 3. Kg de Picanha \n 4. Morango (R$20) \n 5. Lichia (R$25,99) \n 6. Pneu (R$300) \n 7. Cadeira Gamer (R$149,99) \n 8. Figo (R$9,99) \n 9. Mesa (R$400) \n 10. Romã (R$21) \n 11. Monitor (R$199,99) \n 12. Mouse (R$49,99) \n 13. Vaso (R$39,99) \n 14. Teclado Gamer (R$249.99 \n 15. Pão (R$2.99)) \n 16. Acabar pedido \n "))

	if (pedido == 1):
		compra_total += Maca
		compra_online()
	elif (pedido == 2):
		compra_total += banana
		compra_online()
	elif (pedido == 3):
		compra_total += Bife
		compra_online()
	elif (pedido == 4):
		compra_total += Morango
		compra_online()
	elif (pedido == 5):
		compra_total += Lichia
		compra_online()
	elif (pedido == 6):
		compra_total += Pneu
		compra_online()
	elif (pedido == 7):
		compra_total += Cadeira
		compra_online()
	elif (pedido == 8):
		compra_total += Figo
		compra_online()
	elif (pedido == 9):
		compra_total += Mesa
		compra_online()
	elif (pedido == 10):
		compra_total += Romã
		compra_online()
	elif (pedido == 11):
		compra_total += Monitor
		compra_online()
	elif (pedido == 12):
		compra_total += Mouse
		compra_online()
	elif (pedido == 13):
		compra_total += Vaso
		compra_online()
	elif (pedido == 14):
		compra_total += Teclado_Gamer
		compra_online()
	elif (pedido == 15):
		compra_total += Pão
		compra_online()
	elif (pedido == 16):
		finalizando_compra()
	else:
		print("Input invalido")
		compra_online()

def finalizando_compra():
	global compra_total
	confirmarCompra = int(input("O total de sua compra deu {compra_total:.2f} deseja proseguir? \n 1. Sim \n 2. Não\n"))
	if (confirmarCompra == 1):
		print("O valor total de sua compra deu," ,round(compra_total, 2) , "  (Sem desconto)")
		if (compra_total >= 500):
			compra_total *= 0.90
			print(f"Como o valor total de sua compra deu 500 reais ou mais, você recebeu um desconto de 10%, o seu novo valor a pagar é de \n R$ {compra_total:.2f}")
			print("FIM DO PROGRAMA!")

		else:
			print("Total a pagar:" ,round(compra_total, 2 ))
			print("FIM DO PROGRAMA!")
	elif (confirmarCompra == 2):
		compra_online()
	else:
		print("Input invalido")
		finalizando_compra()

compra_online()