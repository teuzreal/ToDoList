function filtrar() {
    const busca = document.getElementById("busca").value.toLowerCase();
    const tarefas = document.querySelectorAll(".tarefa");

    tarefas.forEach(t => {
        const titulo = t.querySelector(".titulo").innerText.toLowerCase();
        t.style.display = titulo.includes(busca) ? "flex" : "none";
    });
}