import { useState, useEffect } from "react";
import Layout from "../components/Layout";
import type { InvoiceData, ProductData, WarehouseData, CustomerData } from "../types/Types";
import { GetInvoices, GetProducts, GetWarehouses, GetCustomers } from "../services/apiService";

interface DisplayInvoice {
  id: number;
  invoiceNumber: number;
  productName: string;
  customerName: string;
  warehouseName: string;
  quantity: number;
  status: string;
}

export default function InvoicesPage() {
  const [invoices, setInvoices] = useState<DisplayInvoice[]>([]);
  const [showInvoiceForm, setShowInvoiceForm] = useState(false);
  const [currentInvoice, setCurrentInvoice] = useState<InvoiceData | null>(null);
  const [formBtnName, setFormBtnName] = useState("Submit");
  const [products, setProducts] = useState<ProductData[]>([]);
  const [warehouses, setWarehouses] = useState<WarehouseData[]>([]);
  const [customers, setCustomers] = useState<CustomerData[]>([]);

  const API_URL = import.meta.env.VITE_API_URL;

  useEffect(() => {
    const fetchData = async () => {
      const [prodData, whData, custData, invoiceData] = await Promise.all([
        GetProducts(API_URL),
        GetWarehouses(API_URL),
        GetCustomers(API_URL),
        GetInvoices(API_URL),
      ]);


      setProducts(prodData);
      setWarehouses(whData);
      setCustomers(custData);

      const displayData: DisplayInvoice[] = invoiceData.map((inv: InvoiceData) => {
        const product = prodData.find((p) => p.id === inv.product_id);
        const warehouse = whData.find((w) => w.id === inv.warehouse_id);
        const customer = custData.find((c) => c.id === inv.customer_id);


        return {
          id: inv.id,
          invoiceNumber: inv.invoice_number,
          productName: product?.name || "Unknown",
          warehouseName: warehouse?.name || "Unknown",
          customerName: customer?.name || "Unknown",
          quantity: inv.quantity,
          status: inv.status,
        };
      });

      setInvoices(displayData);
      console.log(`Disp data: ${displayData}`)
    };
    fetchData();
  }, []);

  const AddInvoiceBtn = () => {
    setCurrentInvoice(null);
    setFormBtnName("Create Invoice");
    setShowInvoiceForm(true);
  };

  const EditInvoiceBtn = (id: number) => {
    const inv = invoices.find((i) => i.id === id);
    if (inv) {
      setCurrentInvoice({
        id: inv.id,
        invoice_number: inv.invoiceNumber,
        product_id: products.find((p) => p.name === inv.productName)?.id || 0,
        warehouse_id: warehouses.find((w) => w.name === inv.warehouseName)?.id || 0,
        customer_id: customers.find((c) => c.name === inv.customerName)?.id || 0,
        quantity: inv.quantity,
        status: inv.status,
      });
      setFormBtnName("Update Invoice");
      setShowInvoiceForm(true);
    }
  };

  const DeleteInvoiceBtn = (id: number) => {
    console.log("Delete invoice", id);
  };

  return (
    <Layout>
      <div className="p-6">
        {/* Header */}
        <div className="flex items-center justify-between mb-6">
          <div>
            <h2 className="text-2xl font-bold text-cyan-300 drop-shadow-[0_0_6px_rgba(34,211,238,0.7)]">
              📄 Invoices Dashboard
            </h2>
            <p className="text-gray-400 text-sm">Manage all invoices</p>
          </div>
          <button
            onClick={AddInvoiceBtn}
            className="bg-cyan-500/70 text-gray-900 px-4 py-2 rounded-lg shadow-[0_0_6px_rgba(34,211,238,0.5)] hover:bg-cyan-400/70 transition"
          >
            + New Invoice
          </button>
        </div>

        {/* Invoice Form Modal */}
        {showInvoiceForm && (
          <div className="fixed inset-0 bg-black bg-opacity-30 flex items-center justify-center z-50">
            <div className="bg-gray-900/95 p-6 rounded-2xl shadow-[0_0_20px_rgba(0,200,255,0.5)] w-full max-w-md">
              <InvoiceForm
                invoice={currentInvoice}
                button_name={formBtnName}
                products={products}
                warehouses={warehouses}
                customers={customers}
                onClose={() => setShowInvoiceForm(false)}
              />
            </div>
          </div>
        )}

        {/* Table */}
        <div className="bg-gray-900/70 rounded-xl shadow-[0_0_20px_rgba(0,200,255,0.3)] overflow-hidden">
          <table className="min-w-full text-cyan-200">
            <thead className="bg-gray-800/70 uppercase text-sm font-semibold">
              <tr>
                <th className="px-6 py-3 text-left">Invoice #</th>
                <th className="px-6 py-3 text-left">Product</th>
                <th className="px-6 py-3 text-left">Customer</th>
                <th className="px-6 py-3 text-left">Warehouse</th>
                <th className="px-6 py-3 text-left">Quantity</th>
                <th className="px-6 py-3 text-left">Status</th>
                <th className="px-6 py-3 text-center">Actions</th>
              </tr>
            </thead>
            <tbody>
              {invoices.map((inv, index) => (
                <tr key={index} className="border-b border-gray-700 hover:bg-gray-800/50 transition">
                  <td className="px-6 py-3">{inv.invoiceNumber}</td>
                  <td className="px-6 py-3">{inv.productName}</td>
                  <td className="px-6 py-3">{inv.customerName}</td>
                  <td className="px-6 py-3">{inv.warehouseName}</td>
                  <td className="px-6 py-3">{inv.quantity}</td>
                  <td className="px-6 py-3">
                    <span
                      className={`px-2 py-1 rounded-full text-xs font-semibold ${
                        inv.status === "Paid"
                          ? "bg-green-700/50 text-green-200"
                          : "bg-red-700/50 text-red-200"
                      }`}
                    >
                      {inv.status}
                    </span>
                  </td>
                  <td className="px-6 py-3 text-center space-x-2">
                    <button
                      onClick={() => EditInvoiceBtn(index)}
                      className="text-blue-400 hover:underline"
                    >
                      Edit
                    </button>
                    <button
                      onClick={() => DeleteInvoiceBtn(index)}
                      className="text-red-400 hover:underline"
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
              {invoices.length === 0 && (
                <tr>
                  <td colSpan={7} className="text-center py-6 text-gray-400 italic">
                    No invoices found.
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

// Invoice Form
type InvoiceFormProps = {
  invoice: InvoiceData | null;
  products: ProductData[];
  warehouses: WarehouseData[];
  customers: CustomerData[];
  button_name: string;
  onClose: () => void;
};

function InvoiceForm({ invoice, products, warehouses, customers, button_name, onClose }: InvoiceFormProps) {
  const [invoiceNumber, setInvoiceNumber] = useState<number>(0);
  const [productId, setProductId] = useState<number>(0);
  const [warehouseId, setWarehouseId] = useState<number>(0);
  const [customerId, setCustomerId] = useState<number>(0);
  const [quantity, setQuantity] = useState<number>(0);
  const [status, setStatus] = useState<string>("Pending");

  useEffect(() => {
    if (invoice) {
      setInvoiceNumber(invoice.invoice_number);
      setProductId(invoice.product_id);
      setWarehouseId(invoice.warehouse_id);
      setCustomerId(invoice.customer_id);
      setQuantity(invoice.quantity);
      setStatus(invoice.status);
    }
  }, [invoice]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log({ invoiceNumber, productId, warehouseId, customerId, quantity, status });
    onClose();
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <h3 className="text-2xl font-bold text-cyan-300 mb-4 drop-shadow-[0_0_6px_rgba(0,200,255,0.7)]">
        {button_name}
      </h3>

      <div className="flex flex-col">
        <label className="text-cyan-200 mb-1">Invoice Number</label>
        <input
          type="number"
          value={invoiceNumber}
          onChange={(e) => setInvoiceNumber(Number(e.target.value))}
          className="bg-gray-800/70 border border-cyan-500/50 rounded-lg px-3 py-2 text-cyan-200 focus:outline-none focus:ring-2 focus:ring-cyan-400 transition"
        />
      </div>

      <div className="flex flex-col">
        <label className="text-cyan-200 mb-1">Product</label>
        <select
          value={productId}
          onChange={(e) => setProductId(Number(e.target.value))}
          className="bg-gray-800/70 border border-cyan-500/50 rounded-lg px-3 py-2 text-cyan-200 focus:outline-none focus:ring-2 focus:ring-cyan-400 transition"
        >
          <option value={0}>Select a product</option>
          {products.map((p) => (
            <option key={p.id} value={p.id}>{p.name}</option>
          ))}
        </select>
      </div>

      <div className="flex flex-col">
        <label className="text-cyan-200 mb-1">Customer</label>
        <select
          value={customerId}
          onChange={(e) => setCustomerId(Number(e.target.value))}
          className="bg-gray-800/70 border border-cyan-500/50 rounded-lg px-3 py-2 text-cyan-200 focus:outline-none focus:ring-2 focus:ring-cyan-400 transition"
        >
          <option value={0}>Select a customer</option>
          {customers.map((c) => (
            <option key={c.id} value={c.id}>{c.name}</option>
          ))}
        </select>
      </div>

      <div className="flex flex-col">
        <label className="text-cyan-200 mb-1">Warehouse</label>
        <select
          value={warehouseId}
          onChange={(e) => setWarehouseId(Number(e.target.value))}
          className="bg-gray-800/70 border border-cyan-500/50 rounded-lg px-3 py-2 text-cyan-200 focus:outline-none focus:ring-2 focus:ring-cyan-400 transition"
        >
          <option value={0}>Select a warehouse</option>
          {warehouses.map((w) => (
            <option key={w.id} value={w.id}>{w.name}</option>
          ))}
        </select>
      </div>

      <div className="flex flex-col">
        <label className="text-cyan-200 mb-1">Quantity</label>
        <input
          type="number"
          value={quantity}
          onChange={(e) => setQuantity(Number(e.target.value))}
          className="bg-gray-800/70 border border-cyan-500/50 rounded-lg px-3 py-2 text-cyan-200 focus:outline-none focus:ring-2 focus:ring-cyan-400 transition"
        />
      </div>

      <div className="flex flex-col">
        <label className="text-cyan-200 mb-1">Status</label>
        <select
          value={status}
          onChange={(e) => setStatus(e.target.value)}
          className="bg-gray-800/70 border border-cyan-500/50 rounded-lg px-3 py-2 text-cyan-200 focus:outline-none focus:ring-2 focus:ring-cyan-400 transition"
        >
          <option value="Pending">Pending</option>
          <option value="Paid">Paid</option>
        </select>
      </div>

      <div className="flex justify-end space-x-2">
        <button
          type="button"
          onClick={onClose}
          className="px-4 py-2 bg-gray-700/70 text-cyan-200 rounded-lg hover:bg-gray-600/70 transition"
        >
          Cancel
        </button>
        <button
          type="submit"
          className="px-4 py-2 bg-cyan-500/70 text-gray-900 font-semibold rounded-lg shadow-[0_0_6px_rgba(0,200,255,0.5)] hover:bg-cyan-400/70 transition"
        >
          {button_name}
        </button>
      </div>
    </form>
  );
}
