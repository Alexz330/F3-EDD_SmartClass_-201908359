
import AppContext from '../context/AppContext';
import React, { useContext } from 'react';
import '../styles/User.css'
const UserValidated = ({ userInformation }) => {
    const { getNombre } = useContext(AppContext)
    return (
        <div className="User">
            <div className="User_container">



                <div className="User_informacion">
                    <div className="">
                        <h1 className="User_title__Bienvenida">Bienvenido</h1>
                        <h2 className="User_nombre">{getNombre()}</h2>
                    </div>

                </div>

                <div className="User_bienvenida">
                    <div className="user__image__container">
                        <img className="user__image" src="https://mocah.org/uploads/posts/104228-flat-forest-deer-4k-5k-iphone-wallpaper-abstract.jpg" alt="" />
                    </div>
                </div>

            </div>

        </div>
    )
}

export default UserValidated
