document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('form');
  const usernameInput = form.querySelector('input[name="username"]');
  const passwordInput = form.querySelector('input[name="password"]');

  form.addEventListener('submit', function(event) {
      // Basic validation
      if (usernameInput.value.trim() === '' || passwordInput.value.trim() === '') {
          event.preventDefault();
          alert('Please fill in both fields.');
      } else {
          // Optional: Add a loading animation or spinner
          const button = form.querySelector('button');
          button.innerHTML = 'Logging in...';
          button.disabled = true;
      }
  });

  // Optional: Add more advanced validation or features here
});
