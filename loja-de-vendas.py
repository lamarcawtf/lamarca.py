import time
from rich.console import Console
from rich.table import Table

console = Console()

# Produtos e preços
produtos = {
    "coca cola": 6.00,
    "salgadinho": 3.50,
    "trident": 2.00
}

# Painel de produtos
console.print("\n[bold cyan]Produtos disponíveis:[/bold cyan]")
tabela = Table(title="Cardápio", show_header=True, header_style="bold magenta")
tabela.add_column("Produto", justify="left")
tabela.add_column("Preço (R$)", justify="right")

for nome, preco in produtos.items():
    tabela.add_row(nome.title(), f"{preco:.2f}")

console.print(tabela)

# Escolha dos produtos com quantidade
carrinho = []
while True:
    produto = console.input("[yellow]Digite o nome do produto (ou 'fim' para encerrar): [/yellow]").strip().lower()
    if produto == "fim":
        break
    if produto not in produtos:
        console.print("[red]Produto inválido![/red] Tente novamente.")
        continue
    try:
        quantidade = int(console.input(f"[yellow]Digite a quantidade de {produto.title()}: [/yellow]"))
        if quantidade <= 0:
            console.print("[red]Quantidade inválida![/red]")
            continue
    except ValueError:
        console.print("[red]Digite um número válido para a quantidade![/red]")
        continue
    carrinho.append((produto, quantidade))

if not carrinho:
    console.print("[red]Nenhum produto selecionado. Compra cancelada.[/red]")
    exit()

# Calcula o total
total = sum(produtos[p] * q for p, q in carrinho)

# Mostra itens comprados
console.print("\n[bold cyan]Resumo da compra:[/bold cyan]")
tabela_compra = Table(show_header=True, header_style="bold green")
tabela_compra.add_column("Produto", justify="left")
tabela_compra.add_column("Qtd", justify="center")
tabela_compra.add_column("Preço Unit.", justify="right")
tabela_compra.add_column("Subtotal", justify="right")

for item, qtd in carrinho:
    subtotal = produtos[item] * qtd
    tabela_compra.add_row(item.title(), str(qtd), f"{produtos[item]:.2f}", f"{subtotal:.2f}")

tabela_compra.add_row("[bold yellow]TOTAL[/bold yellow]", "", "", f"[bold yellow]{total:.2f}[/bold yellow]")
console.print(tabela_compra)

# Escolha do pagamento
console.print("\n[bold cyan]Métodos de pagamento:[/bold cyan] [green]debito[/green] | [green]credito[/green] | [green]pix[/green]")
pagamento = console.input("[yellow]Digite o método de pagamento: [/yellow]").strip().lower()

if pagamento not in ["debito", "credito", "pix"]:
    console.print("[red]Método de pagamento inválido![/red]")
    exit()

# ======= PAGAMENTO PIX =======
if pagamento == "pix":
    console.print(f"\n[bold cyan]Chave PIX:[/bold cyan] [yellow]lc7pix@firemail.com[/yellow]")
    console.print("[bold green]Aguardando pagamento...[/bold green]")
    time.sleep(3.5)
    console.print("[bold green]Pagamento aprovado com sucesso![/bold green]")

# ======= PAGAMENTO CRÉDITO =======
elif pagamento == "credito":
    try:
        parcelas = int(console.input("[yellow]Digite a quantidade de parcelas (1 a 12): [/yellow]"))
        if parcelas < 1 or parcelas > 12:
            console.print("[red]Número de parcelas inválido![/red]")
            exit()
    except ValueError:
        console.print("[red]Digite um número válido para parcelas![/red]")
        exit()
    
    total += 0.85
    console.print(f"\n[bold green]Total com taxa:[/bold green] R$ {total:.2f}")

    metodo_cartao = console.input("\n[cyan]Digite 1 para Aproximar ou 2 para Inserir o cartão: [/cyan]").strip()

    if metodo_cartao == "1":  # Aproximar
        console.print("[blue]Aproxime o cartão...[/blue]")
        time.sleep(7)
        console.print("[bold green]Compra aprovada![/bold green]")
    elif metodo_cartao == "2":  # Inserir
        senha = console.input("[yellow]Digite a senha do cartão: [/yellow]").strip()
        if senha == "lamarca":
            console.print("[blue]Processando...[/blue]")
            time.sleep(3)
            console.print("[bold green]Compra aprovada![/bold green]")
        else:
            console.print("[red]Senha incorreta![/red]")
            exit()
    else:
        console.print("[red]Opção inválida![/red]")

# ======= PAGAMENTO DÉBITO =======
elif pagamento == "debito":
    metodo_cartao = console.input("\n[cyan]Digite 1 para Aproximar ou 2 para Inserir o cartão: [/cyan]").strip()

    if metodo_cartao == "1":  # Aproximar
        console.print("[blue]Aproxime o cartão...[/blue]")
        time.sleep(7)
        console.print("[bold green]Compra aprovada![/bold green]")
    elif metodo_cartao == "2":  # Inserir
        senha = console.input("[yellow]Digite a senha do cartão: [/yellow]").strip()
        if senha == "lamarca":
            console.print("[blue]Processando...[/blue]")
            time.sleep(3)
            console.print("[bold green]Compra aprovada![/bold green]")
        else:
            console.print("[red]Senha incorreta![/red]")
            exit()
    else:
        console.print("[red]Opção inválida![/red]")

## README

"""
SISTEMA DE VENDAS NO TERMINAL COM PAGAMENTO SIMULADO
====================================================

Descrição:
----------
Este é um sistema simples de vendas em terminal, desenvolvido em Python. 
O usuário pode selecionar produtos, informar quantidades, visualizar o resumo da compra e simular pagamentos via PIX, crédito ou débito.

Tecnologias Utilizadas:
----------------------
- Python 3.x
- Biblioteca Rich (para exibição colorida e tabelas no terminal)

Instalação:
-----------
Certifique-se de ter Python 3 instalado e instale a biblioteca Rich com o comando:
pip install rich

Estrutura do Código:
-------------------
1. Importações:
   - time: usado para pausas temporais (time.sleep) para simular processamento.
   - rich.console.Console: exibe texto colorido e estilizado no terminal.
   - rich.table.Table: cria tabelas com colunas, cores e alinhamento.

2. Produtos e Preços:
   - Definidos em um dicionário chamado 'produtos', com nomes e preços.

3. Exibição do Cardápio:
   - Utiliza Table para mostrar produtos e preços de forma organizada e colorida.

4. Seleção de Produtos:
   - Usuário escolhe produtos digitando o nome.
   - Valida se o produto existe.
   - Solicita quantidade e valida se é um número positivo.
   - Adiciona ao carrinho.

5. Resumo da Compra:
   - Calcula total da compra.
   - Exibe uma tabela com produto, quantidade, preço unitário e subtotal.
   - Mostra o total final.

6. Escolha de Pagamento:
   - Opções: débito, crédito ou PIX.
   - Valida entrada do usuário.

7. Pagamento PIX:
   - Mostra chave PIX.
   - Simula espera com time.sleep.
   - Aprova automaticamente após a espera.

8. Pagamento Crédito:
   - Permite parcelamento de 1 a 12 vezes.
   - Adiciona taxa fixa de R$ 0,85 ao total.
   - Métodos: Aproximar ou Inserir cartão.
   - Se Inserir, solicita senha (senha correta: "lamarca").

9. Pagamento Débito:
   - Mesma lógica do crédito, sem taxa adicional.
   - Métodos: Aproximar ou Inserir cartão, valida senha.

Fluxo de Uso:
-------------
1. Exibe produtos disponíveis.
2. Usuário escolhe produtos e quantidades.
3. Mostra resumo da compra com subtotal e total.
4. Usuário escolhe método de pagamento.
5. Simula pagamento conforme método escolhido.
6. Compra aprovada ou encerrada conforme validação.

Observações:
------------
- Senha fixa para cartão: "lamarca".
- Taxa de crédito: adiciona R$ 0,85 ao total.
- Pagamentos são simulados, não reais.
- Biblioteca Rich é essencial para cores e tabelas.

Autor:
------
- Lamarca
"""
