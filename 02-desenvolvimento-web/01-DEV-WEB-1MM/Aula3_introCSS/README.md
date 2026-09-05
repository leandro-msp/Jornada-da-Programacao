**Desenvolvimento WEB - AULA 3 - 04/09/2026**

# Introdução CSS

CSS (Cascading Style Sheet : Folhas de Estilo em Cascata): é uma linguagem de estilo utilizada em conjunto com HTML.
---

#### A sintaxe para CSS possui duas partes principais: um seletor e uma ou mais declarações.
* **Seletor:** indica qual tag HTML será aplicada uma determinada propriedade e formatação

* **Propriedade:** define qual o aspecto que será modificado
	* **valor:** vai junto a propriedade e indica definição exata dela, sendo assim:
	***seletor{propriedade:valor}***

**ex.:**
```bash
body{
	background-color: blue;
	}
```

## Vantages do CSS:
* Controle do layout de vários documentos a partir de uma simples folha de estilos
* Maior precisão de controle do layout
* Aplicação de diferentes  layouts para servir diferentes mídias (tela, impressora, etc).

## Métodos de Aplicação:
* **Inline:** diretamente na tag (como atributo):
```bash
<h1 style ="color:blue;">Texto</h1>
```
* **Interno:** estilos são definidos no cabeçalho da página (documento):
```bash
<style>
	h1{
		color:red;
	}
</style>
``` 
* **Externo:** Arquivo a parte (arquivo.css), arquivo que é chamado dentro do <head> atraveś da tag link:
```bash
<link rel="stylesheet" href="arquivo.css"/>
```		
> dentro do arquivo.css:
```bash
h1 {
	color:blue;
	font-size: 20px;
}
p {
	color:red;
}
```
## Identidade e Classes:
Para que a página seja apresentada uma forma mais organizada e a seleção dos elementos por CSS ocorram da melhor forma, podemos identificar as tags por classes e/ou identidades.

* **Identidade:** Uma id é uma identificação única e uma determinada id deve ser utilizada apenas uma vez no documento inteiro para um determinado elemento HTML.
> Para criar um id, um hashtah(#) antecede o nome escolhido para o Id(o nome não deve conter espaços, acentos, nem caracateres especiais, a sepração deve ser feita por underscore):
```bash
#nome_id{
propriedade:valor;
} 
```
Para utilizarmos o Id criado, devemos chamálo como atributo na tag escolhida. 
ex.:
```bash
<body id="nome_id">
```

* **Classes:**
A diferença entre as *classes*, e as identidades, é que as classes são reutilizáveis, ou seja você pode atribuir a vários elementos simuntaneamente.
> Criando um Seletor Classe (utiliza-se um ponto "." antes nome definido:
```bash
.nome_classe {
propriedade:valor;
}
```
Você pode criar diferentes estilos para parágrafos em um arquivo CSS, por exemplo, e utilizá-los nos parágrafos que quiser no documento HTML usando o atributo “class”junto ao elemento a se aplicar o estilo.
```bash
<p class="nome_classe">
```



	 
	 
