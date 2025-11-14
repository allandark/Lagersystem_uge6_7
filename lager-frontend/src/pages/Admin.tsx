import Layout from "../components/Layout";
import LoginForm from "../components/LoginForm";
import RegisterForm from "../components/Register";
import UserInfo from "../components/UserInfo";
import UserList from "../components/UserList";
import { setToken, getToken } from '../services/authService';
import { useState, useEffect } from 'react';

export default function AdminPage() {
  const [tokenState, setTokenState] = useState<string | null>(null);

  useEffect(() => {
    setTokenState(getToken());
  }, []);

  return (
    <Layout>
      <div className="flex min-h-[80vh] items-center justify-center">
        {tokenState ? (
          <div className="space-y-6 text-cyan-200">
            <UserInfo />
            <RegisterForm />
            <UserList />
         
          </div>
        ) : (
          <LoginForm
            onLoginSuccess={(token) => {
              setToken(token);
              setTokenState(token);
            }}
          />
        )}
      </div>
    </Layout>
  );
}
