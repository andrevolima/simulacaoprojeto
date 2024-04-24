// script.js
document.addEventListener('DOMContentLoaded', function () {
    const campeonatosList = document.getElementById('campeonatos-list');

    // Função para carregar os campeonatos
    function carregarCampeonatos() {
        fetch('http://127.0.0.1:8000/campeonatos/')
            .then(response => response.json())
            .then(campeonatos => {
                // Limpar a lista antes de adicionar os campeonatos
                campeonatosList.innerHTML = '';

                campeonatos.forEach(campeonato => {
                    // Criar elemento de lista para cada campeonato
                    const listItem = document.createElement('li');

                    // Texto do campeonato
                    listItem.textContent = campeonato.nome;

                    // Botão para acessar o campeonato
                    const button = document.createElement('button');
                    button.textContent = 'Acessar';
                    button.addEventListener('click', () => {
                        const senhaCampeonato = document.getElementById('senha-acessar-campeonato').value;
                        acessarCampeonato(campeonato.id, senhaCampeonato);
                    });
                    listItem.appendChild(button);

                    campeonatosList.appendChild(listItem);
                });
            })
            .catch(error => console.error('Erro ao buscar campeonatos:', error));
    }

    // Função para acessar um campeonato
    function acessarCampeonato(campeonatoId, senhaCampeonato) {
        fetch(`http://127.0.0.1:8000/campeonatos/${campeonatoId}/`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${senhaCampeonato}`
            }
        })
        .then(response => {
            if (response.ok) {
                window.location.href = `times.html?campeonato_id=${campeonatoId}`;
            } else {
                throw new Error('Senha incorreta');
            }
        })
        .catch(error => console.error(error));
    }

    // Carregar os campeonatos ao carregar a página
    carregarCampeonatos();

    // Adicionar evento de submit ao formulário para adicionar campeonato
    const addCampeonatoForm = document.getElementById('add-campeonato-form');
    addCampeonatoForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const nomeCampeonato = document.getElementById('nome-campeonato').value;
        const senhaCampeonato = document.getElementById('senha-campeonato').value; // Capturar valor do campo de senha
    
        fetch('http://127.0.0.1:8000/campeonatos/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                nome: nomeCampeonato, 
                senha: senhaCampeonato // Enviar senha junto com o nome
            })
        })
        .then(response => {
            if (response.ok) {
                carregarCampeonatos(); // Recarregar a lista de campeonatos após adicionar um novo
                document.getElementById('nome-campeonato').value = ''; // Limpar o campo de nome
                document.getElementById('senha-campeonato').value = ''; // Limpar o campo de senha
            } else {
                throw new Error('Erro ao adicionar campeonato');
            }
        })
        .catch(error => console.error(error));
    });
});
