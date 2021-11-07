import React, { useContext, useEffect, useState } from 'react'
import AppContext from '../context/AppContext';
import UserError from '../componets/UserError';
import { Link } from 'react-router-dom'

const ListaApuntes = () => {

    const { state, getCarnet, getNombre } = useContext(AppContext)
    const { logueado, userInformation } = state
    const [apuntes, setApuntes] = useState([])




    const API = `http://localhost:5000/ObtenerApuntes`

    useEffect(() => {
        const obtenerApuntes = async () => {
            const res = await fetch(API, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    "carnet": getCarnet(),

                }),
            });

            const respuesta = await res.json()
            setApuntes(respuesta.apunte)
            console.log(apuntes)


        }
        obtenerApuntes();

    }, [API])


    if (logueado) {
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

                    <section className="Apuntes__table">
                        <table class="styled-table">
                            <thead>
                                <tr>    
                                <th>No</th>
                                    <th>Apunte</th>
                                    <th>Contenido</th>
                                </tr>
                            </thead>
                            <tbody>
                          {
                              apuntes.map((apunte,i)=>(
                                <tr class="active-row">
                                <td>{i}</td>
                                <td>{apunte.title}</td>
                                <td>{apunte.content}</td>
                            </tr>
                              ))
                          }
                            
                              
                            </tbody>
                        </table>

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

export default ListaApuntes
