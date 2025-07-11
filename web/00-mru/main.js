import { $ } from "logger.js"
import { cE } from "./logger"

export const fruit = ["manzana", 'naranja']
const root = $(".section")
const filtter = $(".filtter")


export function addFruit() {
    fruit.forEach(element => {
      // crear y agregarla etiqueta html p
      let P = d.createElement('p')  
      // agregar el texto a la etiqueta html p 
      P.textCantent = el 
      // agregar el artiburto class a la etiqueta html p
      P.classlist.add("fruit")
      root.appendchild('p')
       
     // agregar los elementos de nuentra lista fruits
     // agregar los elementos otpion a nuetros elementos select(filtter)
     let option = cE("option")
     //agregar el texto a la etiqueta html p
     option.textCantent = el
     //agregar la etiqueta el aributos value a la etiqueta html option
     option.setAttribute("value", el)
     filtter.appendchild(option)
    })  
    
 }
 addFruit()
  