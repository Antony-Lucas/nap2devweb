//Alteração do DOM para trocar o formulário do modal login/signup
document.getElementById('show-signup').addEventListener('click', function (e) {
    e.preventDefault();
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('signup-form').style.display = 'block';
});

document.getElementById('show-login').addEventListener('click', function (e) {
    e.preventDefault();
    document.getElementById('signup-form').style.display = 'none';
    document.getElementById('login-form').style.display = 'block';
});

//Alteração do DOM para exibir os campos somente para PF e somente para PJ
document.addEventListener('DOMContentLoaded', function () {
    const pessoaFisicaRadio = document.getElementById('pessoaFisica');
    const empresaRadio = document.getElementById('empresa');
    const pessoaFisicaFields = document.getElementById('pessoaFisicaFields');
    const empresaFields = document.getElementById('empresaFields');
    function updateFields() {
        if (pessoaFisicaRadio.checked) {
            pessoaFisicaFields.style.display = 'block';
            empresaFields.style.display = 'none';
        } else if (empresaRadio.checked) {
            pessoaFisicaFields.style.display = 'none';
            empresaFields.style.display = 'block';
        }
    }

    pessoaFisicaRadio.addEventListener('change', updateFields);
    empresaRadio.addEventListener('change', updateFields);

    updateFields();
});