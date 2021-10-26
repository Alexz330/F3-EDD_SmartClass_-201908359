import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Layout from '../containers/Layout';
import Home from '../pages/Home';
import Login from '../pages/Login';
import CreateAcount from '../pages/CreateAcount';
import User from '../pages/User';
import AppContext from '../context/AppContext';
import useInialState from '../hooks/useInitialState';
// estilos globales 
import '../styles/global.css'

const App = () => {
	const initialState = useInialState();
	return (
		<AppContext.Provider value={initialState}>
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
		</AppContext.Provider>

	);
}

export default App;