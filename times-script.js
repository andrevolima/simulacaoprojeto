document.addEventListener('DOMContentLoaded', function () {
    const urlParams = new URLSearchParams(window.location.search);
    const campeonatoId = urlParams.get('campeonato_id');
    
    if (campeonatoId) {
        fetch(`http://localhost:8000/campeonatos/${campeonatoId}/times/`)
            .then(response => response.json())
            .then(times => {
                const timesList = document.getElementById('times-list');
                times.forEach(time => {
                    const listItem = document.createElement('li');
                    listItem.textContent = time.nome;
                    timesList.appendChild(listItem);
                });
            })
            .catch(error => console.error('Erro ao buscar times:', error));
    } else {
        console.error('ID do campeonato não encontrado na URL.');
    }
});
