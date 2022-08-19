(function () {

    const btnDelete = document.querySelectorAll(".btnDelete");

    btnDelete.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Confirm to delete?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });

})();