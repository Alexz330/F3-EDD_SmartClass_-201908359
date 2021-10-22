import React from 'react'
import Header from '../componets/Header'

const Layoust = ({children}) => {
    return (
        <div>
           <div className="Layout">
			<Header/>
			{children}
		</div> 
        </div>
    )
}

export default Layoust
