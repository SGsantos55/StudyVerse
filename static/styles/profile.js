// JavaScript for profile page
document.addEventListener('DOMContentLoaded', function() {
    // Fade in effect for feed and activity sections
    const feedSection = document.querySelector('.main-content');
    const activitySection = document.querySelector('.activity');

    feedSection.style.opacity = 0;
    activitySection.style.opacity = 0;
    
    setTimeout(function() {
        feedSection.style.transition = "opacity 1s ease-in";
        activitySection.style.transition = "opacity 1s ease-in";
        feedSection.style.opacity = 1;
        activitySection.style.opacity = 1;
    }, 200); // Slight delay to allow page load
});
