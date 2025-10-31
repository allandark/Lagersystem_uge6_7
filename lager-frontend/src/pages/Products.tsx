import Layout from "../components/Layout";
import type { WarehouseData, InventoryData, ProductData  } from "../types/Types";
import { useState, useEffect } from 'react';
import "./Products.css"


interface DisplayItem {
  productName: string;
  price: number;
  quantity: number;
  status: string;
  location: string;
}


export default function ProductsPage() {

    const [displayData, setDisplayData] = useState<DisplayItem[]>([]);    

    const API_URL = import.meta.env.VITE_API_URL;

    const getWarehouses = async () =>{
        try{
            const res = await fetch(`${API_URL}/api/warehouse/`)
            const data: WarehouseData[] = await res.json()                        
            return Array.isArray(data) ? data : [];
        }
        catch(error){
            console.log("Error fetching warehouses:", error);
            return [];
        }                    
    }

    // const getProduct = async(id: number) =>{
    //     try{
    //         const res = await fetch(`${API_URL}/api/product/id${id}`)
    //         const data: ProductData = await res.json()
    //         return data;
    //     }
    //     catch(error){
    //         console.log("Error fetching product:", error);
    //     }    
    // }

    const getProducts = async() =>{
        try{
            const res = await fetch(`${API_URL}/api/product/`)
            const data: ProductData[] = await res.json()
            return Array.isArray(data) ? data : [];
        }
        catch(error){
            console.log("Error fetching product:", error);
            return [];
        }    
    }

    const getInventory = async (id: number) => {
        try{
            const res = await fetch(`${API_URL}/api/warehouse/${id}/inventory`)
            const data: InventoryData[] = await res.json()                        
            return Array.isArray(data) ? data : [];
        }
        catch(error){
            console.log("Error fetching inventory:", error);
            return [];
        }    
    }


    
    useEffect(() => {
        const fetchData = async () => {
            const warehouses = await getWarehouses();
            const results: DisplayItem[] = [];
            const products: ProductData[] = await getProducts();
            for(const wh of warehouses){
                console.log(`Getting inventory from: ${wh.name}`)
                const currentInventory = await getInventory(wh.id)
                if(currentInventory){
                    for(const inventory of currentInventory){
                        
                        const product = products.find(item => item.id === inventory.product_id);
                        if(product){
                            results.push({
                                        productName: product.name,
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


    return (
        <Layout>

            <div>
                <h2>Inventory Overview</h2>


                <table className="table">
                <thead>
                    <tr>
                    <th>Product</th>
                    <th>Price</th>
                    <th>Quantity</th>
                    <th>Status</th>
                    <th>Location</th>
                    </tr>
                </thead>
                <tbody>
                    {displayData.map((item, index) => (
                    <tr key={index}>
                        <td>{item.productName}</td>
                        <td>{item.price}</td>
                        <td>{item.quantity}</td>
                        <td>{item.status}</td>
                        <td>{item.location}</td>
                    </tr>
                    ))}
                </tbody>
                </table>


            </div>

        </Layout>
    );
}