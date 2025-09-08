document.addEventListener("DOMContentLoaded", () => {
  const ctx = document.getElementById('categoryChart');
  if (!ctx) return; // prevent errors if chart missing
  const labels = JSON.parse(document.getElementById('chartLabels').textContent);
  const dataValues = JSON.parse(document.getElementById('chartData').textContent);

  const colors = [
      'rgba(54, 162, 235, 0.6)',
      'rgba(255, 206, 86, 0.6)',
      'rgba(75, 192, 192, 0.6)',
      'rgba(153, 102, 255, 0.6)',
      'rgba(255, 99, 132, 0.6)',
      'rgba(255, 159, 64, 0.6)'
  ];

  const backgroundColors = labels.map((_, i) => colors[i % colors.length]);

  new Chart(ctx, {
      type: 'bar',
      data: {
          labels: labels,
          datasets: [{
              label: 'Total Quantity',
              data: dataValues,
              backgroundColor: backgroundColors,
              borderColor: 'rgba(0,0,0,0.8)',
              borderWidth: 2
          }]
      },
      options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
              y: { beginAtZero: true }
          }
      }
  });
});

