// login.js

document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const response = await fetch(form.action, {
        method: form.method,
        body: formData,
    });
    if (response.ok) {
        // Show success message pop-up
        document.getElementById('successPopup').style.display = 'block';
        // Redirect to users page after 2 seconds
        setTimeout(() => {
            window.location.href = '/users';
        }, 2000);
    } else {
        alert('Login failed. Please check your credentials.');
    }
});
