const express = require('express');
const app = express();
const port = 3000;

// Lista de operadoras
const operadoras = [
  {
    id: 701,
    nome_fantasia: "SEGUROS UNIMED",
    razao_social: "UNIMED SEGUROS SAÚDE S/A",
    modalidade: "Seguradora Especializada em Saúde",
    cnpj: "04487255000181",
    telefone: "11",
    logradouro: "ALAMEDA MINISTRO ROCHA AZEVEDO",
    numero: "346",
    bairro: "Edifício Seguros, andares térreo ao 9º",
    cidade: "CERQUEIRA CESAR",
    uf: "São Paulo",
    cep: "SP",
    cargo_representante: "compliance@segurosunimed.com.br",
  },
  // Adicione mais operadoras conforme necessário
];

// Rota de busca textual
app.get('/api/operadoras', (req, res) => {
  const { query } = req.query; // Pega o parâmetro de consulta 'query' da URL

  if (!query) {
    return res.status(400).json({ message: 'Query parameter is required' });
  }

  // Filtrando as operadoras que contém o texto da busca no nome_fantasia, razao_social ou cnpj
  const resultadoBusca = operadoras.filter((operadora) => {
    return (
      operadora.nome_fantasia.toLowerCase().includes(query.toLowerCase()) ||
      operadora.razao_social.toLowerCase().includes(query.toLowerCase()) ||
      operadora.cnpj.includes(query)
    );
  });

  // Retorna os resultados encontrados
  if (resultadoBusca.length === 0) {
    return res.status(404).json({ message: 'Nenhuma operadora encontrada' });
  }

  res.json(resultadoBusca);
});

// Inicializando o servidor
app.listen(port, () => {
  console.log(`Servidor rodando na porta http://localhost:${port}`);
});


