import { useState } from 'react';
import type { ProductData  } from "../types/Types";


type ProductFormProps = {
  button_name: string;
  product: ProductData | null;
  onClose: () => void;
};


export default function ProductForm({ button_name, product, onClose }: ProductFormProps) {
    const [name, setName] = useState<string>("");
    const [price, setPrice] = useState<number>(0);
    const [status, setStatus] = useState<string>("");
    const API_URL = import.meta.env.VITE_API_URL;

    if(product != null){
            setName(product.name);
            setPrice(product.price);
            setStatus(product.status); 
        }
    
    // useEffect(() => {
        
    //   }, []);

      async function submitProduct(){
       
        onClose();
      }

  
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    submitProduct();
  };

 
  return (
      <div>
        <form onSubmit={handleSubmit}>
            {/* {product ? (
            <div>
                ID: {product.id}
            </div>
            ):<div/>} */}
            <div></div>
            <label>Product Name:
            <input
                name="name"
                autoComplete="off"
                placeholder="product name"
                type="text"
                value={name}
                onChange={e => setName(e.target.value)}
            />
            <br />
            </label>
            <label>Price:
                <input
                    name="price"
                    step="0.01"
                    autoComplete="off"
                    placeholder="product price"
                    type="number"
                    value={price}
                    onChange={e => {
                        const value: number = isNaN(e.target.valueAsNumber)  ? 0 : e.target.valueAsNumber;
                        setPrice(value);
                    }}
                />
            </label>
            <label>Status:
                <input
                    name="status"
                    autoComplete="off"
                    placeholder="product status"
                    type="text"
                    value={status}
                    onChange={e => setStatus(e.target.value)}
                />
            </label>
            <button
            type="submit"
            >{button_name}</button>
        
        </form>
      </div>
    )}
