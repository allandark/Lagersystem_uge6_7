import Layout from "../components/Layout";
import LoginForm from "../components/LoginForm";
import RegisterForm from "../components/Register";
import UserInfo from "../components/UserInfo";
import UserList from "../components/UserList";
import { setToken, getToken } from '../services/authService';
import { useState, useEffect } from 'react';

export default function AdminPage() {

    const [tokenState, setTokenState] = useState<string | null>(null);
    
    // useEffect(() => {   
            
    //     setTokenState(getToken());
    //     console.log(tokenState) 
    // }, []);


    return (
        <Layout>
         
            
        {tokenState ? (
        <div>
            <UserInfo/>
            {/* <RegisterForm/> */}
            {/* <UserList/> */}
        </div>
        ) : (
            <LoginForm onLoginSuccess={(token)=>{
                console.log(`Login Success - Token: ${token}`)
                setToken(token);
                setTokenState(token)}}/>
        )}

            
        </Layout>
    );
}