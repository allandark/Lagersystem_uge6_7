import { useState } from 'react';
import { AuthLogin } from '../services/apiService';

type LoginFormProps = {
  onLoginSuccess: (token: string) => void;
};

export default function LoginForm({ onLoginSuccess }: LoginFormProps) {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");

  const API_URL = import.meta.env.VITE_API_URL;

  async function handleLogin() {
    const res: string | null = await AuthLogin(API_URL, name, password);
    if (res != null) {
      onLoginSuccess(res);
    }
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    handleLogin();
  };

  return (
    <div className="bg-gray-900/90 p-8 rounded-3xl shadow-[0_0_30px_rgba(0,255,255,0.5)] w-full max-w-sm">
      <h2 className="text-3xl font-bold text-cyan-300 mb-6 text-center drop-shadow-[0_0_10px_rgba(0,255,255,0.7)]">
        Admin Login
      </h2>
      <form onSubmit={handleSubmit} className="space-y-5">
        <div className="flex flex-col">
          <label className="text-cyan-200 mb-1">Username</label>
          <input
            type="text"
            placeholder="Enter username"
            autoComplete="on"
            value={name}
            onChange={e => setName(e.target.value)}
            className="bg-gray-800/70 border border-cyan-500/50 rounded-xl px-4 py-2 text-cyan-200 placeholder-cyan-400 focus:outline-none focus:ring-2 focus:ring-cyan-400 transition"
          />
        </div>

        <div className="flex flex-col">
          <label className="text-cyan-200 mb-1">Password</label>
          <input
            type="password"
            placeholder="Enter password"
            autoComplete="off"
            value={password}
            onChange={e => setPassword(e.target.value)}
            className="bg-gray-800/70 border border-cyan-500/50 rounded-xl px-4 py-2 text-cyan-200 placeholder-cyan-400 focus:outline-none focus:ring-2 focus:ring-cyan-400 transition"
          />
        </div>

        <button
          type="submit"
          className="w-full bg-cyan-500/70 text-gray-900 font-bold py-2 rounded-xl shadow-[0_0_15px_rgba(0,255,255,0.7)] hover:bg-cyan-400/70 hover:shadow-[0_0_20px_rgba(0,255,255,0.9)] transition"
        >
          Login
        </button>
      </form>
    </div>
  );
}
