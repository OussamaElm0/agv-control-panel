let dates = window.dates
let counts = window.counts

var ctx = document.getElementById('commands-chart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',  // You can use 'line' for a line chart
        data: {
            labels: dates,
            datasets: [{
                label: 'Number of Commands',
                data: counts,
                backgroundColor: 'rgba(54, 162, 235, 0.2)', // Adjust color as needed
                borderColor: 'rgba(54, 162, 235, 1)',     // Adjust color as needed
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });