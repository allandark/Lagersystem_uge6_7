import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import dotenv from 'dotenv';
import path from 'path';


// Load your custom env file
dotenv.config({ path: path.resolve(__dirname, 'globals.env') });


// https://vite.dev/config/
export default defineConfig({  
  define: {
    'import.meta.env.VITE_API_URL': JSON.stringify(process.env.VITE_API_URL),
    'import.meta.env.VITE_VERSION': JSON.stringify(process.env.VITE_VERSION),
  },
  plugins: [
    react({
      babel: {
        plugins: [['babel-plugin-react-compiler']],
      },
    }),
  ],
  build: {
      sourcemap: true
    }
})
