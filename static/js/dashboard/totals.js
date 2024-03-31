// Access the total AGVs value from Django context
let totalAGVs = window.totalAGVs;
let totalBLOCs = window.totalBLOCs;
let totalPOSTEs = window.totalPOSTEs;

// Data
var data = {
  labels: ["AGVs", "POSTEs", "BLOCs"],
  datasets: [
    {
      label: "Total AGVs",
      data: [totalAGVs, 0, 0], // Adjust data as needed, assuming other values are 0 initially
      backgroundColor: "rgba(255, 99, 132, 0.2)", // Color for AGVs
      borderColor: "rgba(255, 99, 132, 1)", // Border color for AGVs
      borderWidth: 1,
    },
    {
      label: "Total POSTEs",
      data: [0, totalPOSTEs, 0], // Adjust data as needed, assuming other values are 0 initially
      backgroundColor: "rgba(54, 162, 235, 0.2)", // Color for POSTEs
      borderColor: "rgba(54, 162, 235, 1)", // Border color for POSTEs
      borderWidth: 1,
    },
    {
      label: "Total BLOCs",
      data: [0, 0, totalBLOCs], // Adjust data as needed, assuming other values are 0 initially
      backgroundColor: "rgba(255, 206, 86, 0.2)", // Color for BLOCs
      borderColor: "rgba(255, 206, 86, 1)", // Border color for BLOCs
      borderWidth: 1,
    },
  ],
};

// Use Chart.js to create a bar chart
var ctx = document.getElementById("totals-chart").getContext("2d");
var totalsChart = new Chart(ctx, {
  type: "bar",
  data: data,
  options: {
    responsive: false,
    plugins: {
      legend: {
        position: "top",
      },
      title: {
        display: true,
        text: "Totals",
      },
    },
  },
});
