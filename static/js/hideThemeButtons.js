// needs to be added to every page except index.html because the buttons had to be added to base.html to be applied to every page
const hideButtons = () => {
    $('#themeSelectors').addClass('d-none')
}

hideButtons();