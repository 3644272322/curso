//1. inicializar el canvas 
const canvas = document.querySelector("canvas")
const context = canvas.getContext("2d")
//configuarcion de la pantalla y el tamaño de los blques

const Black_SIZE = 20
const BOARD_WIDTH = 14
const BORAD_HEIGTH = 30
//creando el tablero del  tetris

context.scale(  Black_SIZE,Black_SIZE)

// 3. crear board de 30 filas
const board = [
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],

]
//4. la plaza del jugador
const pise = {
    position: { x:5, y:5 },
    shape: [
        [1,1,]
        [1,1,]
    ]
} 

// 2. game gloop - < es la parte mas importante esta es el area donde se dibujara nuestro ecenario 

function update() {
 drow()
 //loopin infinito o tambien conocido frucion recusivas
 // una funcion recusivas se llamar a si misma

  window.requestAnimationFrame(update)
}

function drow() {
   // vamos a dibujar nuestro board
   context.fillStyle="#222"
   context.fillRect(0,0, canvas.width, canvas.height)
   
   //pintar el bload

   board.forEach(HTMLTableRowElement.y) =>{

   }
    row .forEach(Value, x) => {

       if (Value=== 1)
           context.fillStyle ="red"
           context.fillRect (x, y, 1, 1)

    }

  }
    pise.shape.forEach((row, y))=> {
        row.forEach((value,x)=> {
           if.(value === 1)
              context.fillStyle = "yellow"
              context.fillRect(x + pise.position.x, y + pise.position.y)
            }
        })  

     })
 })

}
//5, mover la plaza

document.addEventListener("keydown", ev => {
    if (ev.key === "ArrowRight")
  }   pise.position.x++
       if (checkColllsion()){
         pise.position.x--
       }

})
    if (ev.key === "ArrowRight")
  }   pise.position.x++
       if (checkColllsion()){
         pise.position.x--
       }

})
}   pise.position.y++
if (checkColllsion()){
    pise.position.x--
   }
}
  if (ev.key === "Arrowup"){
    const rotated = []
    for (let 1 =0; 1- < pise.shape[0],length.)
 }

})
update()

