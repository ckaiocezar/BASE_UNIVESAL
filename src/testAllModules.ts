// src/testAllModules.ts
import express from "express";
import dotenv from "dotenv";
import axios from "axios";
import { PrismaClient } from "@prisma/client";

console.log("=== Iniciando testes da base completa ===");

// 1️⃣ Teste dotenv
console.log("\n[TESTE] dotenv:");
dotenv.config();
if (process.env.NODE_ENV) {
  console.log("✅ Variável de ambiente carregada: NODE_ENV =", process.env.NODE_ENV);
} else {
  console.log("⚠️ Nenhuma variável NODE_ENV encontrada. dotenv OK se você tiver .env");
}

// 2️⃣ Teste Express
console.log("\n[TESTE] Express:");
const app = express();
const PORT = 4000;
const server = app.listen(PORT, () => {
  console.log(`✅ Express iniciado com sucesso em http://localhost:${PORT}`);
});
setTimeout(() => {
  server.close(() => console.log("✅ Servidor Express encerrado após teste"));
}, 2000); // fecha após 2s

// 3️⃣ Teste Axios
console.log("\n[TESTE] Axios:");
axios.get("https://jsonplaceholder.typicode.com/todos/1")
  .then(res => console.log("✅ Axios retornou:", res.data))
  .catch((err: any) => console.error("❌ Axios erro:", err));

// 4️⃣ Teste Prisma
console.log("\n[TESTE] Prisma:");
const prisma = new PrismaClient();
prisma.$connect()
  .then(() => {
    console.log("✅ Prisma conectado ao banco com sucesso!");
    return prisma.$disconnect();
  })
  .catch((err: any) => console.error("❌ Prisma erro:", err));
