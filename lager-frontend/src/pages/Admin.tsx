import Layout from "../components/Layout";
import LoginForm from "../components/Login";
// import type { Product } from "../types/types";
// import "./Products.css";

export default function AdminPage() {

    return (
        <Layout>
            <h2>Admin</h2>
            <LoginForm/>
        </Layout>
    );
}