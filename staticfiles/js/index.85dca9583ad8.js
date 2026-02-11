const buttons = document.querySelectorAll(".menu-btn");
const views = document.querySelectorAll(".view");

buttons.forEach(button => {
    button.addEventListener("click", () => {

        buttons.forEach(btn => btn.classList.remove("active"));
        button.classList.add("active");

        views.forEach(view => view.classList.remove("active"));

        const target = button.dataset.view;
        document.getElementById(target).classList.add("active");

    });
});
