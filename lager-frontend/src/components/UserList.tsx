import { useState, useEffect } from 'react';
import { getToken, clearToken } from '../services/authService';
import type { AdminUser } from '../types/Types';
import { useNavigate } from 'react-router-dom';

export default function UserList() {
  const [users, setUsers] = useState<AdminUser[]>([]);
  const API_URL = import.meta.env.VITE_API_URL;
  const [token, setTokenState] = useState<string | null>(getToken());
  const navigate = useNavigate();

  const getUsers = async () => {
    if (!token) {
      console.warn("No token found. Redirecting to login...");
      clearToken();
      setTokenState(null);
      navigate("/admin");
      return;
    }

    try {
      const res = await fetch(`${API_URL}/api/auth/profile/`, {
        method: "GET",
        headers: {
          "Authorization": `Bearer ${token}`,
        },
      });

      if (!res.ok) {
        if (res.status === 401) {
          console.warn("Token expired or invalid. Clearing and redirecting...");
          clearToken();
          setTokenState(null);
          navigate("/admin");
          return;
        }
        throw new Error(`Request failed with status ${res.status}`);
      }

      const data: AdminUser[] = await res.json();
      setUsers(data);
    } catch (error) {
      console.error("User info error:", error);
    }
  };

  useEffect(() => {
    getUsers();
  }, []);

  return (
    <div className="flex justify-center mt-8">
      <div className="bg-gray-900/90 p-6 rounded-3xl shadow-[0_0_30px_rgba(0,255,255,0.5)] w-full max-w-lg text-gray-200">
        <h2 className="text-2xl font-bold text-cyan-400 mb-4 text-center drop-shadow-[0_0_10px_rgba(0,255,255,0.7)]">
          All Users
        </h2>

        {users && users.length > 0 ? (
          <ul className="space-y-3">
            {users.map(user => (
              <li
                key={user.id}
                className="px-4 py-2 rounded-lg bg-gray-800/60 hover:bg-cyan-500/20 transition-colors flex justify-between items-center shadow-[0_0_5px_rgba(0,255,255,0.3)]"
              >
                <span className="font-mono text-cyan-300">[{user.id}]</span>
                <span className="font-semibold">{user.name}</span>
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-center text-gray-400 italic mt-4">No users found.</p>
        )}
      </div>
    </div>
  );
}
