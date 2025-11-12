import Layout from "../components/Layout";
import type { WarehouseData, InventoryData, CustomerData  } from "../types/Types";
import { useState, useEffect } from 'react';
import "./Customer.css"

interface DisplayItem {
    id: number,
    name: string,
    email: string,
}

export default function CustomerPage() {

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

    const getCustomers = async() =>{
        console.log("Hello!");
        try{
            const res = await fetch(`${API_URL}/api/customer/`)
            const data: CustomerData[] = await res.json()
            return Array.isArray(data) ? data : [];
        }
        catch(error){
            console.log("Error fetching customers:", error);
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
        async function sleep(ms: number): Promise<void> {
            return new Promise((resolve) => setTimeout(resolve, ms));
        }
        const fetchData = async () => {
            console.log("Get customers");
            const warehouses = await getWarehouses();
            await sleep(2000);
            const results: DisplayItem[] = [];
            const customers: CustomerData[] = await getCustomers();
            await sleep(2000);
            for(const wh of warehouses){
                console.log(`Getting inventory from: ${wh.name}`)
                const currentInventory = await getInventory(wh.id)
                await sleep(2000);
                if(currentInventory){
                    for(const inventory of currentInventory){

                        const customer = customers.find(item => item.id === inventory.product_id);
                        if(customer){
                            results.push({
                                id: customer.id,
                                name: customer.name,
                                email: customer.email,
                            });
                        }

                    }
                }
            }
            setDisplayData(results);
        };
        fetchData();
    },[]);


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
                            <td>{item.id}</td>
                            <td>{item.name}</td>
                            <td>{item.email}</td>
                        </tr>
                    ))}
                    </tbody>
                </table>


            </div>

        </Layout>
    );
}