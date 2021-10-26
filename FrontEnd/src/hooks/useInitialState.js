import { useState } from 'react';

const initialState = {
    logueado: false,
    userInformation:[]
}

const useInialState = () =>{
    const [state,setState] = useState(initialState);

    const addAccesUser = ()=>{
        setState({
            ...state,
            logueado:true
        });
     
    }

    const logOutUser = () =>{
        setState({
            ...state,
            logueado:false
        });
        state.userInformation.pop()
    }


    const addInformatioUser = (information) =>{  
            console.log(information)
           state.userInformation.push(information)
            
         

    }
    return {
        state,
        addAccesUser,
        logOutUser,
        addInformatioUser
    }
}

export default useInialState;