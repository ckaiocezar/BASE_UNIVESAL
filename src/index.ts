import express = require('express');
import dotenv from 'dotenv';

dotenv.config();

const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Servidor rodando com sucesso!');
});

app.listen(port, () => console.log(`Servidor rodando em http://localhost:${port}`));
