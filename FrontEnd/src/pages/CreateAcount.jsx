import React, { useRef} from 'react'
import { useHistory } from 'react-router-dom';
import "../styles/CreateAccount.css"
const CreateAcount = () => {

    const form = useRef(null)
    const history = useHistory();

    const handleSubmit = async e => {

        e.preventDefault();
        const formData = new FormData(form.current);
        const data = {
            carnet: formData.get('carnet'),
            dpi: formData.get('dpi'),
            nombre: formData.get('nombre'),
            carrera: formData.get('carrera'),
            correo: formData.get('correo'),
          
            password: formData.get("password"),
            edad: formData.get("edad")
        }


        const res = await fetch(`http://localhost:8080/agregarEstudiante`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },

            body: JSON.stringify({
                "carnet": data.carnet,
                "dpi":data.dpi,
                "nombre":data.nombre,
                "carrera":data.carrera,
                "correo":data.correo,
                "password": data.password,
                "edad":data.edad
            }),

        });
        
        history.push('/sing-up')

        console.log(data);
    }

    return (
        <div className="CreateAccount">
            <div className="CreateAccount-container">
                <h1 className="title">My account</h1>
                <form action="/" className="form" ref={form}>
                    <div>
                        <label for="carnet" className="label">Carnet</label>
                        <input type="text" name="carnet" placeholder="carnet" className="input input-name" />

                        <label for="dpi" className="label">dpi</label>
                        <input type="text" name="dpi" placeholder="dpi" className="input input-name" />

                        <label for="nombre" className="label">nombre</label>
                        <input type="text" name="nombre" placeholder="nombre" className="input input-name" />

                        <label for="nombre" className="label">carrera</label>
                        <input type="text" name="carrera" placeholder="carrera" className="input input-name" />

                        <label for="correo" className="label">correo</label>
                        <input type="text" name="correo" placeholder="Correo" className="input input-name" />

                        
                        <label for="password" className="label">Password</label>

                        <input type="password" name="password" placeholder="*********" className="input input-password" />

                        <label for="edad" className="label">edad</label>
                        <input type="text" name="edad" placeholder="edad" className="input input-password" />

                    </div>
                    <input type="submit" value="Create" className="primary-button login-button" onClick={handleSubmit} />
                </form>
            </div>
        </div>
    )
}

export default CreateAcount
