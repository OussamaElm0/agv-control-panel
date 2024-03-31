let mostAgvUsed = window.mostAgvsUsed;

// Extract AGV names and usage counts from the data
const labels = mostAgvUsed.map(({ name }) => name);
const usageCounts = mostAgvUsed.map(({ usage_count }) => usage_count);

const data = {
    labels,
    datasets: [
        {
        label: 'AGV Usage Count',
        data: usageCounts,
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1,
        },
    ],
};

const config = {
    type: 'bar',
    data,
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
};

const mostAgvsUsedChart = new Chart(
  document.getElementById("most-agvs-used").getContext(''),
  config
);  