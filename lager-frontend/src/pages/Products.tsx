import Layout from "../components/Layout";
import type { WarehouseData, InventoryData, ProductData  } from "../types/Types";
import { useState, useEffect } from 'react';


export default function ProductsPage() {

    const [warehouses, setWarehouses] = useState<WarehouseData[]>([]);    
    const [currentInventory, setcurrentInventory] = useState<InventoryData[]>([]);
    const [currentProduct, setcurrentProduct] = useState<ProductData|null>(null);

    

    const API_URL = import.meta.env.VITE_API_URL;

    const getWarehouses = async () =>{
        try{
            const res = await fetch(`${API_URL}/api/warehouse/`)
            const data: WarehouseData[] = await res.json()
            setWarehouses(data)
            console.log("Found warehouses: ", data)
        }
        catch(error){
            console.log("Error fetching warehouses:", error);
        }                    
    }

    // const getWarehouse = async (id: number) =>{
    //     try{
    //         const res = await fetch(`/api/warehouse/${id}`)
    //         const data: WarehouseData = await res.json()
    //         setcurrentWarehouse(data)
    //         console.log("Found warehouses: ", data)
    //     }
    //     catch(error){
    //         console.log("Error fetching warehouses:", error);
    //     }                    
    // }

    const getProduct = async(id: number) =>{
        try{
            const res = await fetch(`/api/product/${id}`)
            const data: WarehouseData = await res.json()
            // setcurrentWarehouse(data)
            console.log("Found warehouses: ", data)
        }
        catch(error){
            console.log("Error fetching warehouses:", error);
        }    
    }

    const getInventory = async (id: number) => {
        try{
            const res = await fetch(`/api/warehouse/${id}/inventory`)
            const data: InventoryData[] = await res.json()
            setcurrentInventory(data)
            console.log("Found warehouses: ", data)
        }
        catch(error){
            console.log("Error fetching warehouses:", error);
        }    
    }


    
    useEffect(() => {
        getWarehouses()
        for(const wh of warehouses ){
            console.log(`Getting inventory from: ${wh.name}`)
            getInventory(wh.id)
            for(const inven of currentInventory){
                // console.log(`Product: ${inven.}`)
            }
        }
    }, []);


    return (
        <Layout>
            <div>

            </div>
        </Layout>
    );
}