
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
                        <h1>Bienvenido</h1>
                        <h2>{getNombre()}</h2>
                    </div>

                </div>

                <div className="User_bienvenida">
                    <div className="user__image__container">
                        <img className="user__image" src="https://mocah.org/uploads/posts/324859-House-Abstract-Forest-Digital-Art-Landscape-Illustration-4K-iphone-wallpaper.jpg" alt="" />
                    </div>
                </div>

            </div>

        </div>
    )
}

export default UserValidated
