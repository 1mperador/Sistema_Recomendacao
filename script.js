// Substitua pela URL do seu back-end
const API_URL = "https://seu-backend.com/api";

// Exemplo de requisição para buscar dados
fetch(`${API_URL}/buscar`) // Substitua "/buscar" pela rota do seu servidor
  .then(response => response.json())
  .then(data => console.log("Dados recebidos:", data))
  .catch(error => console.error("Erro ao buscar dados:", error));


//   TODO NÃO SEI SE TA CERTO