const changeTheme = () => {
    $('body')
    .css('background-color', '#3a6596')
    .css('color', '#ffffff');
    $('#Blue')
    .removeClass('btn-primary')
    .addClass('btn-light')
    .css('color', ('#3a6596'));
    $('.btn-block').css('color', '#ffffff');
}

const defaultTheme = () => {
    $('body')
    .css('background-color', '#ffffff')
    .css('color', '#000');
    $('#Blue')
    .removeClass('btn-light')
    .addClass('btn-primary')
    .css('color', ('#fff'));
    $('.btn-block').css('color', '#000');
}

const toggleBlueButton = document.getElementById('Blue');
toggleBlueButton.addEventListener("click", changeTheme);

const toggleDefaultButton = document.getElementById('default');
toggleDefaultButton.addEventListener('click', defaultTheme)