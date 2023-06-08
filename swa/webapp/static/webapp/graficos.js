const ctx = document.getElementById('myChart');
const ctx1 = document.getElementById('myChart1');
const ctx2 = document.getElementById('myChart2');

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

new Chart(ctx1, {
    type: 'pie',
    data: {
        labels: labelsU2,
        datasets: [{
            label: 'Estudiantes Graduados',
            data: data2,
            backgroundColor: ColoresRandom(datosJson2),
            hoverOffset: 4
        }],    
    },
});

new Chart(ctx2, {
    type: 'bar',
    data: {
        labels: labelsU,
        datasets: [{
            label: 'Estudiantes Desertados',
            data: data3,
            backgroundColor: '#0d9488',
            borderWidth: 1
        }]
    },
    options: {
        indexAxis: 'y',
        scales: {
            y: {
                beginAtZero: true
            }
        },
    },
});

function ColoresRandom(colores) {
    var colors = [];
    var totalColors = colores.length;
    var startColor = { r: 31, g: 231, b: 213 };
    var endColor = { r: 35, g: 82, b: 78 };

    for (var i = 0; i < totalColors; i++) {
      var color = interpolar(startColor, endColor, i, totalColors);
      colors.push(color);
    }
  
    return colors;
  }
  function interpolar(startColor, endColor, step, totalSteps) {
    var r = Math.round(startColor.r + (endColor.r - startColor.r) * step / totalSteps);
    var g = Math.round(startColor.g + (endColor.g - startColor.g) * step / totalSteps);
    var b = Math.round(startColor.b + (endColor.b - startColor.b) * step / totalSteps);
    return 'rgb(' + r + ', ' + g + ', ' + b + ')';
  }
