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

    const getCarnet= ()=>{
        if (state.userInformation[0] === undefined){
            console.error("usuario no encontrado")
        }else{
            return state.userInformation[0]["carnet"]
        }
            
    }

    const verifcationAdmin=()=>{
        if (state.userInformation[0] === undefined){
            console.error("usuario no encontrado")
        }else{
            if (state.userInformation[0]["admin"] === true){
                return true
            }else{
                return false
            }
            
        }
    }


    const getNombre= ()=>{
        if (state.userInformation[0] === undefined){
            console.error("usuario no encontrado")
        }else{
            return state.userInformation[0]["nombre"]
        }
            
    }


       
    
    return {
        state,
        addAccesUser,
        logOutUser,
        addInformatioUser,
        getCarnet,
        getNombre,
        verifcationAdmin
    }
}

export default useInialState;