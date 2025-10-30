import Layout from "../components/Layout";
import type { WarehouseData } from "../types/Types";
import { useState, useEffect } from 'react';


export default function ProductsPage() {

    const [warehouses, setWarehouses] = useState<WarehouseData[]>([]);
    const [wh, setWh] = useState<WarehouseData|null>(null);
    const [wh_id, setWhId] = useState(1);

    const getWarehouses = async () =>{
        try{
            const res = await fetch("http://localhost:5000/api/warehouse/")
            const data: WarehouseData[] = await res.json()
            setWarehouses(data)
            console.log("Found warehouses: ", data)
        }
        catch(error){
            console.log("Error fetching warehouses:", error);
        }                    
    }

        const getWarehouse = async (id: number) =>{
        try{
            const res = await fetch(`http://localhost:5000/api/warehouse/${id}`)
            const data: WarehouseData = await res.json()
            setWh(data)
            console.log("Found warehouses: ", data)
        }
        catch(error){
            console.log("Error fetching warehouses:", error);
        }                    
    }


    
    useEffect(() => {
    getWarehouses();
    // getWarehouse(wh_id);
    }, []);


    return (
        <Layout>
            <h2>Products</h2>
            <button onClick={() =>{
                var value: number = wh_id + 1;
                if(value > 3){
                    value = 1;
                }
                setWhId(value);
                getWarehouse(value);
            }}>{wh_id}</button>
            
            {wh && (
            <div>
                [{wh.id}]: {wh.name}
            </div>
            )}

            <h3>Warehouses</h3>
            <ul>
                {warehouses.map(warehouse => (
                <li key={warehouse.id}>[{warehouse.id}]: {warehouse.name}</li>
                ))}
            </ul>

        </Layout>
    );
}