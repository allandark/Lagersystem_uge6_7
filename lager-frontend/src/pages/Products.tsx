import Layout from "../components/Layout";
import type {  InventoryData, ProductData, WarehouseData } from "../types/Types";
import { GetInventory, GetWarehouses, GetProducts } from "../services/apiService";
import { useState, useEffect } from "react";
import ProductForm from "../components/ProductForm";
import InventoryForm from "../components/InventoryForm";
// import type { NumberMap } from "framer-motion";

interface DisplayItem {
  product_id: number;
  warehouse_id: number;
  inventory_id: number;
  product_name: string;
  price: number;
  quantity: number;
  status: string;
  location: string;
}

export default function ProductsPage() {
  const [displayData, setDisplayData] = useState<DisplayItem[]>([]);
  const [showProductForm, setShowProductForm] = useState(false);
  const [showInventoryForm, setShowInventoryForm] = useState(false);
  const [currentProduct, setCurrentProduct] = useState<ProductData | null>(null);
  const [currentWarehouse, setCurrentWarehouse] = useState<WarehouseData | null>(null);
  const [currentInventory, setCurrentInventory] = useState<InventoryData | null>(null);
  const [currentBtnName, setCurrentBtnName] = useState("Submit"); 
//   

  const API_URL = import.meta.env.VITE_API_URL;

  useEffect(() => {
    const fetchData = async () => {
      const warehouses = await GetWarehouses(API_URL);
      const products = await GetProducts(API_URL);
      const results: DisplayItem[] = [];

      for (const wh of warehouses) {
        const currentInventory = await GetInventory(API_URL, wh.id);
        if (currentInventory) {
          for (const inventory of currentInventory) {
            const product = products.find((item) => item.id === inventory.product_id);
            if (product) {
              results.push({
                product_id: product.id,
                warehouse_id: wh.id,
                inventory_id: inventory.id,
                product_name: product.name,
                price: product.price,
                quantity: inventory.quantity,
                status: product.status,
                location: wh.name,
              });
            }
          }
        }
      }
      setDisplayData(results);
    };
    fetchData();
  }, []);


  // Product actions
  const AddProductBtn = () => {
    setCurrentProduct(null);
    setShowProductForm(true);
    setCurrentBtnName("Post");
  };

  const UpdateProductBtn = (row_id: number) => {

    const index = Number(row_id);
    const data = displayData[index];
    if (data) {
      setCurrentProduct({
        id: data.product_id,
        name: data.product_name,
        price: data.price,
        status: data.status,
      } as ProductData);
      setCurrentInventory({
        id: data.inventory_id,
        product_id: data.product_id,
        warehouse_id: data.warehouse_id,
        quantity: data.quantity        
      } as InventoryData);
      setCurrentWarehouse({
        id: data.warehouse_id,
        name: data.location
      } as WarehouseData);
      console.log(`current product: `, currentProduct);
      console.log(`current inventory: `, currentInventory);
      console.log(`current warehouse: `, currentWarehouse);
    //   setShowProductForm(true);
      setShowInventoryForm(true);

      setCurrentBtnName("Put");
    }
  };

  const AddInventoryBtn = () => {
    setShowInventoryForm(true);
    setCurrentBtnName("Post");
  };

  const DeleteProductBtn = (row_id: number) => {
    console.log(`Delete product ${row_id}`);
    setCurrentBtnName("Delete");
  };

  return (
    <Layout>
      <div className="p-6 bg-gray-900 min-h-screen text-cyan-200 space-y-6">
        {/* Header */}
        <div className="flex items-center justify-between mb-6">
          <div>
            <h2 className="text-3xl font-bold tracking-wide drop-shadow-[0_0_8px_rgba(34,211,238,0.7)]">
              🛰️ Inventory Dashboard
            </h2>
            <p className="text-cyan-300 text-sm">Manage your inventory across all warehouses</p>
          </div>
          <div className="flex space-x-3">
            <button
              onClick={AddProductBtn}
              className="px-4 py-2 bg-green-600/90 hover:bg-green-500/90 text-gray-900 font-semibold rounded-lg shadow-[0_0_10px_rgba(0,255,128,0.6)] transition"
            >
              + New Product
            </button>
            <button
              onClick={AddInventoryBtn}
              className="px-4 py-2 bg-blue-600/90 hover:bg-blue-500/90 text-gray-900 font-semibold rounded-lg shadow-[0_0_10px_rgba(0,200,255,0.6)] transition"
            >
              + Add to Warehouse
            </button>
          </div>
        </div>

        {/* Modals */}
        {showProductForm && (
          <div className="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50">
            <div className="bg-gray-800/95 p-6 rounded-2xl shadow-[0_0_20px_rgba(34,211,238,0.4)] w-full max-w-md">
              <ProductForm
                button_name={currentBtnName}
                product={currentProduct}
                onClose={() => {
                    setShowProductForm(false)
                }}
              />
            </div>
          </div>
        )}

        {showInventoryForm && (
          <div className="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50">
            <div className="bg-gray-800/95 p-6 rounded-2xl shadow-[0_0_20px_rgba(0,200,255,0.5)] w-full max-w-lg">
              <InventoryForm 
                button_name={currentBtnName} 
                product={currentProduct}
                warehouse={currentWarehouse}
                inventory={currentInventory}
                onClose={() => {
                setShowInventoryForm(false)
                }} />
            </div>
          </div>
        )}

        {/* Table */}
        <div className="overflow-x-auto rounded-2xl border border-cyan-600/50 shadow-[0_0_20px_rgba(34,211,238,0.3)]">
          <table className="min-w-full text-cyan-200">
            <thead className="bg-gray-800/70 text-cyan-300 uppercase text-sm font-semibold tracking-wide">
              <tr>
                <th className="px-6 py-3 text-left">Product</th>
                <th className="px-6 py-3 text-left">Price</th>
                <th className="px-6 py-3 text-left">Quantity</th>
                <th className="px-6 py-3 text-left">Status</th>
                <th className="px-6 py-3 text-left">Location</th>
                <th className="px-6 py-3 text-center">Actions</th>
              </tr>
            </thead>
            <tbody>
              {displayData.map((item, index) => (
                <tr
                  key={index}
                  className="border-b border-cyan-500/20 hover:bg-gray-700/50 transition-colors"
                >
                  <td className="px-6 py-3 font-medium">{item.product_name}</td>
                  <td className="px-6 py-3">${item.price.toFixed(2)}</td>
                  <td className="px-6 py-3">{item.quantity}</td>
                  <td className="px-6 py-3">
                    <span
                      className={`px-2 py-1 rounded-full text-xs font-semibold ${
                        item.status === "Active"
                          ? "bg-green-700/20 text-green-400"
                          : "bg-red-700/20 text-red-400"
                      }`}
                    >
                      {item.status}
                    </span>
                  </td>
                  <td className="px-6 py-3">{item.location}</td>
                  <td className="px-6 py-3 text-center space-x-2">
                    <button
                      onClick={() => UpdateProductBtn(index)}
                      className="px-2 py-1 bg-blue-500/70 hover:bg-blue-400/70 text-gray-900 rounded-lg shadow-[0_0_6px_rgba(0,200,255,0.5)] transition"
                    >
                      Edit
                    </button>
                    <button
                      onClick={() => DeleteProductBtn(index)}
                      className="px-2 py-1 bg-red-600/70 hover:bg-red-500/70 text-gray-900 rounded-lg shadow-[0_0_6px_rgba(255,50,50,0.5)] transition"
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
              {displayData.length === 0 && (
                <tr>
                  <td colSpan={6} className="text-center py-6 text-cyan-400 italic">
                    No products found.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </Layout>
  );
}
