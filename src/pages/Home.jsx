import React from 'react'
import "../styles/Home.css"
import logo from '../assets/logo.png'
const Home = () => {
    return (
        <div className="Home">

            <section className="Bienvenida ">  
             <img src={logo} alt="logo" />
            </section>

            <div className="Contenedor_Bienvenida_imagen">
                <img className="Bienvenida_imagen" src="https://images.pexels.com/photos/7096/people-woman-coffee-meeting.jpg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260" alt="" />
            </div>

        </div>
    )
}

export default Home
