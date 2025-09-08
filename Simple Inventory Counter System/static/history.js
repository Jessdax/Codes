// Render chart for inventory by category
document.addEventListener("DOMContentLoaded", () => {
    const ctx = document.getElementById('categoryChart').getContext('2d');
    const labels = JSON.parse(document.getElementById('chartLabels').textContent);
    const quantities = JSON.parse(document.getElementById('chartData').textContent);

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Total Quantity',
                data: quantities,
                backgroundColor: 'rgba(26, 188, 156, 0.6)',
                borderColor: 'rgba(26, 188, 156, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: { y: { beginAtZero: true } }
        }
    });
});
