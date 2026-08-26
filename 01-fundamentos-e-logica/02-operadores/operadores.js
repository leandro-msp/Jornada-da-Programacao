//Os operadores em JS são semelhantes ao do PHP

// Aritiméticos

let a = 100;
let b = 200;
let c = 300;
let d = b;

console.log("Soma:", a+b);
console.log("Subtração:", c-b);
console.log("Mutiplicação", b*5);
console.log("Divisão: ", 1000/a);
console.log("Módulo/Resto: ", c%2);
console.log("Expoente:", 5**2);

//COMPARAÇÃO 

console.log("São iguais:", a==b); // false
console.log("Não são Iguais:", b!=c); // true
console.log("São idênticos:", d===b); // true
console.log("Não são Idênticos:", (a+b)!==(c)); // false

    // menor e maior | menor igual e maior igual
    console.log("é menor:", d<c);
    console.log("é maior:", d>b);
    console.log("é menor ou igual:", c<=(d+a));
    console.log("é maior ou igual:", (c-a)>=b);
    
//INCREMENTO/DECREMENTO

//Pré-incremento e pré-decremento

let i = 0;
let z = ++i;
    console.log("i:",i);
    console.log("z:",z);
z = --i;
    console.log("i:",i);
    console.log("z:",z);

//Pós-incremento e pós-decremento

z = i++;
    console.log("i",i);
    console.log("z:",z);
z= i--;
    console.log("i",i);
    console.log("z:",z);

//LÓGICOS

//! - NEGAÇÃO

let e = !(a==(d/2));
    console.log("E:",e);
    e = !(c===b); 
    console.log("E:",e);

//E - &&

let f = ((b>a) && (c==(b+a)));
    console.log("f:",f);
    f = ((d==200) && (200!==b));
    console.log("f:", f);

//OU - ||

let g = ((d>a) || (400<(b*2)));
    console.log("g:",g);
    g = ((a*3==(b)) || (200<d));
    console.log("g:",g);