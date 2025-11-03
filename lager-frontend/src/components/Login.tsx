import { useState, useEffect  } from 'react';
import { setToken, getToken, clearToken } from '../authService';
import { useNavigate } from 'react-router-dom';
import "./Login.css"

export default function LoginForm() {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");
  const [token, setTokenState] = useState<string | null>(getToken());  
  const API_URL = import.meta.env.VITE_API_URL;
  const navigate = useNavigate();


    const sendLogin = async () => {
      try {
          console.log("Logging in")
          const loginModel = {
              "username": name,
              "password": password
          }        
          const res = await fetch(`${API_URL}/api/auth/login`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            credentials: 'include',
            body: JSON.stringify(loginModel),
          });
          console.log(`Res: ${res}`)
        
          const data = await res.json();          
          setToken(data.access_token);
          setTokenState(data.access_token);
           
          console.log("Login successfull")
          
        } catch (error) {
          console.error("Login error:", error); 
          clearToken();
        }
      };

      
    useEffect(() => {
        
        if (token) {
          console.log("Token found, redirecting...");
          navigate("/admin"); 
        }
      }, []);


  
  const handleSubmit = () => {
    // e.preventDefault();e: React.FormEvent
    sendLogin();
    navigate("/admin");
    
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
        <button>Login</button>
        </form>
      </div>
    )}
