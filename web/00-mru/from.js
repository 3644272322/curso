import{ $, $$ } from "logger.js"
import { fruits, addFruits } from "./main.js"

const form = $(".from")

form.ontsubmit=(ev)=>{
    ev.preventDefaul()
    const formData = new FormData(ev.target)
    const addData = formData.get("vel")
    fruits.push(addEl)
    console.log(fruits)
    addFruits()
}

