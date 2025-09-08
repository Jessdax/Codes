// Optional: Confirm delete action
document.addEventListener('DOMContentLoaded', () => {
  let deleteUrl = null;

  // Open modal on delete link click
  document.querySelectorAll('a.delete-btn').forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault(); // prevent immediate navigation
      deleteUrl = this.href; // store URL
      document.getElementById('deleteModal').style.display = 'flex';
    });
  });

  // Cancel button closes modal
  document.getElementById('cancelBtn').addEventListener('click', () => {
    document.getElementById('deleteModal').style.display = 'none';
    deleteUrl = null;
  });

  // Confirm delete redirects
  document.getElementById('confirmDeleteBtn').addEventListener('click', () => {
    if (deleteUrl) {
      window.location.href = deleteUrl;
    }
  });
});


window.addEventListener('DOMContentLoaded', () => {
    const criticalRows = document.querySelectorAll('tr.critical');
    if (criticalRows.length > 0) {
      const notice = document.getElementById('low-stock-notice');
      let message = "⚠️ Critically low stock for the following items:<br>";
      criticalRows.forEach(row => {
        const name = row.children[1].textContent;
        const qty = row.children[2].textContent;
        message += `- ${name}: ${qty}<br>`;
      });
      notice.innerHTML = message;
      notice.style.display = "block";
  
      // Auto-hide after 5 seconds with fade-out
      setTimeout(() => {
        notice.classList.add('fade-out');
        // Remove from display after transition
        setTimeout(() => {
          notice.style.display = 'none';
        }, 1500); // matches CSS transition duration
      }, 5000); // 5 seconds before fading
    }
  });
  document.addEventListener("DOMContentLoaded", () => {
    const exportBtn = document.getElementById("exportBtn");
    if (exportBtn) {
      exportBtn.addEventListener("click", () => {
        let table = document.querySelector("table");
        if (!table) {
          alert("No table found to export!");
          return;
        }
        let rows = Array.from(table.querySelectorAll("tr"));
        let csvContent = rows.map(row => {
          let cols = Array.from(row.querySelectorAll("th, td"));
          return cols.map(col => `"${col.innerText}"`).join(",");
        }).join("\n");
  
        let blob = new Blob([csvContent], { type: "text/csv" });
        let url = window.URL.createObjectURL(blob);
        let a = document.createElement("a");
        a.setAttribute("href", url);
        a.setAttribute("download", "inventory_table.csv");
        a.click();
      });
    }
  });

  
  
  
  
  
  
