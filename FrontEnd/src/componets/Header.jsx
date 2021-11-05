import React,{useContext} from 'react'
import AppContext from '../context/AppContext'
import { Link } from 'react-router-dom'
import '../styles/Header.css'
import Logo from '../assets/logo-horizontal .png'


const Header = () => {
    const {state,logOutUser,verifcationAdmin} = useContext(AppContext)
    
    const onClick = ()=>{
        logOutUser();
    }
    return (
        <div className='header'>
            <Link to="/"><img src={Logo} alt="no cargada" className="logo-header" /></Link>

            <nav>
                <ul className="nav__links">

                    <li><Link to="/apuntes-agregar">Apuntes </Link></li>
                    <li><Link href="/">Tareas</Link></li>
                    <li><Link href="/">Red de Cursos</Link></li>
                    {
                        verifcationAdmin()?<li><Link to="/reportes">Reportes</Link></li>:""
                    }

                </ul>
            </nav>
            <div className="nav__buttons">
                {
                    !state.logueado?<Link to="/login" className="btn_nav"><button className="button-nav">Log in</button></Link>
                    :<Link to="/login" className="btn_nav"><button className="button-nav" onClick={onClick}>Log out<output></output></button></Link>
                    
                }
                      {
                    !state.logueado?<Link to="/sing-up" className="btn_nav"><button className="button-nav">Sing Up</button></Link>
                    :""
                    
                }
                
                
              
              
            </div> 



        </div>

    )
}

export default Header
