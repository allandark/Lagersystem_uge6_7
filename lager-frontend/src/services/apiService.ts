import type { WarehouseData, InventoryData, ProductData  } from "../types/Types";

export const AuthLogin = async (url:string, name: string, password: string) =>  {
    try {
        console.log("Logging in")
        const loginModel = {
            "username": name,
            "password": password
        }        
        const res = await fetch(`${url}/api/auth/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        credentials: 'include',
        body: JSON.stringify(loginModel),
        });
        console.log(`Res: ${res}`)
    
        const data: any = await res.json();                     
        return data["access_token"];
        
    } catch (error) {
        console.error("Login error:", error); 
        return null;
    }
};



export const GetWarehouses = async (url:string,) =>{
    try{
        const res = await fetch(`${url}/api/warehouse/`)
        const data: WarehouseData[] = await res.json()                        
        return Array.isArray(data) ? data : [];
    }
    catch(error){
        console.log("Error fetching warehouses:", error);
        return [];
    }                    
}


export const GetProduct = async(url: string, id: number) =>{
    try{
        const res = await fetch(`${url}/api/product/id${id}`)
        const data: ProductData = await res.json()
        return data;
    }
    catch(error){
        console.log("Error fetching product:", error);
        return null;
    }    
}


export const GetProducts = async(url: string) =>{
    try{
        const res = await fetch(`${url}/api/product/`)            
        const data: ProductData[] = await res.json()
        return Array.isArray(data) ? data : [];
    }
    catch(error){
        console.log("Error fetching product:", error);
        return [];
    }    
}

export const GetInventory = async (url: string, id: number) => {
    try{
        const res = await fetch(`${url}/api/warehouse/${id}/inventory`)
        const data: InventoryData[] = await res.json()                        
        return Array.isArray(data) ? data : [];
    }
    catch(error){
        console.log("Error fetching inventory:", error);
        return [];
    }    
}

export const AddProduct = async (
    url:string, name: string, price: number, status: string) =>  {
    return null;
}

export const UpdateProduct = async (
    url:string, id: number, name: string, price: number, status: string) =>  {
    return null;
}