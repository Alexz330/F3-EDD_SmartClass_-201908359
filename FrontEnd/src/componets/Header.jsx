import React from 'react'
import { Link } from 'react-router-dom'
import '../styles/Header.css'
import Logo from '../assets/logo-horizontal .png'


const Header = () => {
    return (
        <div className='header'>
            <Link to="/"><img src={Logo} alt="no cargada" className="logo-header" /></Link>

            <nav>
                <ul className="nav__links">

                    <li><Link href="/">Apuntes </Link></li>
                    <li><Link href="/">Tareas</Link></li>
                    <li><Link href="/">Red de Cursos</Link></li>

                </ul>
            </nav>
            <div className="nav__buttons">
                <Link to="/login" className="btn_nav"><button className="button-nav">Log in</button></Link>
                <Link to="/sing-up" className="btn_nav"><button className="button-nav">Sing Up</button></Link>
              
              
            </div> 



        </div>

    )
}

export default Header
