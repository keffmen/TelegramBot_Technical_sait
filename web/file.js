let tg = window.Telegram.WebApp;

function generateRandomId() {
    return Math.random().toString(36).substring(2) + Date.now().toString(36);
}


window.addEventListener('load', function() {
    tg.expand();
    document.getElementById('Name').value = tg.initDataUnsafe.user.first_name + ' ' + tg.initDataUnsafe.user.last_name
    console.log('Страница полностью загружена');
});


function uploadServer(){
    var input = document.getElementById('input_photo')
    var file = input.files[0];
    var orgInput = document.getElementById('org')
    var nameInput = document.getElementById('Name')
    var telInput = document.getElementById('phoneNumber')
    var nameInput = document.getElementById('problem')


    // Проверка наличия данных в полях
    if (!file || !nameInput.value || !orgInput.value || !telInput.value) {
        alert('Пожалуйста, заполните все поля формы.');
        return;
    }


    var formData = new FormData();
    var id = generateRandomId()
    formData.append('id', id);
    formData.append('image', file);
    formData.append('name', nameInput.value);
    formData.append('org', orgInput.value);
    formData.append('phone', telInput.value);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/upload', true);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            alert('Заявка отправлена' + id )
            console.log(xhr.responseText);
            tg.close();
        }
        else{
            alert('Ошибка отправки!')
            console.log(xhr.responseText);
        }
    };

    xhr.send(formData);
}