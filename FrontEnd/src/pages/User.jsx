import AppContext from '../context/AppContext';
import React, { useContext } from 'react';
import UserError from '../componets/UserError';
import UserValidated from '../componets/UserValidated';

const User = ({ nombre }) => {
  const { state } = useContext(AppContext)
  const {logueado,userInformation} = state
 
  
  if(logueado){
    return(
      <>
        <UserValidated userInformation={userInformation}/>
      </>
    )
  }else{
    return(
      <div className="">
        <UserError />
      </div>
    )
  }
   
  
}

export default User
