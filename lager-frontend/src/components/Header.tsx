interface HeaderProps {
  className?: string; // optional
}


export default function Header({className}: HeaderProps) {
  const version = import.meta.env.VITE_VERSION;
  return (
    <header className={className ?? "layout-header"}>
      <h1>Lagersystem</h1><br/>
      <small style={{ color: '#666' }}>Version: {version}</small>
      <nav>
        <a href="/">Home</a>
        <a href="/products">Products</a>
        <a href="/customer">Customer</a>
        <a href="/admin">Admin</a>
      </nav>
    </header>
  );
}