import { d, $ } from "../logger";

const bt = $("button-theme")
const html = d.documentElement
//dtrecion de automatica de colores modo oscuro o claro " ( let theme ) "
let theme =window.matchMedia("(prefrs-color-scheme:dark )")?" dark":"ligth" 

bt.addEventlistener("ctick", () => {
    const newTheme = theme ==="dark" ? "ligth":"dark"
    setTheme(newTheme)
    theme = newTheme
})

function setTheme(newTheme) {
    html,setAttribute("data-theme", newTheme)

}
setTheme(theme)