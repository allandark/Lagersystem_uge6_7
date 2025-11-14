import { useState, useEffect } from 'react';
import { getToken, clearToken } from '../services/authService';
import type { AdminUser } from '../types/Types';
import { useNavigate } from 'react-router-dom';

export default function UserInfo() {
  const [user, setUser] = useState<AdminUser | null>(null);
  const API_URL = import.meta.env.VITE_API_URL;
  const token = getToken();
  const navigate = useNavigate();

  const getUser = async () => {
    if (!token) {
      console.warn("No token found. Redirecting to login...");
      clearToken();
      navigate("/admin");
      return;
    }

    try {
      const res = await fetch(`${API_URL}/api/auth/profile/me`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
      });

      if (!res.ok) {
        if (res.status === 401) {
          console.warn("Token expired or invalid. Clearing and redirecting...");
          clearToken();
          navigate("/admin");
        }
        throw new Error(`Request failed with status ${res.status}`);
      }

      const data: AdminUser = await res.json();
      setUser(data);
    } catch (error) {
      console.error("User info error:", error);
    }
  };

  useEffect(() => {
    getUser();
  }, []);

  return (
    <div className="flex justify-center mt-10">
      <div className="bg-gray-900/90 p-6 rounded-3xl shadow-[0_0_30px_rgba(0,255,255,0.5)] w-full max-w-md text-gray-200">
        <h2 className="text-2xl font-bold text-cyan-400 mb-4 text-center drop-shadow-[0_0_10px_rgba(0,255,255,0.7)]">
          Admin Info
        </h2>

        <div className="space-y-3">
          <div>
            <span className="font-semibold text-cyan-300">ID:</span> <span>{user?.id ?? "-"}</span>
          </div>
          <div>
            <span className="font-semibold text-cyan-300">Name:</span> <span>{user?.name ?? "-"}</span>
          </div>
        </div>

        <button
          onClick={() => {
            clearToken();
            window.location.href = "/admin";
          }}
          className="mt-6 w-full bg-cyan-500/70 text-gray-900 font-bold py-2 rounded-xl shadow-[0_0_15px_rgba(0,255,255,0.7)] hover:bg-cyan-400/70 hover:shadow-[0_0_20px_rgba(0,255,255,0.9)] transition"
        >
          Logout
        </button>
      </div>
    </div>
  );
}
