import { $ } from " .logger.js"

form.ontsubmit=(ev)=>{
    ev.preventDefault()
    const formData = new FormData(ev.target)
    const addEle = formData.get('element')
    console.log(addEle);
    
    
} 