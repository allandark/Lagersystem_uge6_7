// interface HeaderProps {
//   className?: string; // optional
// }

export default function Header() {
  const version = import.meta.env.VITE_VERSION;
  return (
    <header className="relative bg-linear-to-r from-gray-900 via-gray-800 to-gray-900 p-6">
      <div className="max-w-6xl mx-auto px-4 flex justify-between items-center">
      {/* Logo */}
      <div className="inline-block relative overflow-visible">
        <h1 className="text-5xl font-bold text-transparent bg-clip-text
                 bg-linear-to-r from-blue-400 via-purple-400 to-pink-400
                 bg-size-[200%_200%] animate-gradient-colors text-glow
                 leading-[1.3] pb-2"
                    >
          Lagersystem
        </h1>

        <small className="block text-gray-400 tracking-wide 
                        hover:text-blue-300 hover:drop-shadow-[0_0_5px_rgba(59,130,246,0.6)]
                        transition duration-300 mt-1">
          Version: {version}
        </small>
      </div>

      {/* Navigation */}
      <nav className="flex gap-6 justify-center mt-6">
        <a
            href="/"
            className="
              relative
              text-white
              transition-all
              duration-300
              hover:text-blue-400
              hover:drop-shadow-[0_0_15px_rgba(59,130,246,0.9)]
              before:absolute
              before:inset-0
              before:rounded
              before:bg-blue-400
              before:opacity-30
              before:blur-xl
              before:scale-110
              before:transition-all
              before:duration-300
              hover:before:opacity-50
              hover:before:scale-125
              before:pointer-events-none
            "
          >
            Home
          </a>
          <a
            href="/products"
            className="
              relative
              text-white
              transition-all
              duration-300
              hover:text-blue-400
              hover:drop-shadow-[0_0_15px_rgba(59,130,246,0.9)]
              before:absolute
              before:inset-0
              before:rounded
              before:bg-blue-400
              before:opacity-30
              before:blur-xl
              before:scale-110
              before:transition-all
              before:duration-300
              hover:before:opacity-50
              hover:before:scale-125
              before:pointer-events-none
            "
          >
            Products
          </a>
          <a
            href="/customer"
            className="
              relative
              text-white
              transition-all
              duration-300
              hover:text-blue-400
              hover:drop-shadow-[0_0_15px_rgba(59,130,246,0.9)]
              before:absolute
              before:inset-0
              before:rounded
              before:bg-blue-400
              before:opacity-30
              before:blur-xl
              before:scale-110
              before:transition-all
              before:duration-300
              hover:before:opacity-50
              hover:before:scale-125
              before:pointer-events-none
            "
          >
            Customer
          </a>
          <a
            href="/admin"
            className="
              relative
              text-white
              transition-all
              duration-300
              hover:text-blue-400
              hover:drop-shadow-[0_0_15px_rgba(59,130,246,0.9)]
              before:absolute
              before:inset-0
              before:rounded
              before:bg-blue-400
              before:opacity-30
              before:blur-xl
              before:scale-110
              before:transition-all
              before:duration-300
              hover:before:opacity-50
              hover:before:scale-125
              before:pointer-events-none
            "
          >
            Admin
          </a>

     
        
      </nav>
      </div>

      
    </header>
  );
}