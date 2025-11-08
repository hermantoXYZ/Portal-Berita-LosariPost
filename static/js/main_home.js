
document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelector('.slides');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');

    if (slides && prevBtn && nextBtn) {
        const scrollAmount = slides.clientWidth;

        nextBtn.addEventListener('click', () => {
            slides.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        });

        prevBtn.addEventListener('click', () => {
            slides.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        });
    }
});