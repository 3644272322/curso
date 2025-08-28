import { $ , d } from ". /logger.js"
//definir variables

export const fruits = ["manzana","naranja", "platano"]
const root =$('.main') 


fruits.forEach(el =>{
let p = d.createElement('p')
 p.textcontent = el 
 root.appendChild(p)


})

