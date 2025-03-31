// Function to simulate biometric authentication
function authenticateUser() {
    let authMessage = document.getElementById("authMessage");

    // Show processing message
    authMessage.innerText = "🔍 Verifying identity...";
    authMessage.style.color = "yellow";

    setTimeout(() => {
        // Simulate successful authentication
        authMessage.innerText = "✅ Authentication Successful!";
        authMessage.style.color = "lightgreen";
    }, 2000);
}

// Function to handle voting
function vote(candidate) {
    // Simulate vote processing
    setTimeout(() => {
        // Redirect to success page after voting
        window.location.href = "success.html";
    }, 2000);
}
