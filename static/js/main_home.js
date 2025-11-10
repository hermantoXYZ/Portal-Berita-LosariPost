document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelector('.slides');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');

    if (slides && prevBtn && nextBtn) {
        const scrollAmount = slides.clientWidth;

        // Fungsi scroll ke kanan
        const scrollNext = () => {
            slides.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        };

        // Fungsi scroll ke kiri
        const scrollPrev = () => {
            slides.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        };

        // Tombol manual
        nextBtn.addEventListener('click', scrollNext);
        prevBtn.addEventListener('click', scrollPrev);

        // Scroll otomatis setiap 5 detik (5000 ms)
        setInterval(scrollNext, 4000);
    }
});
