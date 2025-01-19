const banners = document.querySelectorAll(".banner-container .banner");
let currentIndex = 0;

// Função para alternar banners automaticamente
function rotateBanners() {
    banners[currentIndex].scrollIntoView({ behavior: "smooth", inline: "center" });
    currentIndex = (currentIndex + 1) % banners.length; // Volta ao primeiro após o último
}

// Alterna os banners a cada 3 segundos (se não houver interação do mouse)
let autoScroll = setInterval(rotateBanners, 3000);

// Pausa o auto-scroll ao interagir com o mouse
banners.forEach(banner => {
    banner.addEventListener("mouseenter", () => clearInterval(autoScroll));
    banner.addEventListener("mouseleave", () => {
        autoScroll = setInterval(rotateBanners, 3000);
    });
});
