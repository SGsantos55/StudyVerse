document.addEventListener("DOMContentLoaded", () => {
    // Scroll to the bottom of the conversation when new messages are added
    const messageWrapper = document.querySelector(".comment-wrapper");
    if (messageWrapper) {
        messageWrapper.scrollTop = messageWrapper.scrollHeight;
    }

    // Handle input for the message form (optional: character limit for message)
    const messageInput = document.querySelector(".message-input");
    if (messageInput) {
        messageInput.addEventListener("input", (e) => {
            const maxLength = 300;
            const charCount = e.target.value.length;
            if (charCount > maxLength) {
                e.target.value = e.target.value.substring(0, maxLength);
            }
        });
    }
});
