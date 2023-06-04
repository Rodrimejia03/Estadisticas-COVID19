const ctx = document.getElementById('myChart');
const ctx1 = document.getElementById('myChart1');
const ctx2 = document.getElementById('myChart2');



new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Universidad El Salvador', 'Universidad Tecnologica de El Salvador', 'Universidad Don Bosco'],
        datasets: [{
            label: 'Estudiantes inscritos',
            data: [54531, 11530, 15600],
            backgroundColor: ['#0d9488', '#0f766e','#0f766e'],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    },
});

new Chart(ctx1, {
    type: 'pie',
    data: {
        labels: ['Universidad El Salvador', 'Universidad Tecnologica de El Salvador', 'Universidad Don Bosco'],
        datasets: [{
            label: 'Estudiantes desertados',
            data: [740, 550, 468],
            backgroundColor: [
                '#0d9488',
                '#0f766e',
                '#0f766e'
            ],
            hoverOffset: 4
        }]
    },
});