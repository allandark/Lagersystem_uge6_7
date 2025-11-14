import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./index.css"
import Home from "./pages/Home";
import Products from "./pages/Products";
import Invoice from "./pages/Invoice";
import Admin from "./pages/Admin";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/products" element={<Products />} />
        <Route path="/invoice" element={<Invoice />} />
        <Route path="/admin" element={<Admin />} />
      </Routes>
    </BrowserRouter>
  );
}


