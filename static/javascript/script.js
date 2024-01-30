document.addEventListener("DOMContentLoaded", function() {
    // Generar ceniza y agregarla al contenedor
    const ashContainer = document.getElementById("ash-container");
    const navHeight = document.querySelector("nav").offsetHeight;

    for (let i = 0; i < 100; i++) {
        const ash = document.createElement("div");
        ash.className = "ash";
        ash.style.left = `${Math.random() * 100}vw`;
        ash.style.top = `${-Math.random() * navHeight}px`;
        ash.style.animationDuration = `${Math.random() * 5 + 5}s`;
        ash.style.animationDelay = `-${Math.random() * 5}s`;
        ashContainer.appendChild(ash);
    }

    // Selecciona los elementos con las clases .content1, .content2, .content3 y .content4
    const contentElements = document.querySelectorAll('.content1, .content2, .content3, .content4');

    // Agrega la clase .in a los elementos para activar la animación automáticamente
    contentElements.forEach(contentElement => {
        contentElement.classList.toggle('in');
    });

    const hechos = document.querySelectorAll(".hechos li");

    for (const hecho of hechos) {
        const detalles = hecho.querySelector(".detalles a");
        const senalar = hecho.querySelector(".senalar a");

        detalles.addEventListener("mouseover", function() {
            detalles.classList.toggle("hover");
        });

        detalles.addEventListener("mouseout", function() {
            detalles.classList.toggle("hover");
        });

        senalar.addEventListener("mouseover", function() {
            senalar.classList.toggle("hover");
        });

        senalar.addEventListener("mouseout", function() {
            senalar.classList.toggle("hover");
        });

    }
});
