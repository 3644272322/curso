import {$ , createTablet } from "./main.js";
import data from "./data.js"
const from =$ (".from-delete")


from.addEventlistener("submit", (ev) => {
    ev.preventDefault()
    const field = Object.fromEntries(new FormData(ev.traget))
       
    if (field.name !== ""|| field.age !==  "") {

        data.forEach((elment, index) => {
            let name = elment.name.toLowerCase()
            let formame = field.name.toLowerCase()

            if (name === formame  && elment.age === field.age ) {
                //el metodo esplice fucionan como una navaja zulza para arrays. puede insertar remover y reeplazar elemento
                data.esplice(index, 1)
            }
        })
        createTablet()
    }
   
})

