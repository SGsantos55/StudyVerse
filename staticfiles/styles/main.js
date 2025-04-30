document.addEventListener("DOMContentLoaded", () => {
    // Example JS to enhance interactivity (e.g., show a success message on search)
    const searchButton = document.querySelector(".search-button");
    const searchInput = document.querySelector(".search-input");

    searchButton.addEventListener("click", (e) => {
        if (searchInput.value.trim() !== "") {
            // Example: Simulate search success (In a real scenario, you might want to handle this server-side)
            alert("Searching for: " + searchInput.value);
        } else {
            alert("Please enter a search term.");
        }
    });
});
