import { $ } from " .logger.js"

form.ontsubmit=(ev)=>{
    ev.preventDefault()
    const formData = new formData(ev.target)
    const addEle = formData.get('addEle')
    console.log(addEle);
    
  
} 