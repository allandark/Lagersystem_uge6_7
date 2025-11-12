import { useState, useEffect } from 'react';
import { setToken, getToken, clearToken } from '../services/authService';
import { AuthLogin } from '../services/apiService';
// import { useNavigate } from 'react-router-dom';

type LoginFormProps = {
  onLoginSuccess: (token: string) => void;
};


export default function LoginForm({onLoginSuccess }:LoginFormProps) {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");

  const API_URL = import.meta.env.VITE_API_URL;

      async function handleLogin(){
        const res: string | null = await AuthLogin(API_URL, name, password);
        if (res != null){    
          onLoginSuccess(res);
        }
      }

  
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("handle submit")
    handleLogin();
  };

 
  return (
      <div>
        <form onSubmit={handleSubmit}>
        <label>Username:
          <input
            name="username"
            autoComplete="on"
            placeholder="username"
            type="text"
            value={name}
            onChange={e => setName(e.target.value)}
          />
        </label>
        <br />
        <label>Password:
          <input
            name="password"
            autoComplete="off"
            type="password"
            value={password}
            onChange={e => setPassword(e.target.value)}
          />
        </label>
        <br />
        <button
        type="submit"
        >Login</button>
        </form>
      </div>
    )}
