// import datos locales del archivo datas.js
// import { data } from "./data.js"; 
const $ = s => document.querySelector(s)
const section = document.querySelector(".main-section")
const from = $(".search")
console.log(from);


from.onsubmit = (ev) => {
    ev.preventDafaul()
    const field = new FormData(ev.target) 
    const search = field.get("search")
    console.log(field);
    
}


async function characters() {
    const res =  await fetch("https://rickandmortyapi.com/api/character") 
    if  (!res.ok) {
        console.error("error al recibir los datos del sevidor");
    }
    const data = await res.json()
    data.results.forEach(personaje => {
        const article = document.createRange().createContextualFragment(`
            <article class="card">
                <img class="image" src="${personaje.image}" />
                <p class="title">${personaje.name}
                </p>
            </article>  
        `)
        section.append(article)  

     })
    
}

characters() 