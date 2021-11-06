import React from 'react'
import '../styles/Reportes.css'

const Reportes = () => {

    const leerJsonApuntes = (event) => {
        const input = event.target
        const reader = new FileReader()
        reader.onload = async (event) => {
            const text = reader.result

            const json = JSON.parse(text)
            const valores = json.usuarios

            valores.forEach( (element, index) => {

                const carnet = element.carnet
                const apuntes = element.apuntes

                //console.log(carnet, "apuntes" + apuntes)

                apuntes.forEach(async(apunte,i) => {
                    console.log(apunte);
                    const res = await fetch(`http://localhost:5000/apuntesAgregar   `, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            "carnet":carnet,
                            "Título": apunte["Título"],
                            "Contenido": apunte["Contenido"]

                        }),
                    });

                })


            });

        }
        reader.readAsText(input.files[0], "UTF-8")
    }

    const leerJsonPensum = (event) => {
        const input = event.target
        const reader = new FileReader()
        reader.onload = async (event) => {
            const text = reader.result

            const json = JSON.parse(text)
            const Pensum = json.Cursos
            console.log(Pensum)
            const res = await fetch(`http://localhost:5000/agregarPensum   `, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            "pensum": Pensum

                        }),
                    });

        }
        reader.readAsText(input.files[0], "UTF-8")
    }




    const leerJsonEstudiantes = (event) => {
        const input = event.target
        const reader = new FileReader()
        reader.onload = async (event) => {
            const text = reader.result

            const json = JSON.parse(text)
            const Estudiantes = json.estudiantes

            console.log(Estudiantes)
            const res = await fetch(`http://localhost:5000/cargaMasivaEstudiantes   `, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            "estudiantes": Estudiantes

                        }),
                    });

        }
        reader.readAsText(input.files[0], "UTF-8")
    }




    const leerJsonEstudiantesCursos = (event) => {
        const input = event.target
        const reader = new FileReader()
        reader.onload = async (event) => {
            const text = reader.result

            const json = JSON.parse(text)
            const Estudiantes = json.Estudiantes
            
            console.log(Estudiantes)
            const res = await fetch(`http://localhost:5000/cargaMasivaCursos`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            "Estudiantes": Estudiantes

                        }),
                    });

        }
        reader.readAsText(input.files[0], "UTF-8")
    }
    
    return (
        <div className="Reportes">
            <div className="Reportes_container">
               <div className="Resportes_Apuntes">
                   <h2>
                       Carga De Apuntes
                   </h2>
               <input className="" type="file" placeholder="Cargar Apuntes" onChange={leerJsonApuntes} />

               <h2>
                       Carga De Pensum
                   </h2>
               <input className="" type="file" placeholder="Cargar Apuntes" onChange={leerJsonPensum}/>

               <h2>
                       Carga De Estudiantes
                   </h2>
               <input className="" type="file" placeholder="Cargar Apuntes" onChange={leerJsonEstudiantes}/>

               <h2>
                       Carga De Cursos para Estudiantes
                   </h2>
               <input className="" type="file" placeholder="Cargar Apuntes" onChange={leerJsonEstudiantesCursos}/>
               </div>

            </div>
        </div>
    )
}

export default Reportes
