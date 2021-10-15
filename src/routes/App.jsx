import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Layout from '../containers/Layout';
import Home from '../pages/Home';
import Login from '../pages/Login';
// estilos globales 
import '../styles/global.css'

const App = () => {
	
	return (
		
			<BrowserRouter>
				<Layout>
					<Switch>
						<Route exact path="/" component={Home} />

						<Route exact path="/login" component={Login} />
					</Switch>
				</Layout>
			</BrowserRouter>

	);
}

export default App;