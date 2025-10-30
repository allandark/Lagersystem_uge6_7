import { useState, useEffect } from 'react';
import { getToken, setToken } from '../authService';

export default function LoginForm() {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");
  


    const sendLogin = async () => {
      try {
        const loginModel = {
            "username": name,
            "password": password
        }
        console.log(loginModel)
        const res = await fetch("http://localhost:5000/api/auth/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(loginModel),
        });
        
          const data = await res.json();
          console.log("Login success:", data);
          setToken(data.access_token);
        } catch (error) {
          console.error("Login error:", error);
        }
      };


  
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    sendLogin();
  };

  const token = getToken();

  return (

    <div>
    {token ? (
      <div>Token exists: {token}</div>
    ) : (
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
            type="text"
            value={password}
            onChange={e => setPassword(e.target.value)}
          />
        </label>
        <br />
        <button>Login</button>
        </form>
      </div>
    )}
    </div>
    
  );}