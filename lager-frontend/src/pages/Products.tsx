import Layout from "../components/Layout";
import type { WarehouseData, InventoryData, ProductData  } from "../types/Types";
import { useState, useEffect } from 'react';
import "./Products.css"


interface DisplayItem {
  productName: string;
  price: number;
  quantity: number;
  location: string;
}


export default function ProductsPage() {

    const [warehouses, setWarehouses] = useState<WarehouseData[]>([]);    
    const [currentInventory, setcurrentInventory] = useState<InventoryData[]>([]);
    const [currentProduct, setcurrentProduct] = useState<ProductData|null>(null);
    const [displayData, setDisplayData] = useState<DisplayItem[]>([]);

    const productCache: Record<number, ProductData | undefined> = {};

    const API_URL = import.meta.env.VITE_API_URL;

    const getWarehouses = async () =>{
        try{
            const res = await fetch(`${API_URL}/api/warehouse/`)
            const data: WarehouseData[] = await res.json()
            setWarehouses(data)
            // console.log("Found warehouses: ", data)
            return data;
        }
        catch(error){
            console.log("Error fetching warehouses:", error);
            return []
        }                    
    }

    const getProduct = async(id: number) =>{
        try{
            const res = await fetch(`${API_URL}/api/product/id${id}`)
            const data: ProductData = await res.json()
            // setcurrentWarehouse(data)
            // console.log("Found product: ", data)
            return data;
        }
        catch(error){
            console.log("Error fetching product:", error);
        }    
    }

    const getInventory = async (id: number) => {
        try{
            const res = await fetch(`${API_URL}/api/warehouse/${id}/inventory`)
            // console.log(res)
            const data: InventoryData[] = await res.json()
            setcurrentInventory(data)
            // console.log("Found inventory: ", data)
            return data;
        }
        catch(error){
            console.log("Error fetching inventory:", error);
        }    
    }


    
    useEffect(() => {
        const fetchData = async () => {
            const warehouses = await getWarehouses();
            const results: DisplayItem[] = [];
            
            for(const wh of warehouses){
                console.log(`Getting inventory from: ${wh.name}`)
                const currentInventory = await getInventory(wh.id)
                if(currentInventory){
                    for(const invent of currentInventory){
                        
                        if (!productCache[invent.product_id]) {
                            productCache[invent.product_id] = await getProduct(invent.product_id);
                        }

                        const product = productCache[invent.product_id]!
                        if(product){                            
                            results.push({
                                        productName: product.name,
                                        price: product.price,
                                        quantity: invent.quantity,
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
                    <th>Location</th>
                    </tr>
                </thead>
                <tbody>
                    {displayData.map((item, index) => (
                    <tr key={index}>
                        <td>{item.productName}</td>
                        <td>{item.price}</td>
                        <td>{item.quantity}</td>
                        <td>{item.location}</td>
                    </tr>
                    ))}
                </tbody>
                </table>


            </div>

        </Layout>
    );
}