import React from 'react'
import { Link } from 'react-router-dom'
import '../styles/Header.css'
import Logo from '../assets/logo_sin_slogan.png'


const Header = () => {
    return (
        <div className='header'>
            <Link href="/"><img src={Logo} alt="no cargada" className="logo-header" /></Link>

            <nav>
                <ul className="nav__links">

                    <li><Link href="/">Apuntes </Link></li>
                    <li><Link href="/">Tareas</Link></li>
                    <li><Link href="/">Red de Cursos</Link></li>

                </ul>
            </nav>
            <div className="nav__buttons">
                <Link href="/index" className="btn_nav"><button>Login</button></Link>
                <Link href="/index" className="btn_nav"><button>Sing Up</button></Link>
            </div>



        </div>

    )
}

export default Header
