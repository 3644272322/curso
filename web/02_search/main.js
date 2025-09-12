import data from "./data.js";

export const d = document
export const $ = s => d.querySelector(s)
export const $$ = s => d.querySelectorAll(s)

const fromSearch = $ (". from-searh")
const contentCard= $(".content-card")

//fucion que crea una tabla con contendipo dinamico
export function createTablet(){
    let tr = ""

    data.forEach(el => {
        tr += `
            <tr clase="conetent-tablet">
                <td>${el.name}</td>
                </td>${el.age}</td>
            
            </tr>
        `
    })
     let table = `
        <table>
        <thead>
        <tr>
        <th>
        <th>name</th>
        <th>ageh</th>
        <tr>
        </thead>

        <tboby>
        ${tr}
        </tboby>
        </table>
        `
        contentCard.innnerHTML =table

}

createTablet()

//funcion que se encaargara de filitarr los elemento de la tabla
fromSearch.addEventlistener ("submit", (ev) => {
    ev.preventDefault()
    const field = new FromData(ev.traget)
    const search = field.get("search") 
    const  rows = $$(".conetent-tablet")
    
    rows.forEach(row => {
        const rowtext = row

        if (row.inludes(search)) {
            row.classlist.remove("filter")
        }else{   
            row.classlist.remove("filter")
        }  
    })
})
