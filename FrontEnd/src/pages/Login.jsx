
import React, { useRef, useContext, useState } from 'react';
import { useHistory } from 'react-router-dom';
import AppContext from '../context/AppContext';
//estilos
import '../styles/Login.css';
//logo
import logo from '../assets/logo.png'

const Login = () => {

	const form = useRef(null);

	//contexto del estado 
	const { addAccesUser, state,addInformatioUser, } = useContext(AppContext)
	const history = useHistory();

	const [uservalidated, setUserValidated] = useState(true)

	const handleSubmit = async (event) => {
		event.preventDefault();

		const formData = new FormData(form.current);

		const data = {
			carnet: formData.get('carnet'),
			password: formData.get('password')
		}

		const res = await fetch(`http://localhost:5000/estudiante`, {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({
				"carnet": data.carnet,
				"password": data.password
			}),
		});

		const datasUser = await res.json();
		
		const { userValided } = datasUser;

		if (userValided === true) {
			addInformatioUser(datasUser)
			setUserValidated(true)
			
			addAccesUser();
			history.push('/user')
		} else {
			console.log("usuario no valido")
			setUserValidated(false)
			console.log(uservalidated)
		}
	}

	return (
		<div className="Login">
			<div className="Login-container">
				<img src={logo} alt="logo" className="logo" />

				<form action="/" className="form" ref={form}>
					<label htmlFor="carnet" className="label">carnet</label>
					<input type="text" name="carnet" placeholder="201900000" className="input input-email" />
					<label htmlFor="password" className="label">Password</label>
					<input type="password" name="password" placeholder="*********" className="input input-password" />
					<button
						type="submit"
						onClick={handleSubmit}
						className="primary-button login-button">
						Log in
					</button>
				</form>

				<button
					className="secondary-button signup-button"
				>
					Sing up
				</button>

				{
					uservalidated ? "" : "Usuario no valido"
				}
			</div>
		</div >
	);
}

export default Login;