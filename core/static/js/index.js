// DEIXA OS MENUS COM ASPECTO SELECIONADO E DESMARCA O ANTERIOR
const buttons = document.querySelectorAll('.container-options button');

buttons.forEach(button => {
    button.addEventListener('click', () => {
        // remove active de todos
        buttons.forEach(btn => btn.classList.remove('active'));

        // adiciona active no clicado
        button.classList.add('active');
    });
});
