import type { WarehouseData, InventoryData, ProductData, InvoiceData, CustomerData  } from "../types/Types";

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


export const Post = async (url:string, body: Object, token: string) =>{
    try {
        
        const res = await fetch(`${url}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
            },
            credentials: 'include',
            body: JSON.stringify(body),
        });
        console.log(`Res: ${res}`)    
        const data: any = await res.json();                     
        return data;
        
    } catch (error) {
        console.error("Login error:", error); 
        return null;
    }
};


export const Put = async (url:string, id: number, body: Object, token: string) =>{
    try {

        console.log(body)
        
        const res = await fetch(`${url}/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
            },
            credentials: 'include',
            body: JSON.stringify(body),
        });
        console.log(`Res: `, res)    
        
        const data: any = await res.json();                     
        return data;
        
    } catch (error) {
        console.error("Put error:", error); 
        return null;
    }
};

export const Delete = async (url:string, id: number, token: string) =>{
    try {
        
        const res = await fetch(`${url}/${id}`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
            },
            credentials: 'include',
        });
        console.log(`Res: ${res}`)    
        const data: any = await res.json();                     
        return data;
        
    } catch (error) {
        console.error("Login error:", error); 
        return null;
    }
};


export const GetWarehouses = async (url:string) =>{
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

// export const AddProduct = async (
//     url:string, name: string, price: number, status: string) =>  {
//     return null;
// }

// export const UpdateProduct = async (
//     url:string, id: number, name: string, price: number, status: string) =>  {
//     return null;
// }

export const GetInvoices = async (url: string) => {
    try{
        const res = await fetch(`${url}/api/orders`)
        const data = await res.json()    
        let invoices: Array<InvoiceData> =  [] 
        for(let i = 0; i < data.length; i++) {            
            const  invoice :InvoiceData = {} as InvoiceData
            invoice.id = data[i]["orderID"]
            invoice.product_id = data[i]["produktID"]
            invoice.invoice_number = data[i]["invoicenummer"]
            invoice.customer_id = data[i]["customerID"]
            invoice.status = data[i]["status"]
            invoice.quantity = data[i]["mængde"]
            invoice.warehouse_id = data[i]["lagerID"]
            invoices.push(invoice)
   
        }                  
        return Array.isArray(invoices) ? invoices : [];
    }
    catch(error){
        console.log("Error fetching invoices:", error);
        return [];
    }    
}


export const GetCustomers = async (url: string) => {
    try{
        const res = await fetch(`${url}/api/customer`)
        const data: CustomerData[] = await res.json()    
        // console.log(data)
        return Array.isArray(data) ? data : [];
    }
    catch(error){
        console.log("Error fetching customers:", error);
        return [];
    }    
}