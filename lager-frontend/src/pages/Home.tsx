import Layout from "../components/Layout";
// import { useNavigate } from "react-router-dom";
import DailyReddit from "../components/DailyReddit";
export default function Home() {
  // const navigate = useNavigate();
  return (
    <Layout>
<section className="flex flex-col items-center justify-center text-center py-20">
        <h2 className="text-4xl md:text-6xl font-bold mb-4 text-transparent bg-clip-text 
                       bg-linear-to-r from-blue-400 via-purple-400 to-pink-400
                       bg-size-[200%_200%] animate-gradient-colors text-glow
                       leading-tight">
          Welcome to Lagersystem
        </h2>
        <p className="text-gray-400 max-w-xl mb-8">
          Manage your inventory effortlessly with a modern, sleek interface. 
          Track, update, and visualize your stock in real-time.
        </p>
 
      </section>

      <DailyReddit/>

      {/* Features Section */}
      <section className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-16 px-4 md:px-16">
        <div className="bg-gray-800 p-6 rounded-xl shadow-lg hover:shadow-2xl transition">
          <h3 className="text-xl font-bold mb-2">Real-Time Tracking</h3>
          <p className="text-gray-400">Monitor your inventory in real-time with instant updates.</p>
        </div>
        <div className="bg-gray-800 p-6 rounded-xl shadow-lg hover:shadow-2xl transition">
          <h3 className="text-xl font-bold mb-2">Analytics</h3>
          <p className="text-gray-400">Gain insights from detailed analytics and reports.</p>
        </div>
        <div className="bg-gray-800 p-6 rounded-xl shadow-lg hover:shadow-2xl transition">
          <h3 className="text-xl font-bold mb-2">Easy Management</h3>
          <p className="text-gray-400">Update stock levels, add new items, and manage categories effortlessly.</p>
        </div>
      </section>
    </Layout>
  );
}