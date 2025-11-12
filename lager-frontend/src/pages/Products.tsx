import Layout from "../components/Layout";
import type { WarehouseData, InventoryData, ProductData  } from "../types/Types";
import { GetInventory, GetWarehouses, GetProducts } from "../services/apiService";

import { useState, useEffect } from 'react';
import ProductForm from "../components/ProductForm";


interface DisplayItem {
  id: number;
  productName: string;
  price: number;
  quantity: number;
  status: string;
  location: string;
}


export default function ProductsPage() {

    const [displayData, setDisplayData] = useState<DisplayItem[]>([]);    
    const [productForm, setProductForm] = useState<Boolean>(false);

    const API_URL = import.meta.env.VITE_API_URL;

    var products: ProductData[];
    var currentProduct: ProductData|null = null;
    var currentBtnName: string = "Submit";


    const AddProductBtn = (e: React.FormEvent) => {
            
        console.log(`Add product`);
        setProductForm(true);
        currentBtnName = "Add Product";
        currentProduct = null;
    };

    const UpdateProductBtn = (e: React.FormEvent, id: number) => {
        console.log(`Update product ${id}`);  
        setProductForm(true);
        const res : ProductData | undefined = products.find((e) => e.id == id);
        if(res != undefined){
            currentProduct = res;
        }else{
            console.error(`Cannot find product with ${id}`);
        }
        
    };

    const DeleteProductBtn = (e: React.FormEvent, id: number) => {
            
        
        console.log(`Delete product ${id}`);
    };



    useEffect(() => {
        const fetchData = async () => {
            const warehouses = await GetWarehouses(API_URL);
            const results: DisplayItem[] = [];
            products = await GetProducts(API_URL);
            for(const wh of warehouses){
                console.log(`Getting inventory from: ${wh.name}`)
                const currentInventory = await GetInventory(API_URL, wh.id)
                if(currentInventory){
                    for(const inventory of currentInventory){
                        const product = products.find(item => item.id === inventory.product_id);
                        if(product){
                            results.push({
                                id: product.id,
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
                {productForm ? (
                <div>
                    <ProductForm 
                        button_name={currentBtnName}
                        product={currentProduct}
                        onClose={() => setProductForm(false)}
                    />

                </div>
                ) : (
                    <button
                    onClick={e => AddProductBtn(e)}
                    >Add Product</button>
                )}

                <hr></hr>
                {/* <input>Filter</input> */}
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
                        <td>
                            <button
                            key={item.id} 
                            onClick={e => UpdateProductBtn(e, item.id)}
                            >Update</button>
                            <button
                            key={index}
                            onClick={e => DeleteProductBtn(e, item.id)}
                            >Delete</button>
                        </td>
                    </tr>
                    ))}
                </tbody>
                </table>
            </div>

        </Layout>
    );
}