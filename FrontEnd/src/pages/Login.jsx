
import React, { useRef } from 'react';
import { useHistory } from 'react-router-dom';
import '../styles/Login.css';
import logo from '../assets/logo.png'

const Login = () => {
	const form = useRef(null);

	const handleSubmit = async (event) => {
		event.preventDefault();
		const formData = new FormData(form.current);
		const data = {
			carnet: formData.get('carnet'),
			password: formData.get('password')
		}

		const res = await fetch(`http://localhost:8080/estudiante`, {
			method: "POST",
			headers: {
			  "Content-Type": "application/json",
			},
			body: JSON.stringify({
				"carnet": data.carnet,
				"password":data.password
			}),
		  });

		const datasUser = await res.json();

		const  {logueado} = datasUser;

		if(logueado === true){
			
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
					{/* <a href="/">Inicio</a> */}
					
				</form>
				<button
					className="secondary-button signup-button"
				>
					Sing up
				</button>
			</div>
		</div >
	);
}

export default Login;