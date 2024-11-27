const encomendas = [
    { produto: 'Produto A', cliente: 'João', quantidade: 2 },
    { produto: 'Produto B', cliente: 'Maria', quantidade: 1 },
    { produto: 'Produto C', cliente: 'João', quantidade: 3 },
    { produto: 'Produto D', cliente: 'Ana', quantidade: 4 },
    { produto: 'Produto E', cliente: 'Maria', quantidade: 2 },
];

document.getElementById('clienteForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    document.getElementById('encomendaList').innerHTML = '';

    const cliente = document.getElementById('cliente').value;
    const resultado = encomendas.filter(encomenda => encomenda.cliente.toLowerCase() === cliente.toLowerCase());

    if (resultado.length > 0) {
        resultado.forEach(encomenda => {
            const li = document.createElement('li');
            li.textContent = `Produto: ${encomenda.produto} | Quantidade: ${encomenda.quantidade}`;
            document.getElementById('encomendaList').appendChild(li);
        });
    } else {
        const li = document.createElement('li');
        li.textContent = 'Nenhuma encomenda encontrada para este cliente.';
        document.getElementById('encomendaList').appendChild(li);
    }

    document.getElementById('clienteForm').reset();
});

document.addEventListener("DOMContentLoaded", function() {
    const rastreioModal = document.getElementById('rastreioModal');
    rastreioModal.addEventListener('shown.bs.modal', function () {
        const map = L.map('map').setView([-23.55052, -46.633308], 5);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        const cidadeA = L.marker([-23.55052, -46.633308]).addTo(map).bindPopup('Cidade A - Origem');
        const cidadeB = L.marker([-22.9035, -43.2096]).addTo(map).bindPopup('Cidade B - Destino');

        const rota = L.polyline([[-23.55052, -46.633308], [-22.9035, -43.2096]], {color: 'blue'}).addTo(map);
        map.fitBounds(rota.getBounds());
    });
});
