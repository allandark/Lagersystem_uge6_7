import { useState, useEffect } from "react";
import type { WarehouseData, ProductData, InventoryData } from "../types/Types";
import { GetInventory, GetProducts, GetWarehouses, Put, Post } from "../services/apiService";
import { getToken } from "../services/authService";

type InventoryFormProps = {
  button_name: string;
  product: ProductData | null;
  warehouse: WarehouseData | null;
  inventory: InventoryData | null;
  onClose: () => void;
};

export default function InventoryForm({ button_name,product,warehouse, inventory, onClose }: InventoryFormProps) {
  const [products, setProducts] = useState<ProductData[]>([]);
  const [warehouses, setWarehouses] = useState<WarehouseData[]>([]);
  // const [ setInventories] = useState<InventoryData[][]>([]); //inventories
  const [selectedProduct, setSelectedProduct] = useState<number | "">("");
  const [selectedWarehouse, setSelectedWarehouse] = useState<number | "">("");
  const [selectedInventory, setSelectedInventory] = useState<number | "">("");
  const [quantity, setQuantity] = useState<number>(0);

  const API_URL = import.meta.env.VITE_API_URL;



  useEffect(() => {
    const fetchData = async () => {
      const productsData = await GetProducts(API_URL);
      const warehousesData = await GetWarehouses(API_URL);      
      const inventorysData = []
      for (const wh of warehousesData) {
        const inv = await GetInventory(API_URL, wh.id);  
        inventorysData.push(inv);
      }
      
      setProducts(productsData);
      setWarehouses(warehousesData);
      // setInventories(inventorysData);

      if(product){        
        setSelectedProduct(product.id);        
      }
      if(warehouse){
        setSelectedWarehouse(warehouse.id);
      }
      if(inventory){
        setSelectedInventory(inventory.id);
        setQuantity(inventory.quantity);
      }

      console.log(`product: ${product?.id}, warehouse: ${warehouse?.id}, inventory: ${inventory?.id}`)
    };
    fetchData();
  }, []);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log({ selectedProduct, selectedWarehouse, quantity });
    const makeRequest = async () => {
      const token = getToken()
    

      if(button_name === "Put"){        
        let inv = {    
          id: Number(selectedInventory),
          product_id: Number(selectedProduct),
          warehouse_id: Number(selectedWarehouse),
          quantity: quantity
        };

        console.log("Requesting: ", inv)
        inv.product_id = Number(selectedProduct);
        inv.warehouse_id = Number(selectedWarehouse);
        inv.quantity = Number(quantity)
        inv = await Put(`${API_URL}/api/warehouse/${Number(selectedWarehouse)}/inventory`,inv.id, inv , String(token));
        console.log(inv);
        
      
      } else if(button_name == "Post"){
        let inv = {              
          product_id: Number(selectedProduct),
          warehouse_id: Number(selectedWarehouse),
          quantity: quantity
        };
                                  
          inv = await Post(`${API_URL}/api/warehouse/${Number(selectedWarehouse)}/inventory`, inv, String(token) );
          console.log(inv);
        }        
    }
    makeRequest();
    onClose();
  };

  return (
    <div className="bg-gray-900/95 p-6 rounded-2xl shadow-[0_0_20px_rgba(0,200,255,0.5)] w-full">
      <h3 className="text-2xl font-bold text-cyan-300 mb-4 drop-shadow-[0_0_6px_rgba(0,200,255,0.7)]">
        Add Inventory
      </h3>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="flex flex-col">
          <label className="text-cyan-200 mb-1">Product</label>
          <select
            value={selectedProduct || ''}
            onChange={(e) => setSelectedProduct(Number(e.target.value))}
            className="bg-gray-800/70 border border-cyan-500/50 rounded-lg px-3 py-2 text-cyan-200 focus:outline-none focus:ring-2 focus:ring-cyan-400 transition"
          >  
          {selectedProduct === "" && (
            <option value="">Select a product</option>
          )}    
            {products.map((p) => (
              
              <option  key={p.id} value={p.id}>
                {p.name}
              </option>
            ))}
          </select>
        </div>

        <div className="flex flex-col">
          <label className="text-cyan-200 mb-1">Warehouse</label>
          <select
            value={selectedWarehouse}
            onChange={(e) => setSelectedWarehouse(Number(e.target.value))}
            className="bg-gray-800/70 border border-cyan-500/50 rounded-lg px-3 py-2 text-cyan-200 focus:outline-none focus:ring-2 focus:ring-cyan-400 transition"
          >
            <option value="">Select a warehouse</option>
            {warehouses.map((w) => (
              <option key={w.id} value={w.id}>
                {w.name}
              </option>
            ))}
          </select>
        </div>

        <div className="flex flex-col">
          <label className="text-cyan-200 mb-1">Quantity</label>
          <input
            type="number"
            value={quantity}
            onChange={(e) => setQuantity(Number(e.target.value))}
            className="bg-gray-800/70 border border-cyan-500/50 rounded-lg px-3 py-2 text-cyan-200 placeholder-cyan-400 focus:outline-none focus:ring-2 focus:ring-cyan-400 transition"
            placeholder="0"
          />
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
            className="px-4 py-2 bg-cyan-500/70 text-gray-900 font-semibold rounded-lg shadow-[0_0_6px_rgba(0,200,255,0.5)] hover:bg-cyan-400/70 transition"
          >
            {button_name}
          </button>
        </div>
      </form>
    </div>
  );
}
