let mostAgvUsed = window.mostAgvsUsed;
console.log(mostAgvUsed)
// Extract AGV names and usage counts from the data
const labels = mostAgvUsed.map(({ name }) => name);
const usageCounts = mostAgvUsed.map(({ usage }) => usage);

console.log(usageCounts)

// Chart data
const pieChartData = {
  labels: labels,
  datasets: [{
    label: 'AGV Usage Count',
    data: usageCounts,
    backgroundColor: [
      'rgb(255, 99, 132)',
      'rgb(255, 159, 64)',
      'rgb(255, 205, 86)',
      'rgb(75, 192, 192)',
      'rgb(54, 162, 235)'
    ],
    borderWidth: 1
  }]
};

// Chart configuration
const pieChartConfig = {
  type: 'pie',
  data: pieChartData,
  options: {
    responsive: false,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Most AGVs Used'
      }
    }
  }
};

// Render the pie chart
const ctxPie = document.getElementById('most-agvs-used').getContext("2d");
const agvsChart = new Chart(
    ctxPie
    , pieChartConfig
)