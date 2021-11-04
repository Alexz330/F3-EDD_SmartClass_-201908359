import React, { useContext } from 'react'
import AppContext from '../context/AppContext';
import UserError from '../componets/UserError';
import { Link } from 'react-router-dom'
import '../styles/Apuntes.css'

const Apuntes = () => {
    const { state } = useContext(AppContext)
    const { logueado, userInformation } = state


    console.log(userInformation)
    if (true) {
        return (
            <div className="Apuntes">
                <div className="Apuntes_container">

                    <section className="Apuntes_info">

                        <div className="Apuntes_nombre">
                            <samp><img className="Icon_person" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/OOjs_UI_icon_userAvatar.svg/120px-OOjs_UI_icon_userAvatar.svg.png" alt="" /></samp>
                            <h2 className="Apuntes_nombre__usuario">Nombre</h2>
                        </div>

                        <Link to="/sing-up" className="btn_nav"><button className="button-nav">Nuevo Apunte</button></Link>
                        <Link to="/sing-up" className="btn_nav"><button className="button-nav">Ver Apuntes</button></Link>
                    </section>
                    <br />
                    <section>

                        <div className="Apuntes_titulo">
                            <label htmlFor="" className="title">carnet:</label>
                            <div className="Apuntes_titulo">

                                <label htmlFor="" className="title">Titulo:</label>
                                <input type="text" className="input" />
                            </div>

                        </div>
                        <div className="Apuntes_text">
                            <textarea id="w3review" name="w3review" rows="20" cols="80" className="text_area">
                                At w3schools.com you will learn how to make a website. They offer free tutorials in all web development technologies.
                            </textarea>
                        </div>
                        <div className="Apuntes_boton__guadar">
                            <Link to="/sing-up" className="btn_nav"><button className="button-nav">Ver Apuntes</button></Link>
                        </div>


                    </section>
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
