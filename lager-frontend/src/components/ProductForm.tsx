import { useState, useEffect } from "react";
import type { ProductData } from "../types/Types";
import { Put, Post } from "../services/apiService";
import { getToken } from "../services/authService";

type ProductFormProps = {
  button_name: string;
  product: ProductData | null;
  onClose: () => void;
};

export default function ProductForm({ button_name, product, onClose }: ProductFormProps) {
  const [name, setName] = useState<string>("");
  const [price, setPrice] = useState<number>(0);
  const [status, setStatus] = useState<string>("Active");
  const API_URL = import.meta.env.VITE_API_URL;
  
  useEffect(() => {
    if (product) {
      setName(product.name);
      setPrice(product.price);
      setStatus(product.status);
    }
  }, []);


  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const makeRequest = async () => {
      const token = getToken()
      console.log("post product", product);
  
      if(button_name == "Put"){                              
          let p = {id: 0, name: name,price: price, status: status };
          console.log(p)
          p = await Put(`${API_URL}/api/product`,p.id, p, String(token));
          console.log(p);
        } else if(button_name == "Delete"){
          // let res = await Delete(`${API_URL}/api/product`,product.id, token);
          // console.log(res)
        } else if(button_name == "Post"){                    
          let p = {id: 0, name: name,price: price, status: status };
          console.log(p);
          p = await Post(`${API_URL}/api/product`, p, String(token));
          console.log(p);
        }
      
    }
    
    makeRequest();
    
    onClose();
  };

  return (
    <div className="bg-gray-900/95 p-6 rounded-2xl shadow-[0_0_20px_rgba(34,211,238,0.5)] w-full">
      <h3 className="text-2xl font-bold text-cyan-300 mb-4 drop-shadow-[0_0_6px_rgba(34,211,238,0.7)]">
        {button_name}
      </h3>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="flex flex-col">
          <label className="text-cyan-200 mb-1">Product Name</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="bg-gray-800/70 border border-cyan-500/50 rounded-lg px-3 py-2 text-cyan-200 placeholder-cyan-400 focus:outline-none focus:ring-2 focus:ring-cyan-400 transition"
            placeholder="Enter product name"
          />
        </div>

        <div className="flex flex-col">
          <label className="text-cyan-200 mb-1">Price</label>
          <input
            type="number"
            step="0.01"
            value={price}
            onChange={(e) => setPrice(isNaN(e.target.valueAsNumber) ? 0 : e.target.valueAsNumber)}
            className="bg-gray-800/70 border border-cyan-500/50 rounded-lg px-3 py-2 text-cyan-200 placeholder-cyan-400 focus:outline-none focus:ring-2 focus:ring-cyan-400 transition"
            placeholder="0.00"
          />
        </div>

        <div className="flex flex-col">
          <label className="text-cyan-200 mb-1">Status</label>
          <select
            value={status}
            onChange={(e) => {
              setStatus(e.target.value)
            }}
              
            className="bg-gray-800/70 border border-cyan-500/50 rounded-lg px-3 py-2 text-cyan-200 focus:outline-none focus:ring-2 focus:ring-cyan-400 transition"
          >
            <option value="Active">Active</option>
            <option value="Inactive">Inactive</option>
          </select>
        </div>

        <div className="flex justify-end space-x-2">
          <button
            type="button"
            onClick={onClose}
            className="px-4 py-2 bg-gray-700/70 text-cyan-200 rounded-lg hover:bg-gray-600/70 transition"
          >
            Cancel
          </button>
          <button
            type="submit"
            className="px-4 py-2 bg-cyan-500/70 text-gray-900 font-semibold rounded-lg shadow-[0_0_6px_rgba(34,211,238,0.5)] hover:bg-cyan-400/70 transition"
          >
            {button_name}
          </button>
        </div>
      </form>
    </div>
  );
}
