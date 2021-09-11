const changeTheme = () => {
    $('body')
    .css('background-color', '#3a6596')
    .css('color', '#ffffff');
    $('.btn-block').css('color', '#ffffff');
    $('.footer-text').css('color', '#000');
    $('.list-unstyled')
    .removeClass("text-white")
    .addClass('text-black');
}

const defaultTheme = () => {
    $('body')
    .css('background-color', '#ffffff')
    .css('color', '#000');
    $('.btn-block').css('color', '#000');
    $('.footer-text').css('color', '#fff');
    $('.list-unstyled')
    .removeClass('text-black')
    .addClass('text-white');
}

const toggleBlueButton = document.getElementById('Blue');
toggleBlueButton.addEventListener("click", changeTheme);

const toggleDefaultButton = document.getElementById('default');
toggleDefaultButton.addEventListener('click', defaultTheme)