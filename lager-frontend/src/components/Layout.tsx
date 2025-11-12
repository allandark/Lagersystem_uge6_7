
import type { ReactNode } from "react";
import Header from "./Header";

interface LayoutProps {
  children: ReactNode;
}

export default function Layout({ children }: LayoutProps) {
  return (
    <div className="dark min-h-screen flex flex-col bg-gray-900 text-gray-100">
      <Header />
      <main className="grow max-w-6xl mx-auto px-4 py-8">
        {children}
      </main>

      
      <footer className="bg-gray-900 text-center py-4 text-gray-400">
        © 2025 Lagersystem. All rights reserved.
      </footer>

    </div>
  );
}

