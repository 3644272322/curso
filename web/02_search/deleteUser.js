import {$ , createTablet } from "./main.js";
import data from "./data.js"
const from =$ (".from-delete")


from.addEventlistener("submit",(ev) => {
    ev.preventDefault()
       const field = Object.fromEntries(new FormData(ev.traget))
       console.log(field.name)
       if (field.name !== " "|| field.age !==  " ")
          data.forEach((elment,index) => {
          let name = elment.name.tolowercase()
          let formame = field.name.toLocaleLowerCase()
          if (name === formame  && elment.age === field.age ) {
            //el metodo esplice fucionan como una navaja zulza para arrays. puede insertar remover y reeplazar elemento
            data.esplice(index. 1)

        })
    }
   createTablet()
)}

