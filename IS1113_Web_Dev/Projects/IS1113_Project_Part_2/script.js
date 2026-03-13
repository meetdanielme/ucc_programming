// ===== Tabs =====
const tab_links = document.querySelectorAll(".tab-link");
const tab_sections = document.querySelectorAll(".tab-section");

function show_tab(tab_id) {
    // Hide all sections
    tab_sections.forEach((section) => {
        section.classList.remove("active-section");
    });

    // Remove active style from all links
    tab_links.forEach((link) => {
        link.classList.remove("active-tab");
    });

    // Show selected section
    const selected_section = document.getElementById(tab_id);
    if (selected_section) {
        selected_section.classList.add("active-section");
    }

    // Highlight clicked link
    tab_links.forEach((link) => {
        if (link.dataset.tab === tab_id) {
            link.classList.add("active-tab");
        }
    });
}

// Add click event to each tab link
tab_links.forEach((link) => {
    link.addEventListener("click", () => {
        show_tab(link.dataset.tab);
    });
});

// Set default visible tab on page load
show_tab("professional-summary");


// ===== Contact modal =====
const contactButton = document.getElementById("contact-button");
const contactModal = document.getElementById("contact-modal");
const closeModalButton = document.getElementById("close-modal");
const contactForm = document.getElementById("contact-form");

const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const titleInput = document.getElementById("title");
const messageInput = document.getElementById("message");

function openModal() {
    contactModal.classList.add("show");
}

function closeModal() {
    contactModal.classList.remove("show");
}

contactButton.addEventListener("click", openModal);
closeModalButton.addEventListener("click", closeModal);

// Close when clicking outside form window
contactModal.addEventListener("click", (event) => {
    if (event.target === contactModal) {
        closeModal();
    }
});


// ===== Form validation =====
function setError(inputElement, errorElementId, message) {
    const errorElement = document.getElementById(errorElementId);
    inputElement.classList.add("invalid");
    errorElement.textContent = message;
}

function clearError(inputElement, errorElementId) {
    const errorElement = document.getElementById(errorElementId);
    inputElement.classList.remove("invalid");
    errorElement.textContent = "";
}

contactForm.addEventListener("submit", (event) => {
    event.preventDefault();
    let isValid = true;

    clearError(nameInput, "name-error");
    clearError(emailInput, "email-error");
    clearError(titleInput, "title-error");
    clearError(messageInput, "message-error");

    if (nameInput.value.trim() === "") {
        setError(nameInput, "name-error", "Please enter your name.");
        isValid = false;
    }

    const emailValue = emailInput.value.trim();
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (emailValue === "") {
        setError(emailInput, "email-error", "Please enter your email.");
        isValid = false;
    } else if (!emailPattern.test(emailValue)) {
        setError(emailInput, "email-error", "Please enter a valid email address.");
        isValid = false;
    }

    if (titleInput.value.trim() === "") {
        setError(titleInput, "title-error", "Please enter a message title.");
        isValid = false;
    }

    if (messageInput.value.trim() === "") {
        setError(messageInput, "message-error", "Please enter a message.");
        isValid = false;
    }

    if (!isValid) {
        return;
    }

    const TO_EMAIL = "125701129@umail.ucc.ie";
    const subject = titleInput.value.trim();
    const body = messageInput.value.trim();

    const mailtoUrl =
        `mailto:${TO_EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;

    window.location.href = mailtoUrl;
});