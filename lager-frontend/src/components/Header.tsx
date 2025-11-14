import { useState, useEffect } from "react";
import { getToken } from "../services/authService"; //clearToken
import { useNavigate } from "react-router-dom";

export default function Navbar() {
  const [userName, setUserName] = useState<string | null>(null);
  const API_URL = import.meta.env.VITE_API_URL;
  const token = getToken();
  const navigate = useNavigate();

  const holoLinkClass = `
    relative
    px-4 py-2
    text-white
    font-semibold
    rounded-lg
    transition-all
    duration-300
    hover:text-cyan-400
    hover:drop-shadow-[0_0_15px_rgba(0,255,255,0.9)]
    before:absolute
    before:inset-0
    before:rounded
    before:bg-cyan-400
    before:opacity-20
    before:blur-xl
    before:scale-110
    before:transition-all
    before:duration-300
    hover:before:opacity-50
    hover:before:scale-125
    before:pointer-events-none
  `;

  useEffect(() => {
    if (!token) return;

    const fetchUser = async () => {
      try {
        const res = await fetch(`${API_URL}/api/auth/profile/me`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        if (res.ok) {
          const data = await res.json();
          setUserName(data.name);
        }
      } catch (err) {
        console.error(err);
      }
    };
    fetchUser();
  }, [token]);

  return (
    <nav className="flex gap-6 justify-center mt-6">
      <a href="/" className={holoLinkClass}>
        Home
      </a>
      <a href="/products" className={holoLinkClass}>
        Products
      </a>
      <a href="/invoice" className={holoLinkClass}>
        Invoices
      </a>

      {userName ? (
        <button
          onClick={() => {
            // clearToken();
            navigate("/admin");
          }}
          className={holoLinkClass}
        >
          {userName}
        </button>
      ) : (
        <a href="/admin" className={holoLinkClass}>
          Login
        </a>
      )}
    </nav>
  );
}
