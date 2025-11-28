const wheel = document.getElementById('wheel');
const btn = document.getElementById('btn-girar');
const numeroEl = document.getElementById('numero');
const colorEl = document.getElementById('color');

let currentRotation = 0;

// Orden de números en la ruleta europea (empezando arriba y yendo en sentido horario)
const numerosRuleta = [
    0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5,
    24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26
];

// Mapa número → índice
const numeroAIndice = {};
numerosRuleta.forEach((n, i) => { numeroAIndice[n] = i; });

// Ángulo por casilla
const ANGULO = 360 / 37;

btn.addEventListener('click', async () => {
    btn.disabled = true;
    numeroEl.textContent = '--';
    colorEl.textContent = '---';

    // Giro “random” primero solo visual
    const vueltas = 4;
    const extra = Math.random() * 360;
    currentRotation += vueltas * 360 + extra;
    wheel.style.transition = 'transform 2.8s cubic-bezier(0.17, 0.67, 0.12, 0.98)';
    wheel.style.transform = `rotate(${currentRotation}deg)`;

    // Esperar a que termine el giro visual
    await new Promise(r => setTimeout(r, 2800));

    try {
        const res = await fetch("{% url 'girar_ruleta' %}");
        const data = await res.json();

        const indice = numeroAIndice[data.numero];
        const anguloNumero = indice * ANGULO;

        // Queremos que el número ganador quede arriba, bajo la flecha.
        // Como la flecha está fija, giramos la rueda en sentido contrario.
        const rotacionBase = Math.round(currentRotation / 360) * 360;
        const rotacionFinal = rotacionBase - anguloNumero;

        wheel.style.transition = 'transform 0.8s ease-out';
        wheel.style.transform = `rotate(${rotacionFinal}deg)`;
        currentRotation = rotacionFinal;

        numeroEl.textContent = data.numero;
        colorEl.textContent = data.color.toUpperCase();
    } catch (e) {
        console.error(e);
    } finally {
        btn.disabled = false;
    }
});
