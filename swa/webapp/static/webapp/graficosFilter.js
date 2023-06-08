const ctx = document.getElementById('myChart');
const ctx1 = document.getElementById('myChart1');
const ctx2 = document.getElementById('myChart2');


if(true){
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labelsU,
            datasets: [{
                label: 'Estudiantes inscritos',
                data: data1,
                backgroundColor: '#0d9488',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            },  
        },
    });
    
} else{
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labelsU,
            datasets: [{
                label: 'Estudiantes inscritos',
                data: data1,
                backgroundColor: '#0d9488',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            },  
        },
    });
    
}