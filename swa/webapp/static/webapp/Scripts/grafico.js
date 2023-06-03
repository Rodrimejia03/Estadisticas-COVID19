const ctx = document.getElementById('myChart');
        const ctx1 = document.getElementById('myChart1');
        const ctx2 = document.getElementById('myChart2');

        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Semestre 1', 'Semestre 2'],
                datasets: [{
                    label: 'Estudiantes inscritos',
                    data: [1097, 478],
                    backgroundColor: ['#0d9488', '#0f766e'],
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
                labels: ['Semestre 1', 'Semestre 2'],
                datasets: [{
                    label: 'Estudiantes desertados',
                    data: [300, 50],
                    backgroundColor: [
                        '#0d9488',
                        '#0f766e',
                    ],
                    hoverOffset: 4
                }]
            },
        });

        const xValues = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
        new Chart(ctx2, {
            type: 'line',
            data: {
                labels: xValues,
                datasets: [
                    {
                        label: 'Semestre 1',
                        data: [1860, 1740, 1700, 1400, 1070, 1110],
                        backgroundColor: '#0f766e',
                        borderColor: '#0f766e',
                        fill: false
                    }, {
                        label: 'Semestre 2',
                        data: [1500, 1850, 1300, 1600, 1000, 700],
                        backgroundColor: '#115e59',
                        borderColor: '#115e59',
                        fill: false
                    }
                ]
            },
            options: {
                legend: {
                    display: false
                },
            },
        });