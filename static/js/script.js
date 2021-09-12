// function to apply the alterntive color scheme
const changeTheme = () => {
    setTheme("theme-blue");
    $("main").addClass("theme-blue").removeClass("theme-default");
    console.log("blue");
    $(".stay-black").css("color", "#000");
    $("label").css("color", "#000");
    $(".label-white").css("color", "#fff");
    $(".btn-block").css("color", "#fff");
};

// function to reapply the default theme
const defaultTheme = () => {
    setTheme("theme-default");
    $("main").addClass("theme-default").removeClass("theme-blue");
    console.log("default");
    $(".btn-block").css("color", "#000");
};

const toggleBlueButton = document.getElementById("Blue");
toggleBlueButton.addEventListener("click", changeTheme);

const toggleDefaultButton = document.getElementById("default");
toggleDefaultButton.addEventListener("click", defaultTheme);

// function to set a given theme/color-scheme
function setTheme(themeName) {
    localStorage.setItem("theme", themeName);
    document.documentElement.className = themeName;
}

// set theme to default for first time visitors or apply theme stored in local storage
function checkTheme() {
    if (localStorage.getItem("theme") === "") {
        defaultTheme();
    } else if (localStorage.getItem("theme") === "theme-blue") {
        changeTheme();
    }
}
checkTheme();
