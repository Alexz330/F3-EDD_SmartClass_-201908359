import React from 'react'

const Reportes = () => {



    const leerJson = (event) => {
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
                    const res = await fetch(`http://localhost:8080/apuntesAgregar   `, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            "carnet":carnet,
                            "title": apunte["Titulo"],
                            "content": apunte["Contenido"]

                        }),
                    });

                })


            });

        }
        reader.readAsText(input.files[0], "UTF-8")
    }



    return (
        <div className="Reportes">
            <div className="Reportes_container">
                <input className="" type="file" placeholder="Cargar Apuntes" onChange={leerJson} />

            </div>
        </div>
    )
}

export default Reportes
