import{ $, $$ } from "logger.js"

const bt = $(".from-button")

form.ontsubmit=(ev)=>{
    ev.preventDefaul()
    const formData = new FormData(ev.target)
    const addData = formData.get("vel")
    addElement(addData)
}
