import React, { useContext, useRef } from 'react'
import AppContext from '../context/AppContext';
import UserError from '../componets/UserError';
import { Link } from 'react-router-dom'
import '../styles/Apuntes.css'
import '../styles/Cursos.css'


const Cursos = () => {

    const form = useRef(null);
    const formGrafica = useRef(null);
    const { state, getCarnet, getNombre } = useContext(AppContext)
    const { logueado, userInformation } = state


    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData(form.current);
        const data = {
            Carnet: getCarnet(),
            Codigo: formData.get('Codigo'),
            Nombre: formData.get('Nombre'),
            Creditos: formData.get('Creditos'),
            Prerequisitos: formData.get('Prerequisitos'),
            Obligatorio: formData.get('Obligatorio'),
            semestre: formData.get('semestre'),
            año: formData.get("año")
        }
        console.log(data)

        const res = await fetch(`http://localhost:5000/agregarcurso`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                "carnet": data.Carnet,
                "Codigo": data.Codigo,
                "Nombre": data.Nombre,
                "Creditos": data.Creditos,
                "Prerequisitos": data.Prerequisitos,
                "Obligatorio": data.Obligatorio,
                "semestre": data.semestre,
                "año": data.año
            }),
        });

       

    }



    const handleSubmitGrafica = async (event) => {
        event.preventDefault();
        const formData = new FormData(formGrafica.current);
        const data = {
            Carnet: getCarnet(),
            semestre: formData.get('semestre'),
            año: formData.get('año'),
        
        }

        const res = await fetch(`http://localhost:5000/reporteCursos`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                "carnet": data.Carnet,
                "semestre": data.semestre,
                "año": data.año,
             
            }),
        });
}





    return (
        <div className="Apuntes">
            <div className="Apuntes_container">

                <section className="Apuntes_info">

                    <div className="Apuntes_nombre">
                        <samp><img className="Icon_person" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/OOjs_UI_icon_userAvatar.svg/120px-OOjs_UI_icon_userAvatar.svg.png" alt="" /></samp>
                        <h2 className="Apuntes_nombre__usuario">{getNombre()}</h2>
                    </div>
                    <form action="" ref={formGrafica}>
                        <button className="button-nav" onClick={handleSubmitGrafica}>Ver cursos asigandos</button>

                        <div className="input__curso">
                            <label htmlFor="" className="title ">semestre:</label>
                            <input type="text" className="input" name="semestre" />
                        </div>
                        <div className="input__curso">
                            <label htmlFor="" className="title ">año:</label>
                            <input type="text" className="input" name="año" />
                        </div>
                    </form>
                </section>
                <br />

                <form ref={form}>

                    <div className="Apuntes_titulo">
                        <label htmlFor="" className="title">carnet:{getCarnet()}</label>


                    </div>
                    <h2>Agregar Curso</h2>
                    <div className="Apuntes_text__cursos">
                        <div className="input__curso">
                            <label htmlFor="" className="title ">codigo:</label>
                            <input type="text" className="input" name="Codigo" />
                        </div>
                        <div className="input__curso">
                            <label htmlFor="" className="title ">Nombre:</label>
                            <input type="text" className="input" name="Nombre" />
                        </div>
                        <div className="input__curso">
                            <label htmlFor="" className="title ">Creditos:</label>
                            <input type="text" className="input" name="Creditos" />
                        </div>
                        <div className="input__curso">
                            <label htmlFor="" className="title ">Prerequisitos:</label>
                            <input type="text" className="input" name="Prerequisitos" />
                        </div>
                        <div className="input__curso">
                            <label htmlFor="" className="title ">Obligatorio:</label>
                            <input type="text" className="input" name="Obligatorio" />

                        </div>
                        <div className="input__curso">
                            <label htmlFor="" className="title ">semestre:</label>
                            <input type="text" className="input" name="semestre" />
                        </div>
                        <div className="input__curso">
                            <label htmlFor="" className="title ">año:</label>
                            <input type="text" className="input" name="año" />
                        </div>

                    </div>
                    <div className="Apuntes_boton__guardar">
                        <button className="button-nav" onClick={handleSubmit}>Guardar</button>
                    </div>


                </form>
            </div>
        </div>
    )
}

export default Cursos
