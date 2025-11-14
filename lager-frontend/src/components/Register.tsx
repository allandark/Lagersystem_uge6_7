import { useState } from 'react';
import { getToken, setToken, clearToken } from '../services/authService';
// import { useNavigate } from 'react-router-dom';

export default function RegisterForm() {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");
  const [token, setTokenState] = useState<string | null>(getToken());
  // const navigate = useNavigate();
  const API_URL = import.meta.env.VITE_API_URL;

  const sendRegister = async () => {
    if (!token) {
      console.warn("No token found. Redirecting to login...");
      clearToken();
      setTokenState(null);
      // navigate("/admin");
      return;
    }

    try {
      const loginModel = { username: name, password: password };
      const res = await fetch(`${API_URL}/api/auth/register`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify(loginModel),
      });

      const data = await res.json();
      if (data.access_token) {
        setToken(data.access_token);
        setTokenState(data.access_token);
        // navigate("/admin");
      }
    } catch (error) {
      console.error("Register error:", error);
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    sendRegister();
  };

  return (
    <div className="flex justify-center items-center min-h-[70vh]">
      <div className="bg-gray-900/90 p-8 rounded-3xl shadow-[0_0_30px_rgba(255,0,255,0.5)] w-full max-w-sm">
        <h2 className="text-3xl font-bold text-pink-400 mb-6 text-center drop-shadow-[0_0_10px_rgba(255,0,255,0.7)]">
          Register New User
        </h2>
        <form onSubmit={handleSubmit} className="space-y-5">
          <div className="flex flex-col">
            <label className="text-pink-200 mb-1">Username</label>
            <input
              type="text"
              placeholder="Enter username"
              autoComplete="on"
              value={name}
              onChange={e => setName(e.target.value)}
              className="bg-gray-800/70 border border-pink-500/50 rounded-xl px-4 py-2 text-pink-200 placeholder-pink-400 focus:outline-none focus:ring-2 focus:ring-pink-400 transition"
            />
          </div>

          <div className="flex flex-col">
            <label className="text-pink-200 mb-1">Password</label>
            <input
              type="password"
              placeholder="Enter password"
              autoComplete="off"
              value={password}
              onChange={e => setPassword(e.target.value)}
              className="bg-gray-800/70 border border-pink-500/50 rounded-xl px-4 py-2 text-pink-200 placeholder-pink-400 focus:outline-none focus:ring-2 focus:ring-pink-400 transition"
            />
          </div>

          <button
            type="submit"
            className="w-full bg-pink-500/70 text-gray-900 font-bold py-2 rounded-xl shadow-[0_0_15px_rgba(255,0,255,0.7)] hover:bg-pink-400/70 hover:shadow-[0_0_20px_rgba(255,0,255,0.9)] transition"
          >
            Register
          </button>
        </form>
      </div>
    </div>
  );
}
