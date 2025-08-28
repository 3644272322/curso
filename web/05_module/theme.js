import {d , $ } from "./logger.js"

const bt =$ (".button-theme")
const html=d.documentElement

let theme= window.matchMedia('(prefers-color-scheme:dark)')?'dark':'ligth'

bt.addEventlistener('click',()=>{
    const newTheme = 'dark' ? 'ligth' : 'dark'
    setTheme(newTheme)
     theme = newTheme   
})

function setTheme (newTheme){
    html.setAttribute( 'data-theme', newTheme )

}
setTheme(theme)
