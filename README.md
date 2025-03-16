# Sistema de Recomendacoes 

Este é um sistema simples de recomendações de itens (como filmes) criado utilizando Python, Flask e MongoDB. O sistema permite adicionar itens com título, descrição e tags, exibir informações de um item na página inicial, e buscar itens com base em tags.

## Funcionalidades

- **Exibição de um filme**: A página inicial exibe o primeiro filme cadastrado no banco de dados. Caso nenhum filme esteja cadastrado, uma mensagem informativa é exibida.
- **Adicionação de itens**: Permite cadastrar novos itens com título, descrição e tags.
- **Busca de itens por tags**: Realiza uma busca por itens utilizando tags como critério.

## Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Banco de Dados**: MongoDB
- **Frontend**: HTML com templates Jinja2
- **Railway**: Hospedar Banco de dados

## Como Executar o Projeto

### Requisitos

1. `Python 3.12` ou superior
2. `MongoDB` instalado e em execução
3. Gerenciador de pacotes `pip`

### Passos

1. Clone este repositório:
   ```bash
   git clone <https://github.com/1mperador/Sistema_de_Recomendacoes_Simples.git>
   cd Sistema_de_Recomendacoes_Simples
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # No Windows: .venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Certifique-se de que o MongoDB está em execução:
   ```bash
   sudo systemctl start mongod
   ```

5. Inicie o servidor Flask:
   ```bash
   python app.py
   ```

6. Acesse o sistema no navegador no endereço:
   ```
   http://127.0.0.1:5000/
   ```

## Estrutura do Projeto

```
Sistema_de_Recomendacoes_Simples/
|— app.py               # Arquivo principal da aplicação Flask
|— templates/          # Arquivos HTML para renderização
|   |— base.html        # Template base
|   |— index.html       # Página inicial
|   |— adicionar.html   # Página para adicionar itens
|   |— buscar.html      # Página para buscar itens
|- notes.txt           # Apenas um rascunho de como estou pensando
|— static/             # Arquivos estáticos (ex.: imagens, CSS)
|— requirements.txt    # Lista de dependências do Python
```

## Exemplos de Uso

1. **Adicionando um Item**:
   - Acesse `http://127.0.0.1:5000/adicionar`.
   - Preencha o formulário com um título, uma descrição e tags separadas por vírgulas.
   - Clique em "Adicionar".

2. **Buscando por Tag**:
   - Acesse `http://127.0.0.1:5000/buscar`.
   - Insira uma tag no campo de busca e clique em "Buscar".

3. **Visualizando o Filme na Home**:
   - Acesse `http://127.0.0.1:5000/` para ver o primeiro filme cadastrado ou a mensagem de que não há filmes cadastrados.

## Possíveis Melhorias Futuras

- Adicionar suporte para edição e exclusão de itens.
- Implementar avaliação por usuários.
- Melhorar o design das páginas com CSS.
- Adicionar suporte para imagens personalizadas de cada item.

## Contribuições

Sinta-se à vontade para contribuir com melhorias! Para isso:
1. Faça um fork deste repositório.
2. Crie uma branch para suas alterações:
   ```bash
   git checkout -b minha-feature
   ```
3. Envie um pull request com suas melhorias.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

