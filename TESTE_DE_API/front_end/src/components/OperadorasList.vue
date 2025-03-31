<template>
  <div>
    <input 
      v-model="searchQuery" 
      @input="searchOperadoras" 
      placeholder="Buscar Operadoras..." 
      class="input"
    />
    <ul v-if="operadoras.length > 0">
      <li v-for="operadora in operadoras" :key="operadora.id">
        <strong>{{ operadora.nome_fantasia }}</strong>
        <p>{{ operadora.razao_social }}</p>
        <p>{{ operadora.cidade }}, {{ operadora.uf }}</p>
      </li>
    </ul>
    <p v-if="operadoras.length === 0 && searchQuery">Nenhuma operadora encontrada.</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '', 
      operadoras: [], 
    };
  },
  methods: {
    async searchOperadoras() {
      if (this.searchQuery.trim()) {
        try {
          
          const url = `http://localhost:5000/search?q=${encodeURIComponent(this.searchQuery.trim())}`;
          
          console.log('URL da requisição:', url); 

          const response = await fetch(url);
          
          if (response.ok) {
            const data = await response.json();
            console.log('Resposta da API:', data); 
            if (Array.isArray(data)) {
              this.operadoras = data;
            } else {
              this.operadoras = [];
            }
          } else {
            console.error('Erro ao buscar dados:', response.status);
            this.operadoras = [];
          }
        } catch (error) {
          console.error('Erro ao buscar as operadoras:', error);
          this.operadoras = [];
        }
      } else {
        this.operadoras = [];
      }
    },
  },
};
</script>

<style scoped>

.input {
  padding: 8px;
  margin-bottom: 10px;
  width: 100%;
  max-width: 400px;
  border: 1px solid #ccc;
  border-radius: 4px;
}


ul {
  list-style-type: none;
  padding-left: 0;
}


li {
  margin-bottom: 10px;
}

strong {
  font-size: 16px;
  color: #333;
}

p {
  margin: 0;
  color: #666;
}


p.no-results {
  color: #e74c3c;
  font-weight: bold;
}
</style>
