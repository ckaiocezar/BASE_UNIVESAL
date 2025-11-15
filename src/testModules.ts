import axios from "axios";

// Lista de endpoints para teste
const endpoints = [
  "http://localhost:3000/",
  "http://localhost:3000/teste",
  // Adicione outros endpoints dos módulos que você tem
];

async function testarEndpoints() {
  for (const url of endpoints) {
    try {
      const response = await axios.get(url);
      console.log(`[OK] ${url} -> status ${response.status}`);
      console.log(`Resposta:`, response.data);
    } catch (err: any) {
      console.log(`[ERRO] ${url} ->`, err.message);
    }
  }
}

testarEndpoints();
