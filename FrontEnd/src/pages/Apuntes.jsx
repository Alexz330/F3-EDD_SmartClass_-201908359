import React, { useContext,useRef } from 'react'
import AppContext from '../context/AppContext';
import UserError from '../componets/UserError';
import { Link } from 'react-router-dom'
import '../styles/Apuntes.css'

const Apuntes = () => {


    const form = useRef(null);
    const { state,getCarnet,getNombre } = useContext(AppContext)
    const { logueado, userInformation } = state

    const handleSubmit= async(event)=>{ 
        event.preventDefault();
        const formData =  new FormData(form.current);
        const data = {
            carnet: getCarnet(),
            title:formData.get('title'),
            content:formData.get('content')

        }

        const res = await fetch(`http://localhost:8080/apuntesAgregar`, {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({
				"carnet": data.carnet,
				"title": data.title,
                "content": data.content
			}),
		});



    }


    if (true) {
        return (
            <div className="Apuntes">
                <div className="Apuntes_container">

                    <section className="Apuntes_info">

                        <div className="Apuntes_nombre">
                            <samp><img className="Icon_person" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/OOjs_UI_icon_userAvatar.svg/120px-OOjs_UI_icon_userAvatar.svg.png" alt="" /></samp>
                            <h2 className="Apuntes_nombre__usuario">{getNombre()}</h2>
                        </div>

                        <Link to="/apuntes-agregar" className="btn_nav"><button className="button-nav">Nuevo Apunte</button></Link>
                        <Link to="/apuntes-ver" className="btn_nav"><button className="button-nav">Ver Apuntes</button></Link>
                    </section>
                    <br />

                    <form ref={form}>

                        <div className="Apuntes_titulo">
                            <label htmlFor="" className="title">carnet:{getCarnet()}</label>
                            <div className="Apuntes_titulo">

                                <label htmlFor="" className="title">Titulo:</label>
                                <input type="text" className="input" name="title"/>
                            </div>

                        </div>
                        <div className="Apuntes_text">
                            <textarea name="content" id="w3review" rows="20" cols="80" className="text_area" placeholder="Contenido">
                               
                            </textarea>
                        </div>
                        <div className="Apuntes_boton__guardar">
                            <button className="button-nav" onClick={handleSubmit}>Guardar</button>
                        </div>


                    </form>
                </div>
            </div>
        )
    } else {
        return (
            <div className="">
                <UserError />
            </div>
        )
    }


}


export default Apuntes
