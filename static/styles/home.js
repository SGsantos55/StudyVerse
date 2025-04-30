document.addEventListener('DOMContentLoaded', function () {
  const urlParams = new URLSearchParams(window.location.search);
  const currentTopic = urlParams.get('q');

  const topicLinks = document.querySelectorAll('.browse-topics a');

  topicLinks.forEach(link => {
    // Safely create full URL even from relative href
    const fullHref = new URL(link.getAttribute('href'), window.location.origin);
    const topicParam = fullHref.searchParams.get('q');

    if (topicParam === currentTopic) {
      link.classList.add('active');
    }
  });
});
