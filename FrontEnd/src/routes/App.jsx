import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Layout from '../containers/Layout';
import Home from '../pages/Home';
import Login from '../pages/Login';
import CreateAcount from '../pages/CreateAcount';
import User from '../pages/User';
// estilos globales 
import '../styles/global.css'

const App = () => {
	
	return (
		
			<BrowserRouter>
				<Layout>
					<Switch>
						<Route exact path="/" component={Home} />

						<Route exact path="/login" component={Login} />
						<Route exact path="/sing-up" component={CreateAcount} />
						<Route exact path="/user" component={User} />
					</Switch>
				</Layout>
			</BrowserRouter>

	);
}

export default App;