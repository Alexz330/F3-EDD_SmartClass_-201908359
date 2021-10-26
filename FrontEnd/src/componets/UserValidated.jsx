import React from 'react'

const UserValidated = ({userInformation}) => {
    
    return (
        <div>
            {
                userInformation.map((user)=>(
                    <div className="">
                        <h2>
                            {user.carnet}
                        </h2>
                        <h2>
                            {user.nombre}
                        </h2>
                        <h2>
                        </h2>
                        <h2>{user.DPI}</h2>
                    </div>
                ))
            }
        </div>
    )
}

export default UserValidated
